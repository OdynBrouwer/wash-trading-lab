# Wash Trading Lab

Kennisbasis voor een opensource-project dat nepvolume en wash trading in
cryptomarkten wil detecteren — en dat eerlijk aangeeft wat het **niet** kan.

**Status:** de kennisbasis staat (9 documenten), D25 is geïmplementeerd en gedraaid op
een 100 MB-monster van de Victor & Weintraud-data, de datalaag is ontworpen, en D01–D06
zijn geïmplementeerd en gescoord op zowel een synthetische reeks als **echte
Binance-bars** (BTCUSDT, 43.200 minuutbars) — inclusief de detector waarvan we hardop
zeggen dat hij niet werkt. Nog geen live collector.

---

## Het probleem

Handelsvolume is het makkelijkst te vervalsen cijfer in een financiële markt, omdat
het geprint kan worden zonder dat er liquiditeit tegenover staat. Diepte kun je niet
faken zonder kapitaal dat echt in het boek staat.

Gepubliceerde schattingen van het aandeel nep- of niet-economisch volume lopen van
**51% tot 95%**, afhankelijk van steekproef, periode en definitie. Die spreiding is
geen meetfout maar een definitieprobleem — zie [`docs/01-taxonomie.md`](docs/01-taxonomie.md).

## Wat dit project is

1. Een **geordende taxonomie** van de technieken waarmee volume wordt vervalst.
2. Een **catalogus van detectoren**, elk met: welke data nodig, welke formule,
   welke valkuil, en of hij ooit gevalideerd is.
3. Een **eerlijk beeld van het datalandschap**: wat is gratis, wat is te koop, wat
   ontbreekt structureel.
4. Een **geannoteerde bibliografie** waarin per bron staat hoe betrouwbaar hij is.
5. Een **juridisch en ethisch kader** dat voorkomt dat het project als
   beschuldiging wordt gelezen.

## Wat dit project niet is

- Geen bewijs dat een specifieke beurs of persoon zich misdraagt.
- Geen vervanging voor accountdata of toezicht. Geen enkele detector op publieke
  data kan eigenaarsschap of opzet vaststellen.
- Geen koop- of verkoopadvies.
- Geen product met een verkooppraatje. Waar een bron een commercieel belang heeft,
  staat dat erbij.

---

## Kernontwerp: tier-model

De formules zijn het makkelijke deel. **De data is het probleem.** Een detector heeft
daarom een tier-label dat aangeeft welke data je nodig hebt:

| Tier | Data | Wat haalbaar is |
|---|---|---|
| **T0** | OHLCV | Symptomen: volume zonder prijsreactie, nul-volume, afwijkend sessieprofiel |
| **T1** | trades (tick) | Vorm van de trade-verdeling: roundness, Benford, staart, gepaarde prints |
| **T2** | orderboek | Volume versus diepte, spread, slippage, resilience, cancel-ratio |
| **T3** | accounts / on-chain | Eigendom: wash score, gesloten cycli, round-trips, tegenpartij-concentratie |

Een detector zonder tier-label is een detector waarvan je niet weet of je hem kunt
draaien. Daarom heeft elke detector in [`docs/02-detectoren.md`](docs/02-detectoren.md)
er één.

**Belangrijke consequentie:** met alleen OHLCV (T0) meet je het *symptoom*. Je kunt
niet verder komen dan "dit volume gedraagt zich niet zoals echt volume". Dat is nuttig
en verdedigbaar, maar het is geen identificatie van een dader.

---

## Mappenstructuur

```
.
├── README.md                     dit bestand
├── .gitignore
├── docs/
│   ├── 00-scope.md               afbakening en succescriteria
│   ├── 01-taxonomie.md           de technieken, geordend
│   ├── 02-detectoren.md          catalogus: 26 detectoren met tier
│   ├── 03-datalandschap.md       welke data bestaat, wat ontbreekt
│   ├── 04-bronnen.md             geannoteerde bibliografie
│   ├── 05-roadmap.md             fasen en open vragen
│   ├── 06-juridisch-en-ethiek.md
│   ├── 07-datalaag.md            streams, opslagschema, gatenbeleid
│   ├── 08-benchmark.md           welke T0-detector welke injectie vangt
│   ├── washtrading-formules.md   de canonieke formuleverzameling
│   └── bronnen/                  index per bron; de tekstconversies blijven lokaal
├── scripts/
│   ├── injector.py               nepvolume injecteren met bekende labels
│   ├── detectors_t0.py           D01–D06
│   ├── run_benchmark.py          scoort de detectoren per injectie
│   ├── collector.py              publieke CEX-websockets meten (Binance, Bybit)
│   ├── probe_mendeley_features.py  toetst Falk et al. features op echte labels
│   ├── check_internal_links.py   controleert alle relatieve links
│   ├── d25_scc_wash.py           eerste werkende detector (stdlib-only)
│   └── epub2md.py                EPUB -> Markdown
├── tests/                        regressietests (stdlib unittest)
├── data/                         werkmonsters, git-ignored
└── sources/                      PDF's en EPUB's, git-ignored
```

De formules staan in [`docs/washtrading-formules.md`](docs/washtrading-formules.md).
Dat is de canonieke formuleverzameling; [`docs/02-detectoren.md`](docs/02-detectoren.md)
verwijst ernaar in plaats van hem te dupliceren.

De originele PDF's en EPUB's staan in `sources/` en worden niet gecommit. Dat geldt ook
voor de Markdown-conversies daarvan: die staan lokaal in `docs/bronnen/` maar **niet**
in deze repository, omdat de rechten bij de uitgevers liggen. Wat er wél staat is de
index [`docs/bronnen/README.md`](docs/bronnen/README.md): per bron een oordeel over de
betrouwbaarheid. Dat oordeel is eigen werk, en dat is het deel dat de volgende lezer
nodig heeft.

## Controle

```bash
python scripts/check_internal_links.py      # alle relatieve links
python -m unittest discover -s tests -v     # regressietests
python scripts/run_benchmark.py             # T0-benchmark op synthetische data
python scripts/run_benchmark.py --csv data/BTCUSDT-1m-2026-09.csv   # op echte bars
python scripts/collector.py --minutes 2     # live websockets, Binance + Bybit
```

De linkchecker loopt alle Markdown-bestanden na en lost elke relatieve link op vanuit de
map van het bestand zelf. Exitcode 1 bij een gebroken link.

---

## Bronvermelding en eerlijkheid

Elke claim in deze documentatie hoort herleidbaar te zijn. Daarom:

- getallen altijd met bron, steekproef en periode;
- onderscheid tussen **letterlijk uit een paper** en **eigen reconstructie**;
- commerciële belangen benoemd;
- wat niet gelezen of niet geverifieerd is, staat als `OPEN`.

Zie [`docs/04-bronnen.md`](docs/04-bronnen.md) voor de volledige verantwoording.

## Licentie

- **Code** (`scripts/`): [MIT](LICENSE).
- **Documentatie** (README en `docs/`): [CC BY-SA 4.0](LICENSE-docs).

Kort: je mag alles gebruiken en aanpassen, ook commercieel, mits je het project noemt
en een bewerking van de documentatie onder dezelfde licentie deelt.

De conversies van boeken en papers van derden vallen onder geen van beide en staan om
die reden niet in deze repository — zie [`LICENSE-docs`](LICENSE-docs).

## Bijdragen

Nog niet opengesteld. Eerst moet de taxonomie en de detectorenspecificatie staan,
anders krijgt het project bijdragen die niet aansluiten.
