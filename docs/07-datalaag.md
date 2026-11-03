# 07 — Datalaag: van stream naar archief

Hoe live data binnenkomt, hoe je hem opslaat, en vooral: hoe je eerlijk blijft over
de gaten die erin zitten.

Dit document beschrijft het ontwerp. Er is nog **geen collectorcode**.

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
| **Diepte-diffs** | prijsniveau, nieuwe hoeveelheid, **volgnummer** | Voor D13–D17; het volgnummer is onmisbaar voor het gatenbeleid |

`OPEN` — De agressor-kant is niet op elke venue aanwezig. Dat moet **per venue
geverifieerd** worden voordat je hem in het schema opneemt; een leeg veld is eerlijker
dan een geraden waarde.

`OPEN` — De exacte streamnamen en endpoints verschillen per beurs en veranderen.
Niet overnemen uit dit document; per venue controleren in de eigen documentatie.
De grote beurzen bieden dit doorgaans gratis aan met een publieke sleutel of helemaal
zonder.

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

- `OPEN` — **Eén dependency of geen?** Een WebSocket-client zit niet in de
  standaardbibliotheek. D25 is dependency-vrij; een collector waarschijnlijk niet.
  Keuze: één kleine dependency accepteren, of WebSocket zelf implementeren (kan, maar
  levert niets op).
- `OPEN` — Welke venues en pairs als eerste? Eis: ze moeten **zowel** een trades- als
  een diepte-stream leveren, anders kun je T1 en T2 nooit vergelijken.
- `OPEN` — Is de agressor-kant per gekozen venue beschikbaar?
- `OPEN` — Latentie en doorvoer van deze machine zijn onbekend. Meten vóór ontwerpen:
  één uur één stream meelopen en kijken of er niets wegvalt.
- `OPEN` — Clausule in de gebruiksvoorwaarden over het bewaren van data.
