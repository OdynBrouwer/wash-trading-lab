# 05 — Roadmap en beslissingen

## 1. Fasen

### Fase 0 — Kennisbasis *(huidige fase)*
- [x] Formules inventariseren ([`washtrading-formules.md`](washtrading-formules.md))
- [x] Alle beschikbare bronnen lezen en beoordelen
- [x] Taxonomie opstellen
- [x] Detectorencatalogus met tier-labels
- [x] Datalandschap in kaart brengen
- [x] Juridisch en ethisch kader
- [ ] **Open**: de vier bronnen uit [04-bronnen.md](04-bronnen.md) §3 ophalen

**Definition of done:** een buitenstaander leest de docs en weet (a) wat nepvolume is,
(b) wat je nodig hebt om het te meten, en (c) wat je niet kunt weten.

### Fase 1 — Ontwerp vastleggen
- [x] Datalaag ontworpen: streams, opslagschema, volumeschatting, gatenbeleid ([07-datalaag.md](07-datalaag.md))
- [ ] Keuze van de eerste venue-set en het eerste pair (moet data leveren op T0 **en**
      T1, anders kun je nooit vergelijken)
- [ ] Definitie van de output-vorm: één score of een score per detector met bijdragen
- [ ] Keuze licentie (docs: CC BY-SA 4.0; code: MIT of Apache-2.0)
- [ ] Repositorynaam definitief maken

**Definition of done:** de API-vorm van een detector staat vast, en er is één detector
volledig gespecificeerd tot op functiesignatuur.

### Fase 2 — Synthetische benchmark + T0
- [ ] Injector bouwen (zie [03-datalandschap.md](03-datalandschap.md) §3) met alle variatieparameters
- [ ] D01–D06 implementeren
- [ ] Alle T0-detectoren scoren op de benchmark, inclusief de gevallen waarin ze falen
- [ ] Publiceren: welke detector welke injectie wel/niet vangt

**Definition of done:** een resultaattabel met foutmarges, en minstens één detector
waarvan we hardop zeggen dat hij niet werkt.

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

## 3. Openstaande vragen voor de eigenaar

Deze zijn inhoudelijk en kan ik niet alleen beslissen:

1. **Doel van het project.** Wordt dit een bibliotheek die anderen in hun code
   importeren, een losse analysetool, of een publiek dashboard? Dat bepaalt de
   API-vorm in Fase 1 volledig.
2. **Doelgroep.** Handelaar die zijn venue wil beoordelen, onderzoeker die reproduceerbaar
   werk wil, of journalist die een claim wil checken? Elk vraagt andere output.
3. **Publicatiedrempel.** Durven we namen van venues te noemen naast gemeten waarden?
   Zie [06-juridisch-en-ethiek.md](06-juridisch-en-ethiek.md) §3 — mijn voorstel is nee, of alleen met
   tegenhanger en periode erbij.
4. **Onderhoud.** Wie onderhoudt dit over twee jaar? Als het antwoord "niemand" is,
   moet het ontwerp daarop aangepast worden (weinig dependencies, geen live services).
5. **Relatie met bestaand werk.** Er zijn bestaande opensource-initiatieven op dit
   gebied. Voordat we iets bouwen: eerst kijken wat er al is, anders bouwen we een
   slechtere versie van iets bestaands. `OPEN` — niet onderzocht.

## 4. Risico's

| Risico | Gevolg | Mitigatie |
|---|---|---|
| Geen ground truth | Scores zijn schijnprecisie | Synthetische benchmark + expliciete waarschuwing |
| Data-afhankelijkheid van één commerciële leverancier | Project sterft mee | T0 altijd gratis houden |
| Verkeerd gelezen als beschuldiging | Juridisch en reputatierisico | [06-juridisch-en-ethiek.md](06-juridisch-en-ethiek.md) als harde regel |
| Zwakke detectoren (D08, D11) worden als hoofdproduct gepresenteerd | Geloofwaardigheid weg | Prioritering in [02-detectoren.md](02-detectoren.md) §Prioritering |
| Scope creep naar DEX + NFT + prediction markets | Niets af | Fase 0 taxonomie is breed, uitvoering smal |
