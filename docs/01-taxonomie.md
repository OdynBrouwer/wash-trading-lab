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

## 2. De zes families

### F1 — Self-trade / eigen order vullen
Eén entiteit is beide kanten van de transactie.

- **Mechanisme:** een account (of market maker met eigen account) plaatst een buy en
  een sell die tegen elkaar uitvoeren.
- **Manipuleert:** volume.
- **Tier:** T3 (ideaal), T1 (soms: identieke tegenprints), T0 (zwak signaal).
- **Kenmerk:** geen netto positieverandering, geen economisch motief.
- **Formele kern:** Cao et al. (2015) formaliseren dit als
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

### F3 — Non-economic volume (incentive-gedreven)
Geen collusie, maar handel die alleen plaatsvindt omdat iets anders dan het
prijsrisico de drijfveer is.

- **Vormen:** handelscompetities met prijzen, fee-rebates die verlies dekken,
  market-making-programma's van de beurs zelf, airdrop-farming, "volume-for-hire"
  (verkochte volume).
- **Manipuleert:** volume, en via volume de ranking.
- **Tier:** T1 (patroon), T3 (bewijs).
- **Kenmerk:** handel die doorgaat ongeacht prijsrichting, vaak in ronde bedragen, en
  die stopt zodra het incentive-programma eindigt. Dat laatste is een sterk
  natuurlijk experiment.
- **Waarom dit in de taxonomie hoort:** dit is de categorie die het verschil maakt
  tussen 51% en 95%. Veel "nep" volume is niet strafbaar — het is nutteloos volume.
  Wie alleen juridische wash trading telt, mist het grootste deel.
- **OPEN:** er is geen publieke dataset met incentive-programma's naast volumereeksen.
  Zonder die data is F3 alleen achteraf vast te stellen (volume stort in na einde
  programma), niet vooraf.

### F4 — Orderboek-manipulatie (spoofing, layering, quote stuffing)
Orders die de indruk van intentie moeten wekken, maar nooit bedoeld zijn om te vullen.

- **Mechanisme:** grote orders plaatsen aan één kant, die opzij zetten zodra de prijs
  beweegt; of lagen orders op meerdere niveaus; of extreem veel orders plaatsen en
  direct annuleren.
- **Manipuleert:** *schijnbare* liquiditeit en prijs, **niet het volume**.
- **Tier:** T2 (orderboek-events, inclusief cancels).
- **Meetbaar via:** order-to-trade-ratio, cancel-ratio, levenstijd van orders,
  book-imbalance versus gerealiseerde prijsimpact.
- **Waarom apart:** een volumedetector ziet dit niet. In [02-detectoren.md](02-detectoren.md) staan
  deze detectoren daarom onder T2 en niet onder "wash trading".
- **OPEN:** publieke orderboek-events met cancels zijn zeldzaam; de meeste API's
  leveren alleen snapshots.

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
  - Columbia-onderzoek (nov. 2025) naar Polymarket: ~25% van het volume over drie jaar
    als wash trading aangemerkt, met veel geflagde wallets die **geen winst maakten** —
    consistent met het boeren van een ranking of airdrop, niet met handelswinst.
- **Waarom dit de moeilijkste familie is:** er is geen tegenpartij-benadeling. Het
  "slachtoffer" is de ranking, en dus de gebruiker die de ranking leest.

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
| F3 non-economic | D02, D03, D05, D08, D21 |
| F4 orderboek | D13, D14, D17, D18 |
| F5 prijsgericht | D06, D15, D16, D18 |
| F6 ranking/aandacht | D02, D04, D22 |

## 5. Openstaande taxonomy-vragen

- `OPEN` — Is "non-economic volume" een bruikbare analyseterm of alleen een restpost?
  De literatuur gebruikt hem als containerbegrip; dat maakt hem lastig falsifieerbaar.
- `OPEN` — Waar ligt de grens tussen F3 (incentive) en legitiem zakendoen? Een
  rebate-programma is niet per definitie misbruik.
- `OPEN` — Hoe classificeer je volume dat door de *beurs zelf* wordt gegenereerd
  (eigen market-making)? Dat is geen klantgedrag en valt buiten alle bovenstaande
  families, maar het vertekent het gerapporteerde volume wel.
