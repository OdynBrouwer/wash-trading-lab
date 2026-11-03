# 07 — Datalaag: van stream naar archief

Hoe live data binnenkomt, hoe je hem opslaat, en vooral: hoe je eerlijk blijft over
de gaten die erin zitten.

Dit document beschrijft het ontwerp. Er is een **minimale collector** (`scripts/collector.py`)
die publieke trades en diepte-diffs binnenhaalt en de volgnummers bewaakt. Wat er nog niet is:
het orderboek reconstrueren uit een snapshot plus diffs.

---

## 1. Waarom dit document bestaat

De formules zijn het makkelijke deel. De datalaag is waar een detectieproject
sneuvelt, om drie redenen:

1. **Tick-data is vluchtig.** Beurzen geven geen handelshistorie weg. Wat je vandaag
   niet opslaat, bestaat morgen niet meer. Er is geen download die dit oplost.
2. **Een gat lijkt op nepvolume.** Als jouw collector een uur mist, ziet een detector
   een volume-dip die er niet was. Zonder gatenadministratie meet je je eigen
   storingen.
3. **De gerapporteerde kant is geen databestand.** Wat een beurs *opgeeft* staat op
   een website of in een aggregator-API, niet in een eerlijk exportbestand.

## 2. Twee meetkanalen

Dit is de kern van D26 en het belangrijkste ontwerpbesluit in dit document.

| Kanaal | Wat je meet | Bron | Karakter |
|---|---|---|---|
| **Claim** | Het volume dat de beurs opgeeft aan de buitenwereld | Aggregator-API | Dagelijks, achteraf, klein |
| **Werkelijkheid** | Wat er feitelijk verhandeld is | Websocket tick-stream | Realtime, groot, vluchtig |

Ze zijn onafhankelijk, en **het verschil is het signaal**. Wie alleen het tick-kanaal
heeft, kan zeggen "dit volume gedraagt zich raar". Wie beide heeft, kan zeggen "deze
beurs claimt drie keer zoveel als er te zien was" — en dat is een veel hardere uitspraak.

Praktisch gevolg: de collector moet **beide** kanalen vullen, ook al is de claim-kant
maar één API-call per dag.

## 3. Streams per bron

### 3.1 CEX — publieke websocket
Per beurs en per pair heb je twee streams nodig:

| Stream | Wat je nodig hebt | Waarom |
|---|---|---|
| **Trades** | tijdstip, prijs, hoeveelheid, **agressor-kant** | Zonder agressor-kant zijn D11 (gepaarde prints) en D18 (Kyle's λ) niet betrouwbaar |
| **Diepte-diffs** | prijsniveau, nieuwe hoeveelheid, **volgnummer** | Voor D13, D14, D16 en D17 (D15 vereist eigen fills); het volgnummer is onmisbaar voor het gatenbeleid |

**Agressor-kant per venue.** Voor de eerste twee venues is bekend hoe je hem afleidt;
daarbuiten blijft het verifiëren.

| Venue | Veld | Afleiding | Status |
|---|---|---|---|
| Binance spot | `m` = *was the buyer the maker* | `aggressor = "SELL" if m else "BUY"` | `BEVESTIGD` |
| Bybit spot | `S` = *side of taker*, `Buy` of `Sell` | direct overnemen | `BEVESTIGD` |
| OKX spot | `side` = `buy` of `sell` per trade | direct overnemen | `BEVESTIGD` (live call) |
| Kraken spot | 4e veld van de trade-array: `b` of `s` | direct overnemen | `BEVESTIGD` |

**Regel: nooit de agressor-kant raden uit de prijsbeweging.** Ontbreekt het veld, dan blijft
het `NULL` en vallen D11 en D18 weg voor die venue. Een leeg veld is eerlijker dan een
geraden waarde.

**Endpoints.** Neem streamnamen en endpoints nooit uit dit document over: ze verschillen per
beurs en veranderen. Controleer ze per venue in de documentatie van de beurs zelf. De grote
beurzen bieden dit doorgaans gratis aan, met of zonder publieke sleutel.

**Tijdstempels.** Bewaar altijd twee velden: de beurs-timestamp en de lokale ontvangsttijd.
Het verschil daartussen is netwerkvertraging **plus klokoffset van deze machine** plus
verwerkingstijd; zonder een referentiemeting kun je die drie niet scheiden. Normaliseer naar
UTC in milliseconden en bewaar daarnaast de oorspronkelijke waarde met zijn eenheid.

Let op: Binance gebruikt **niet overal dezelfde eenheid**. De live `@trade`-stream leverde op
3 november 2026 een `T` van 13 cijfers — milliseconden — terwijl de maandelijkse
klines-bestanden vanaf 2025 microseconden bevatten. Laat de collector de eenheid daarom
**per bericht afleiden uit de grootte van het getal** en de gevonden eenheid opslaan; dat is
wat `scripts/collector.py` doet. `BEVESTIGD` (beide eenheden)

**Eén bericht is niet één trade.** Bybit kan tot **1024 trades** in één WebSocket-bericht
stoppen, en meerdere berichten kunnen hetzelfde `seq` dragen. Een collector die "één bericht =
één trade" aanneemt, verliest dus data zonder dat er een fout optreedt. Tel altijd de
`data`-array uit. `BEVESTIGD` — in de testrun van 3 november 2026 zaten er gemiddeld 3,8
trades in een Bybit-bericht en maximaal 37.

### 3.2 Aggregator — gerapporteerd volume
Één call per dag per beurs levert het geclaimde 24u-volume.

**Vermijd HTML-scraping.** Dat is wat Bitwise in 2019 deed, en het brak bij elke
redesign van een pagina. Gebruik de officiële API van de aggregator. Als die er niet
is, is dat een reden om die beurs niet te meten, niet om te gaan schrapen.

### 3.3 On-chain DEX
Volledig publiek en **permanent**: dat is waarom Victor & Weintraud hun analyse konden
doen. Je leest blokken, transacties en contract-events uit. Historisch én live
beschikbaar, gratis.

Dit is de enige bron waar T3 (tegenpartij-identiteit) haalbaar is.

## 4. Opslagschema

Formaat: **NDJSON, één bestand per dag per stream**, gecomprimeerd. Geen database in
fase 1 — dat voegt een afhankelijkheid toe zonder dat je iets kunt met de data die je
nog niet hebt.

Velden met geldbedragen en hoeveelheden als **string**, niet als float. Afronding in
floats is een stille foutenbron die je pas maanden later ontdekt.

### 4.1 Trades
```json
{"ts_event": 1730000000123, "ts_recv": 1730000000154, "venue": "...",
 "pair": "BTC/USDT", "seq": 4711, "price": "34120.50", "qty": "0.0032",
 "aggressor": "buy|sell|unknown", "trade_id": "..."}
```

Twee tijdstempels, niet één. `ts_event` komt van de beurs, `ts_recv` van jouw klok.
Het verschil is je eigen latentie, en de volgorde waarin ze voorkomen verraadt
herordening in de stream.

### 4.2 Orderboek
Twee lagen, want ruwe diffs zijn te groot om alles te bewaren:

| Laag | Inhoud | Bewaarbeleid |
|---|---|---|
| **Ruw** | elke diff zoals ontvangen, met volgnummer | rollend venster (30–90 dagen), daarna weg |
| **Samengevat** | top-of-book en top-10, één snapshot per seconde | voor altijd |

De samengevatte laag is genoeg voor D13–D16. De ruwe laag is alleen nodig voor D17
(cancel-ratio) en voor heranalyse.

### 4.3 Gatenlog
```json
{"ts_start": ..., "ts_end": ..., "venue": "...", "pair": "...", "stream": "depth",
 "seq_from": 120044, "seq_to": 120091, "reden": "reconnect|seq_jump|parse_error"}
```

Dit bestand is geen bijzaak. Zonder dit log is elke volumemeting onbetrouwbaar,
want je kunt achteraf niet meer zien of een dip echt was.

## 5. Volumeschatting

**Dit zijn schattingen, niet gemeten.** Ze moeten na de eerste week verzamelen
vervangen worden door echte cijfers.

| Stream | Orde van grootte | Opslag per dag |
|---|---|---|
| Trades, 1 pair op 1 drukke beurs | 10⁶ per dag | tientallen MB |
| Diepte-diffs, 1 pair | 10⁶–10⁷ berichten per dag | **~1 GB ongecomprimeerd** |
| Top-of-book, 1 seconde | 86.400 records | enkele MB |
| Claim-kant, 1 aggregator-call | 1 record per beurs | verwaarloosbaar |

Conclusie: **enkele pairs op enkele beurzen**, niet tientallen. En de ruwe diepte-laag
is de enige die echt geld kost — daarom een rollend venster.

## 6. Gatenbeleid

Het belangrijkste onderdeel. Drie regels, niet onderhandelbaar:

1. **Een gat wordt geregistreerd, nooit opgevuld.** Geen interpolatie, geen
   "waarschijnlijk continu". Een detector die niet weet dat er een gat was, liegt.
2. **Een detector moet zich kunnen onthouden.** Elke detectoruitslag krijgt een veld
   `dekking` (0–1) en geeft `onbetrouwbaar` terug als de dekking onder een drempel
   zakt. Dat is geen zwakte van het model maar de enige eerlijke uitkomst.
3. **Volgnummers zijn de waarheid, niet de klok.** Een gat detecteer je aan een sprong
   in het volgnummer, niet aan een stilte in de tijd. Stilte kan ook betekenen dat het
   gewoon rustig was.

## 7. Herverbinden

- Exponentiële backoff met jitter; nooit strak opnieuw proberen.
- Na herverbinden: orderboek **opnieuw volledig inlezen** (snapshot), niet doorwerken
  op een verouderde lokale kopie.
- Het gat tussen laatste volgnummer en nieuwe snapshot gaat het gatenlog in.
- Opnieuw abonneren is niet idempotent op elke venue — dubbel afschrijven is een reëel
  risico. Dedupliceer op `trade_id` of op (volgnummer, prijs, hoeveelheid, tijdstip).

## 8. Bewaarbeleid

| Laag | Bewaren | Reden |
|---|---|---|
| Trades | voor altijd | Klein, en de basis voor bijna elke detector |
| Ruwe diepte-diffs | 30–90 dagen rollend | Groot; alleen nodig voor heranalyse en D17 |
| Top-of-book per seconde | voor altijd | Klein, en genoeg voor de meeste diepte-detectoren |
| Gatenlog | voor altijd | Zonder dit is niets reproduceerbaar |
| Claim-kant | voor altijd | Eén regel per dag |

## 9. Wat je niet opslaat

- Geen persoonsgegevens, geen KYC, geen e-mailadressen.
- Geen API-sleutels in databestanden. Sleutels horen in een aparte, niet-versiebeheerde
  configuratie.
- Geen volledige orderhistorie als je alleen aggregaten nodig hebt.
- Geen afgeleide scores zonder de ruwe invoer ernaast: een score zonder onderliggende
  data is niet te controleren.

## 10. Voorwaarden en fatsoen

- Respecteer rate limits en de gebruiksvoorwaarden van elke bron. Publieke streams zijn
  publiek, maar niet onbeperkt.
- Geen HTML scrapen als er een API is: fragiel, en het kan tegen de voorwaarden zijn.
- Bij twijfel over herdistributie: de ruwe data niet publiceren, de methode wel.

## 11. Openstaande punten

- `BESLOTEN, met correctie` — **Eén dependency of geen?** Het oorspronkelijke advies was "één
  hoofddependency: cryptofeed". **Dat stuit op de licentie.** cryptofeed is
  **AGPL-3.0** (met een extra attributieclausule onder §7(b)), en deze repository is MIT.
  Een AGPL-bibliotheek in dezelfde distributie trekt het geheel in de praktijk naar AGPL, en
  §13 raakt ook netwerkgebruik. Drie uitwegen:
  1. **Zelf een minimale collector schrijven** voor twee venues, op `websockets`
     (BSD-3-Clause) of `aiohttp` (Apache-2.0) — beide permissief. Voor twee venues en vier
     streams is dat een paar honderd regels; het lastige deel (snapshots, deltas,
     volgnummers) is per venue gedocumenteerd.
  2. **De collector als apart component** met een eigen AGPL-licentie en een procesgrens
     (bestanden of IPC), zodat de MIT-bibliotheek hem niet importeert. Juridisch
     verdedigbaar, maar complexer en onvriendelijker voor gebruikers.
  3. **CCXT** is MIT, maar de websocket-laag (CCXT Pro) valt buiten die MIT-licentie.

  **Voorstel: optie 1.** D25 blijft dependency-vrij; de collector krijgt één permissieve
  dependency.
- `BESLOTEN` — **Eerste venues en pair:** Binance spot en Bybit spot, beide **BTCUSDT**.
  Eis blijft: ze moeten zowel een trades- als een diepte-stream leveren, anders kun je T1 en
  T2 nooit vergelijken. OKX volgt pas als de collector stabiel loopt; Kraken is aanvullend.
- `BESLOTEN, bevestigd` — **Agressor-kant:** per venue geverifieerd, zie §3.1. Nooit raden.
- `DEELS BEANTWOORD` — **Latentie en doorvoer van deze machine.** Protocol: één uur per venue
  meten en registreren: aantal berichten, aantal trades, aantal diepte-updates, sequence gaps,
  reconnects, verwerkingstijd, queue-achterstand, CPU en RAM. Acceptatie: geen onverklaarde
  gaps, geen verloren trades, geen oplopende achterstand, reconnect zonder datagat, geen
  geheugenlek. Pas daarna de architectuur definitief vastleggen.

  **Meting, 3 november 2026, één uur per venue (BTCUSDT spot), na elkaar gemeten zodat
  ze elkaars bandbreedte niet beïnvloeden:**

  | | Binance | Bybit |
  |---|---|---|
  | Duur | 3.601 s | 3.601 s |
  | Trades binnengehaald | **246.052** (±68/s) | **96.489** uit 27.979 berichten (±3,45 per bericht, max **115**) |
  | Diepte-updates | 35.980 | **139.727** |
  | Sequence gaps | **0** | **0** |
  | Reconnects | **0** | **0** |
  | Fouten | **0** | **0** |
  | Latentie p50 / p95 / max (ms) | 323 / 339 / 684 | 310 / 333 / 415 |
  | Parse-tijd p95 | 53 µs (trade), 529 µs (diepte) | 197 µs (trade), 117 µs (diepte) |
  | Queue-achterstand max | 285 | 23 |

  De doorvoer was niet vlak: tussen minuut 30 en 40 kwam er 50.769 trades in één
  periode van 600 s, bijna dubbel het gemiddelde. De queue liep daarbij op tot 285
  berichten, maar bleef daarna structureel op 0 staan. Alle 179 voortgangsregels per
  venue kwamen op tijd — er is geen moment geweest waarop de collector stilviel.

  **Wat deze meting niet bewijst.** "Geen verloren trades" is alleen hard te maken voor
  de diepte-stream, want daar controleert het volgnummer elke update: 139.727
  opeenvolgende Bybit-updates zonder één onderbreking. Voor trades hebben beide venues
  wel een trade-id, maar die controleren we nog niet op gaten. Dat is de eerstvolgende
  verbetering.

  **Geheugen: hier zat een fout in.** De eerste uitvoering eindigde op 20,7 MB, tegen
  1,2 MB na één minuut. Oorzaak was niet de verbinding maar de meting zelf: elke
  latentie werd als float in een lijst bewaard, en dat zijn 564.000 objecten van ±40
  byte. Op een run van 24 uur was dat richting 500 MB gegroeid. Opgelost met een
  reservoir van vaste grootte (`Sample` in `scripts/collector.py`), dat wél het echte
  maximum en het aantal metingen blijft onthouden.

  Na de fix, opnieuw gemeten over 5 minuten per venue:

  | | Berichten | Geheugen |
  |---|---|---|
  | Binance vóór de fix (60 min) | 282.032 | 20,65 MB |
  | Binance ná de fix (5 min) | 19.211 | **1,97 MB** |
  | Bybit vóór de fix (60 min) | 236.716 | 12,26 MB |
  | Bybit ná de fix (5 min) | 17.302 | **1,47 MB** |

  Het reservoir is bij Binance al volgelopen (16.221 trades > 10.000), dus dit is het
  plafond en niet een tussenstand: het geheugengebruik hangt vanaf dat punt niet meer
  van de duur af.
- `OPEN` — **Gebruiksvoorwaarden per venue.** Vier verschillende rechten die je apart moet
  controleren: (1) publieke toegang tot de marktdata, (2) opslag en archivering,
  (3) herdistributie van de verzamelde data, (4) publicatie van afgeleide analyses. Tot die
  controle: ruwe data alleen intern bewaren, niets herdistribueren, en per dataset de bron,
  de voorwaarden en de verzameldatum vastleggen.
