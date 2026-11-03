# 01 — Taxonomie van nepvolume

De technieken geordend, met per techniek: wat wordt gemanipuleerd, op welk tier je
het kunt meten, en welk voorbeeld we hebben.

## 1. Waarom een taxonomie vooraf

Detectoren werken alleen als je weet *wat* je zoekt. "Wash trading" is in het publieke
debat een paraplu geworden waar zes verschillende dingen onder hangen, en die vragen
verschillende data. Een detector die wash trading en spoofing door elkaar haalt, meet
niets.

Daarom eerst een indeling naar **wat er gemanipuleerd wordt**:

| Doel | Mechanisme | Waar zit het |
|---|---|---|
| **Volume** | trades die geen economische overdracht zijn | in de *prints* |
| **Orderboek / intentie** | orders die nooit bedoeld zijn om te vullen | in de *book events* |
| **Prijs** | prints op een dun boek die de laatste prijs zetten | in *prints + depth* |
| **Aandacht / ranking** | volume om bovenaan een lijst te staan | in *aggregator-data* |

Het onderscheid orderboek-versus-prints is essentieel: **spoofing verhoogt het
volume niet.** De orders worden geannuleerd voordat ze vullen. Wie spoofing met een
volumedetector zoekt, zoekt naar iets wat er per definitie niet is. Dit is de meest
gemaakte fout in zelfgebouwde detectoren.

### 1.1 Twee assen in plaats van één lijst

Eén lijst families is niet genoeg. Dezelfde transactie kan **echt** zijn en tóch het
gerapporteerde volume vertekenen: een beurs die met eigen kapitaal een klantorder vult,
doet zaken die werkelijk plaatsvinden, maar het is geen handel tussen twee onafhankelijke
klanten. Wie dat in één categorie propt, moet kiezen tussen twee fouten — echte
liquiditeit als manipulatie bestempelen, of kunstmatig volume als echt tellen.

Daarom classificeren we op twee onafhankelijke assen.

| As A — economische geldigheid | Betekenis |
|---|---|
| **Echte economische activiteit** | aantoonbare handels-, hedge-, arbitrage- of liquiditeitsfunctie |
| **Incentive-vertekende activiteit** | omvang of frequentie wordt aantoonbaar door een externe beloning beïnvloed |
| **Kunstmatige activiteit** | geen betekenisvolle onafhankelijke economische blootstelling |
| **Ongeclassificeerd** | de functie is met de beschikbare data niet vast te stellen |

| As B — herkomst van het volume | Betekenis |
|---|---|
| **Onafhankelijke klanten** | geen aantoonbare relatie tussen de partijen |
| **Gerelateerde partijen** | zelfde eigenaar, of aantoonbaar gecoördineerd |
| **Beursgebonden entiteit** | market maker of dochter die aan de beurs gelieerd is |
| **De beurs zelf** | eigen boek, eigen matching, eigen internalisatie |
| **Onbekend** | herkomst niet vast te stellen |

De assen zijn onafhankelijk. Een beursgebonden market maker is *echte economische
activiteit + beursgebonden entiteit*. Dezelfde beurs die tegen zichzelf handelt is
*kunstmatige activiteit + de beurs zelf*. Dat onderscheid kan één lijst niet maken.

**Belangrijke grens:** as B is op publieke trade-data meestal **niet** vast te stellen. Dat
is geen reden om de as te laten vallen — het is de reden om per detector te vermelden welke
as je meet, en met welke confidence.

## 2. De zeven families

### F1 — Self-trade / eigen order vullen
Eén entiteit is beide kanten van de transactie.

- **Mechanisme:** een account (of market maker met eigen account) plaatst een buy en
  een sell die tegen elkaar uitvoeren.
- **Manipuleert:** volume.
- **Tier:** T3 (ideaal), T1 (soms: identieke tegenprints), T0 (zwak signaal).
- **Kenmerk:** geen netto positieverandering, geen economisch motief.
- **Formele kern:** Cao et al. (2016) formaliseren dit als
  $\sum_k \text{OrderPair}_k = ("0", P_T \pm \delta_{Tp}, \pm\delta_v)$ — de
  gesigneerde trader-ID's en volumes vallen weg. Zie formules §1.2.
- **Moeilijkheid:** de tegenpartij is op publieke data anoniem. Op een CEX zie je
  alleen "buy" en "sell", niet wie.

### F2 — Matched orders tussen samenwerkende partijen
Twee of meer accounts, onder één controle of in onderling overleg, handelen tegen
elkaar. Juridisch de klassieke definitie (CESR, FCA, CME Rule 575).

- **Manipuleert:** volume.
- **Tier:** T3 (volledig), T1 (deels).
- **Kenmerk:** krappe tijdsintervallen, uitvoerbare prijzen, grotendeels gematchte
  volumes, en een **gesloten cyclus** over de deelnemers.
- **Formele kern:** Cao et al. vergelijkingen (3), (4), (5) plus Feature 2
  (gesloten transactiecyclus). Zie formules §1.3–§1.4.
- **Moeilijkheid:** één gematcht orderpaar is nog geen manipulatie. Pas de cyclus
  maakt het rond. Een detector die alleen paren telt, geeft enorme aantallen
  fout-positieven.

### F3 — Incentive-gedreven volume
Handel die zonder een externe beloning in deze vorm niet zou plaatsvinden. Geen collusie,
maar een drijfveer die niet het prijsrisico is.

- **Vormen:** handelscompetities met prijzen, fee-rebates die verlies dekken,
  market-making-programma's van de beurs zelf, airdrop-farming, "volume-for-hire"
  (verkocht volume).
- **Manipuleert:** volume, en via volume de ranking.
- **Tier:** T1 (gedragspatroon), T3 (bewijs van de incentive-relatie).
- **Kenmerk:** handel die doorgaat ongeacht prijsrichting, vaak in ronde bedragen, en die
  stopt zodra het programma eindigt. Dat laatste is een sterk natuurlijk experiment.
- **Waarom dit in de taxonomie hoort:** dit is de categorie die het verschil maakt tussen
  51% en 95%. Veel "nep" volume is niet strafbaar — het is nutteloos volume. Wie alleen
  juridische wash trading telt, mist het grootste deel.

**De aanwezigheid van een incentive maakt volume niet verdacht.** Een rebate of fee-korting
is een normaal economisch instrument. Het gaat om het gedrag dat de incentive veroorzaakt.

| Subcategorie | Kenmerk | As A |
|---|---|---|
| **F3-L** — legitiem | de incentive ondersteunt echte liquiditeitsvoorziening; de deelnemer draagt koers- en voorraadrisico | echte economische activiteit |
| **F3-D** — distortion | de incentive beïnvloedt frequentie of ordergedrag, maar er blijft economische blootstelling | incentive-vertekend |
| **F3-A** — artificial | volume wordt hoofdzakelijk gegenereerd om de beloning te incasseren, zonder betekenisvolle blootstelling | kunstmatig |

Vier criteria, in volgorde van bewijskracht:

1. **Inventory risk** — draagt de deelnemer werkelijk koers- of voorraadrisico?
2. **Economic exposure** — ontstaat er een netto positie, of wordt die binnen seconden
   geneutraliseerd?
3. **Counterparty independence** — staan er onafhankelijke partijen aan beide zijden?
4. **Incentive dependency** — zou de activiteit ook zonder de beloning plaatsvinden?

Criterium 4 is het scherpste en het lastigst: het vereist een vergelijking vóór, tijdens en
na het programma.

**Meten zonder kant-en-klare dataset.** Er bestaat geen publieke dataset met
incentive-programma's naast volumereeksen. Dat is op te lossen door het register zelf bij te
houden: venue, pair, programmatype, start- en einddatum, beloningsstructuur, voorwaarden,
bron-URL en de datum waarop de informatie openbaar werd. Daarmee wordt een event-study
mogelijk:

$$\text{Effect} = \frac{V_{\text{tijdens}}}{V_{\text{ervoor}}}, \qquad
\text{Decay} = \frac{V_{\text{erna}}}{V_{\text{tijdens}}}$$

**Valkuil:** zonder marktbrede controle meet je de markt, niet het programma. Deel daarom
door het volume van een vergelijkbare venue zonder programma, of door een marktbrede index.
Een daling na afloop bewijst bovendien niet dat het volume kunstmatig *was* — alleen dat het
incentive-gevoelig was.

### F4 — Orderboek-manipulatie (spoofing, layering, quote stuffing)
Orders die de indruk van intentie moeten wekken, maar nooit bedoeld zijn om te vullen.

- **Mechanisme:** grote orders plaatsen aan één kant, die opzij zetten zodra de prijs
  beweegt; of lagen orders op meerdere niveaus; of extreem veel orders plaatsen en
  direct annuleren.
- **Manipuleert:** *schijnbare* liquiditeit en prijs, **niet het volume**.
- **Tier:** T2 (diepte-diffs plus trade-stream, of order-events met order-ID's als de venue
  die levert).
- **Meetbaar via:** order-to-trade-ratio, cancel-ratio, levenstijd van orders,
  book-imbalance versus gerealiseerde prijsimpact.
- **Waarom apart:** een volumedetector ziet dit niet. In [02-detectoren.md](02-detectoren.md) staan
  deze detectoren daarom onder T2 en niet onder "wash trading".
- **Stand van zaken:** een kant-en-klare publieke cancel-feed bestaat niet, maar
  annuleringen zijn *afleidbaar* uit diepte-diffs in combinatie met de trade-stream. Dat
  levert een `depth_decrease` op, niet met zekerheid een geannuleerde order — zie
  [03-datalandschap.md](03-datalandschap.md) §6.2 en [07-datalaag.md](07-datalaag.md) §3.1.

### F5 — Prijsgerichte trucs met volume als gereedschap
- **Painting the tape:** prints op een dun boek om de laatste prijs te zetten.
- **Marking the close:** volume en prijs vlak voor een benchmark-venster.
- **Pump and dump:** wash trades als opwarmer, daarna dumpen in de vraag van anderen.
- **Tier:** T0/T1 voor het patroon, T2 voor de impact.
- **Kenmerk:** volume piekt rond een tijdstip dat erudit toe doet (fixing, expiratie,
  listing), niet rond een informatiemoment.
- **Relevant voorbeeld in de workspace:** de Coinbase Derivatives-filing voor HYPE
  futures beschrijft expliciet welke waarborgen hiertegen zijn ingebouwd —
  fair-value-limits, en een benchmark die uit 40 blokken van 3 minuten een
  volume-gewogen mediaan neemt. Dat is de tegenmaatregel; nuttig als referentie voor
  wat een *robuuste* benchmark kenmerkt.

### F6 — Ranking- en aandachtsfarming
Volume om zichtbaarheid, niet om geld.

- **Vormen:** volume om hoog te staan bij aggregators, om listed te worden, om in een
  "trending"-lijst te komen; op NFT-marktplaatsen: self-trades om de floor price
  op te blazen; op prediction markets: volume om in aanmerking te komen voor een
  airdrop of leaderboard-positie.
- **Tier:** T1/T3, plus aggregator-metadata.
- **Bewijs dat dit bestaat:**
  - Bitwise (2019) beschrijft expliciet dat beurzen volume opvoeren om in
    CoinMarketCap-ranglijsten te stijgen.
  - Forbes/Javier Paz (2022): het ondeugdelijkste volume zat bij kleine beurzen, waar
    "listing rank en aggregator-zichtbaarheid de voornaamste bron van nieuwe
    gebruikers zijn".
  - Columbia-onderzoek (6 nov. 2025) naar Polymarket: ~25% van het volume over drie jaar
    als wash trading aangemerkt, met veel geflagde wallets die **geen winst maakten** —
    consistent met het boeren van een ranking of airdrop, niet met handelswinst. (De in
    eerdere versies genoemde uitsplitsing sport ~45% / verkiezingen ~17% is **niet
    bevestigd**; zie [04-bronnen.md](04-bronnen.md) §1 en §4.)
- **Waarom dit de moeilijkste familie is:** er is geen tegenpartij-benadeling. Het
  "slachtoffer" is de ranking, en dus de gebruiker die de ranking leest.

### F7 — Door de beurs gegenereerd volume (Exchange-Originated Volume, EOV)
Volume waarvan de oorsprong ligt bij de beurs zelf, of bij een entiteit die onder haar
eigendom, controle of operationele verantwoordelijkheid valt.

- **Waarom een eigen familie:** dit is geen klantgedrag. Het valt buiten F1–F6, maar het
  vertekent het gerapporteerde volume wél — en het is de categorie die het vaakst over het
  hoofd wordt gezien.
- **As A:** kan echt, vertekend of kunstmatig zijn. **As B:** beursgebonden entiteit of de
  beurs zelf.
- **Tier:** T3 (vrijwel altijd), T2 (deels: eigen quotes zijn in het boek zichtbaar).

| Subcategorie | Wat het is |
|---|---|
| **F7-M** | eigen market-making door de beurs |
| **F7-P** | proprietary trading door de beurs |
| **F7-I** | interne matching of internalisatie van klantorders |
| **F7-A** | kunstmatig door de beurs gegenereerd volume |

Drie gevallen die op elkaar lijken maar niet hetzelfde zijn:

- de beurs vult een klantorder uit eigen voorraad → **echte** transactie, maar geen
  klant-tegen-klant;
- de beurs quote continu beide kanten → kan **legitieme** liquiditeit zijn;
- de beurs handelt tegen zichzelf om het gerapporteerde volume op te hogen → **kunstmatig**.

**Moeilijkheid:** publieke trade-data zegt niet wie de economische eigenaar van beide zijden
is. Zonder kennis van beursgerelateerde accounts en wallets is F7 niet te meten — alleen te
vermoeden. Dat is een harde grens, geen implementatiedetail.

**Waarom dit nummer F7 is en niet F4:** F4 is in deze taxonomie al orderboek-manipulatie.
Wie familienummers hergebruikt, breekt elke verwijzing in
[02-detectoren.md](02-detectoren.md).

## 3. Wat níet in de taxonomie hoort

| Verschijnsel | Waarom niet |
|---|---|
| Normale market making | Twee kanten kwoteren is legitiem; pas bij afspraken of zelfhandel wordt het F1/F2 |
| Hoge frequentie zonder patroon | Snelheid is geen misbruik |
| Groot volume bij nieuws | Dat is precies wat echt volume doet |
| Liquiditeitsmijnen / yield farming | Economisch gemotiveerd, geen volume-manipulatie (wel verwant aan F3 in de zin dat het om de beloning gaat) |

## 4. Koppeling naar de detectoren

| Familie | Primaire detectoren (zie [02-detectoren.md](02-detectoren.md)) |
|---|---|
| F1 self-trade | D11, D19, D20, D24 |
| F2 matched orders | D11, D20, D23 |
| F3 incentive | D02, D03, D05, D08, D21 |
| F4 orderboek | D13, D14, D17, D18 |
| F5 prijsgericht | D06, D15, D16, D18 |
| F6 ranking/aandacht | D02, D04, D22 |
| F7 beursvolume | D13, D22, D26 |

## 5. De taxonomy-vragen van fase 0 — besloten

| Vraag | Besluit |
|---|---|
| Is "non-economic volume" een bruikbare analyseterm? | **Niet als classificatie.** Wel als overkoepelende aanduiding in het publieke debat. Als classificatie vervangen door as A: echt / incentive-vertekend / kunstmatig / ongeclassificeerd. De term blijft nodig om uit te leggen waarom schattingen van 51% tot 95% uiteenlopen — zie [00-scope.md](00-scope.md) §1 |
| Waar ligt de grens tussen F3 en legitiem zakendoen? | Niet bij het beloningsmodel, maar bij het gedrag: F3-L, F3-D of F3-A, getoetst met de vier criteria hierboven |
| Hoe classificeren we volume dat de beurs zelf genereert? | Eigen familie **F7** (EOV), met F7-M / F7-P / F7-I / F7-A |

**Wat hiermee niet is opgelost:** de operationalisering. As A is meetbaar vanaf T1; as B
vrijwel nooit op publieke data. Elke detector moet daarom zeggen welke as hij meet.
