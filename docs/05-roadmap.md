# 05 — Roadmap en beslissingen

## 1. Fasen

### Fase 0 — Kennisbasis *(huidige fase)*
- [x] Formules inventariseren ([`washtrading-formules.md`](washtrading-formules.md))
- [x] Alle beschikbare bronnen lezen en beoordelen
- [x] Taxonomie opstellen
- [x] Detectorencatalogus met tier-labels
- [x] Datalandschap in kaart brengen
- [x] Juridisch en ethisch kader
- [x] Taxonomy-vragen besloten: twee assen (geldigheid × herkomst) en de nieuwe familie F7
- [x] Bestaande opensource-initiatieven geïnventariseerd (cryptofeed, CCXT, Hummingbot) —
      **let op de licenties**: cryptofeed is AGPL-3.0, CCXT MIT (websocket-laag apart),
      Hummingbot Apache-2.0
- [ ] **Open**: de vier bronnen uit [04-bronnen.md](04-bronnen.md) §3 ophalen (alleen punt 3
      staat nog open: een gelabelde CEX-spotdataset bestaat niet publiek)

**Definition of done:** een buitenstaander leest de docs en weet (a) wat nepvolume is,
(b) wat je nodig hebt om het te meten, en (c) wat je niet kunt weten.

### Fase 1 — Ontwerp vastleggen
- [x] Datalaag ontworpen: streams, opslagschema, volumeschatting, gatenbeleid ([07-datalaag.md](07-datalaag.md))
- [x] Eerste venue-set en pair: **Binance + Bybit, BTCUSDT spot** (beide leveren trades én
      diepte, dus T0/T1/T2 zijn vergelijkbaar). OKX volgt na een stabiele collector
- [x] Definitie van de output-vorm: elke detector levert een waarde **plus** de as die hij
      meet en een confidence; D24 combineert pas als D01–D23 gescoord zijn
- [x] Keuze licentie: MIT voor code, CC BY-SA 4.0 voor de documentatie
- [x] Repositorynaam: `wash-trading-lab`
- [ ] Vorm van de API vastleggen: functiesignatuur van één detector, tot op het niveau van
      input- en outputtypes

**Definition of done:** de API-vorm van een detector staat vast, en er is één detector
volledig gespecificeerd tot op functiesignatuur.

### Fase 2 — Synthetische benchmark + T0
- [x] Injector bouwen (`scripts/injector.py`) met acht scenario's en vaste seed
- [x] D01–D06 implementeren (`scripts/detectors_t0.py`)
- [x] Alle T0-detectoren scoren op de benchmark, inclusief de gevallen waarin ze falen
      → [08-benchmark.md](08-benchmark.md)
- [x] Publiceren: welke detector welke injectie wel/niet vangt
- [x] Benchmark herhalen op **echte** BTCUSDT-bars via `load_binance_klines()`
      → september 2026, 43.200 minuutbars; D03 en D06 veranderen materieel
- [x] Seed-gevoeligheid meten (seed 1–5) — D06 varieert 0,72–0,82, de rest is stabiel
- [x] T0-features toetsen op **echte** wash-labels (Mt. Gox, Falk et al.) — alles op 0,50
- [ ] D02-drempel expliciet afwegen en vastleggen (recall 0,16 synthetisch / 0,43 echt)
- [ ] D03 valideren op meer maanden en pairs (FPR 0,10–0,21 op echte data)

**Definition of done:** een resultaattabel met foutmarges, en minstens één detector
waarvan we hardop zeggen dat hij niet werkt. ✅ Dat is D01: die vangt legitiem hoog
volume vrijwel even goed als nepvolume, ongeacht seed of reeks.

**Belangrijkste uitkomst achteraf:** de toets op échte labels (§8 van
[08-benchmark.md](08-benchmark.md)) laat zien dat alle features die je uit publieke
bars kunt halen op 0,50 scoren. De benchmark hierboven meet dus vooral hoe goed onze
detectoren *onze eigen injectie* herkennen. T0 blijft een triagefilter, geen bewijs.

### Fase 3 — T1 (tick-data)
- [ ] Trades opslaan met agressor-kant
- [ ] D07–D12 implementeren
- [ ] Zelfde benchmarkscore
- [ ] Fout-positievenanalyse op D11 (gepaarde prints), de gevaarlijkste detector

**Definition of done:** we kunnen kwantitatief zeggen welke T1-detectoren iets
toevoegen bovenop T0.

### Fase 4 — T2 en T3
- [x] **D25 geïmplementeerd en gedraaid** op een slice van de Victor & Weintraud-data
      (`scripts/d25_scc_wash.py`, 342.305 trades). Zie de statusregel in [02-detectoren.md](02-detectoren.md)
- [x] Databron gedocumenteerd (`data/README.md`): Zenodo `4540223`, CC-BY-4.0, 3.004 MB totaal
- [ ] Volledige EtherDelta- én IDEX-dataset draaien (3 GB; bewust nog niet gedownload)
- [ ] D13–D18 (orderboek) en D19–D22 (accounts/on-chain)
- [ ] D24 samenstellen, gewichten kalibreren

**Definition of done:** een end-to-end run op minimaal één markt per tier.

### Fase 5 — Publicatie
- [ ] README met eerlijke "wat dit niet kan"-sectie
- [ ] Handleiding voor gebruikers met alleen gratis T0-data
- [ ] Licentie, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- [ ] Openbaar maken

## 2. Beslissingslog

Omdat de projecteigenaar niet aanwezig was tijdens het opzetten, zijn deze keuzes
autonoom genomen. Ze staan hier zodat ze herzien kunnen worden.

| # | Beslissing | Reden | Herzienbaar? |
|---|---|---|---|
| B1 | Eerste scope = **CEX spot** | Meeste bronnen, meeste praktische relevantie, deels publieke data | Ja, kost alleen een extra taxonomiesectie |
| B2 | Eerste vorm = **alleen documentatie** | Code zonder vastgelegde definities wordt weggegooid werk | Ja, direct |
| B3 | **Tier-model** als hoofdstructuur (T0–T3) in plaats van een lijst methoden | Maakt zichtbaar wat een gebruiker met zijn eigen data kan | Nee, dit is dragend |
| B4 | Formules blijven in `../washtrading-formules.md` | Verplaatsen vereist overleg en breekt verwijzingen | Ja |
| B5 | Mapnaam `wash-trading-lab/` | Beschrijvend, neutraal, "lab" past bij onderzoeksfase | **Achterhaald**: de projectmap is opgeheven, de repo-root is nu de projectmap zelf |
| B6 | `data/` komt in `.gitignore` | Grootte en herdistributierechten | Nee |
| B7 | Geen enkele detector krijgt een "bewezen"-status zonder benchmarkscore | Voorkomt schijnprecisie | Nee |
| B8 | Synthetische ground truth in plaats van geen validatie | Enige haalbare middenweg, mits de beperking benoemd wordt | Ja, met tegenargument |
| B9 | Classificatie op **twee assen** (economische geldigheid × herkomst) in plaats van één lijst | Eén lijst kan echte liquiditeit en kunstmatig volume niet scheiden | Nee, dit is dragend |
| B10 | Nieuwe familie **F7** (Exchange-Originated Volume); F4 blijft orderboek-manipulatie | Hergebruik van F4 breekt elke verwijzing in `02-detectoren.md` | Nee |
| B11 | **`VI`** als enige naam voor volume-intensiteit | `VR` is al volume/range in Formules §4.2; twee betekenissen voor één symbool is een bug | Nee |
| B12 | Eerste venues: **Binance + Bybit, BTCUSDT spot** | Beide leveren trades én diepte, dus T1 en T2 zijn vergelijkbaar; BTCUSDT heeft een diep boek en veel historie | Ja |
| B13 | **Eén permissieve dependency** voor de collector (`websockets` BSD-3 of `aiohttp` Apache-2.0), niet cryptofeed | cryptofeed is **AGPL-3.0**; dat botst met de MIT-licentie van deze repo. Technisch is het een prima bibliotheek, juridisch niet combineerbaar | Ja, als de repo ooit AGPL wordt |
| B14 | "Non-economic volume" blijft **literatuurterm**, verdwijnt als **classificatie** | Als categorie niet falsifieerbaar: alles wat je niet begrijpt belandt erin | Ja |

## 3. Beslissingen van de eigenaar

Deze vragen kan de documentatie niet zelf beantwoorden. Ze zijn nu besloten, en ze staan hier
zodat ze herzien kunnen worden.

| # | Vraag | Besluit |
|---|---|---|
| 1 | Doel van het project | **Python-bibliotheek met een analysetool erbovenop.** Geen publiek dashboard in deze fase: dat schept druk om venues te rangschikken voordat de detectoren gevalideerd zijn |
| 2 | Doelgroep | **Onderzoekers eerst** (reproduceerbaarheid, ruwe meetwaarden), daarna handelaren, daarna journalisten |
| 3 | Publicatiedrempel | **Venue-namen mogen**, maar alleen met meetperiode, pair, marktsegment, detectorversie, datakwaliteit en confidence erbij. Nooit "pleegt wash trading"; wel "verhoogde indicatoren voor kunstmatig volume". Zie [06-juridisch-en-ethiek.md](06-juridisch-en-ethiek.md) §3 |
| 4 | Onderhoud | **Minimale afhankelijkheden.** Detectoren dependency-vrij, collector optioneel, geen verplichte clouddienst, en de engine moet ook op CSV/Parquet draaien zonder netwerkverbinding |
| 5 | Relatie met bestaand werk | **Onderzocht**: cryptofeed, CCXT en Hummingbot dekken de collectorkant. **Licentie is hier de beperkende factor**, niet de techniek: cryptofeed is AGPL-3.0 en dat botst met MIT. Conclusie: geen eigen WebSocket-*framework*, maar ook geen AGPL-dependency — zie [07-datalaag.md](07-datalaag.md) §11 |

**Wat dit betekent voor de architectuur:** de collector verzamelt feiten, de detectie-engine
interpreteert ze, en de classificatie-engine trekt pas daarna conclusies. De collector mag
nooit bepalen of volume verdacht is.

## 4. Risico's

| Risico | Gevolg | Mitigatie |
|---|---|---|
| Geen ground truth | Scores zijn schijnprecisie | Synthetische benchmark + expliciete waarschuwing |
| Data-afhankelijkheid van één commerciële leverancier | Project sterft mee | T0 altijd gratis houden |
| Verkeerd gelezen als beschuldiging | Juridisch en reputatierisico | [06-juridisch-en-ethiek.md](06-juridisch-en-ethiek.md) als harde regel |
| Zwakke detectoren (D08, D11) worden als hoofdproduct gepresenteerd | Geloofwaardigheid weg | Prioritering in [02-detectoren.md](02-detectoren.md) §Prioritering |
| Scope creep naar DEX + NFT + prediction markets | Niets af | Fase 0 taxonomie is breed, uitvoering smal |
