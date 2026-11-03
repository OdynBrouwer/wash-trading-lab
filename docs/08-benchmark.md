# 08 — Benchmark: welke T0-detector vangt welke injectie

Resultaten van `scripts/run_benchmark.py`. De **basisreeks** is 60 dagen synthetische
15-minutenbars (seed 7); §4 herhaalt de hele benchmark op **echte** Binance-bars en §5
toetst de stabiliteit over vijf seeds. Herhaalbaar met:

```bash
python scripts/run_benchmark.py --days 60 --seed 7
python scripts/run_benchmark.py --csv "data/BTCUSDT-1m-2026-09.csv"
python -m unittest discover -s tests -v
```

De echte reeks haal je zo op (2 MB zip → 6,7 MB CSV, 43.200 bars, headerloos, µs-tijden):

```bash
curl -O https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1m/BTCUSDT-1m-2026-09.zip
# uitpakken naar data/BTCUSDT-1m-2026-09.csv
```

## 1. Wat hier gemeten wordt

De injector (`scripts/injector.py`) neemt een schone OHLCV-reeks en legt er een
ingreep op met bekende omvang. Per bar is er daarna een label. De detectoren
(`scripts/detectors_t0.py`) krijgen **alleen de bars** — nooit de labels. Voor D06
krijgen ze een eventkalender die ook tijdstippen zonder ingreep bevat, zodat de
detector niet zijn eigen antwoord terugkrijgt.

Twee getallen per detector per scenario:

- **AUC** — scheidt de detector de ingreep van de rest, ongeacht de drempel? Dit is
  het eerlijke getal, want de drempel is niet op de labels afgesteld.
- **Recall / precision bij de drempel uit de spec** — wat de detector doet zoals hij
  in [02-detectoren.md](02-detectoren.md) is opgeschreven, zonder bijstellen.

**Wat dit niet bewijst.** De injectie is door ons bedacht. Een detector die precies
onze injectie herkent, kan in de echte wereld nog steeds niets waard zijn. Deze
benchmark toetst de **implementatie**, niet de wereld. Zie §7.

## 2. De scenario's

| Scenario | Wat het doet | Familie |
|---|---|---|
| `clean` | niets | — |
| `volume_sticky` | volume ×3–9, prijs staat stil | F1/F2 |
| `volume_moved` | volume ×3–9 **met** echte range-expansie | controlegroep |
| `event_spike` | piek rond een bekend tijdstip, geen range-expansie | F5 |
| `zero_gaps` | losse bars met exact nul volume tussen volume in | F1 |
| `flat_session` | uurprofiel weggepoetst over 20 dagen | F3 |
| `constant_volume` | volume bijna constant over 20 dagen | F3 |
| `anti_correlated` | volume onafhankelijk van de prijsbeweging | F3 |

## 3. Resultaten — synthetische basis

60 dagen synthetische 15-minutenbars, seed 7.

### 3.1 AUC per scenario

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| clean | — | — | — | — | — | — |
| volume_sticky | 0.88 | 0.92 | 0.55 | 0.50 | 0.87 | 0.50 |
| volume_moved | 0.96 | 0.79 | 0.74 | 0.50 | 0.92 | 0.50 |
| event_spike | 0.96 | 0.95 | 0.64 | 0.50 | 0.93 | 0.82 |
| zero_gaps | 0.00 | 0.00 | 0.52 | **1.00** | 0.62 | 0.50 |
| flat_session | 0.50 | 0.54 | **0.97** | 0.50 | 0.43 | 0.50 |
| constant_volume | 0.46 | 0.51 | **0.97** | 0.50 | 0.41 | 0.50 |
| anti_correlated | 0.51 | 0.52 | **0.98** | 0.50 | 0.57 | 0.50 |

### Recall bij de drempel uit de spec

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| clean | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| volume_sticky | 0.58 | 0.16 | 0.00 | 0.00 | 0.68 | 0.00 |
| volume_moved | 0.77 | 0.00 | 0.00 | 0.00 | 0.81 | 0.00 |
| event_spike | 0.77 | 0.15 | 0.00 | 0.00 | 0.77 | 0.63 |
| zero_gaps | 0.00 | 0.00 | 0.08 | **1.00** | 0.00 | 0.00 |
| flat_session | 0.00 | 0.01 | 0.73 | 0.00 | 0.01 | 0.00 |
| constant_volume | 0.00 | 0.01 | 0.67 | 0.00 | 0.00 | 0.00 |
| anti_correlated | 0.02 | 0.01 | 0.89 | 0.00 | 0.05 | 0.00 |

### Precision bij de drempel uit de spec

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| clean | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| volume_sticky | 0.12 | 0.48 | 0.00 | 0.00 | 0.12 | 0.00 |
| volume_moved | 0.17 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 |
| event_spike | 0.18 | 0.50 | 0.00 | 0.00 | 0.16 | **1.00** |
| zero_gaps | 0.00 | 0.00 | 0.02 | **1.00** | 0.00 | 0.00 |
| flat_session | 0.00 | 0.79 | 0.93 | 0.00 | 0.01 | 0.00 |
| constant_volume | 0.00 | 0.77 | 0.93 | 0.00 | 0.01 | 0.00 |
| anti_correlated | 0.14 | 0.75 | 0.93 | 0.00 | 0.31 | 0.00 |

### Fout-positieven (FPR)

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| clean | 0.05 | 0.00 | 0.02 | 0.00 | 0.06 | 0.00 |
| volume_sticky | 0.04 | 0.00 | 0.02 | 0.00 | 0.05 | 0.00 |
| volume_moved | 0.04 | 0.00 | 0.02 | 0.00 | 0.05 | 0.00 |
| event_spike | 0.05 | 0.00 | 0.02 | 0.00 | 0.05 | 0.00 |
| zero_gaps | 0.05 | 0.00 | 0.02 | 0.00 | 0.06 | 0.00 |
| flat_session | 0.07 | 0.00 | 0.03 | 0.00 | **0.21** | 0.00 |
| constant_volume | 0.10 | 0.00 | 0.03 | 0.00 | **0.23** | 0.00 |
| anti_correlated | 0.05 | 0.00 | 0.03 | 0.00 | 0.06 | 0.00 |

## 4. Resultaten — echte BTCUSDT-bars

Zelfde benchmark, maar de basisreeks is nu **echte data**: `BTCUSDT-1m-2026-09.csv`
van `data.binance.vision`, 43.200 minuutbars uit september 2026, herschaald naar
2.880 bars van 15 minuten.

```bash
python scripts/run_benchmark.py --csv "data/BTCUSDT-1m-2026-09.csv"
```

### AUC op echte data

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| volume_sticky | 0.93 | 0.95 | 0.40 | 0.50 | 0.85 | 0.50 |
| volume_moved | 0.95 | 0.89 | 0.59 | 0.50 | 0.80 | 0.50 |
| event_spike | 0.97 | 0.98 | 0.56 | 0.50 | 0.81 | 0.77 |
| zero_gaps | 0.00 | 0.00 | 0.54 | **1.00** | 0.62 | 0.50 |
| flat_session | 0.53 | 0.50 | 0.88 | 0.50 | 0.70 | 0.50 |
| constant_volume | 0.50 | 0.46 | 0.87 | 0.50 | 0.66 | 0.50 |
| anti_correlated | 0.55 | 0.49 | 0.88 | 0.50 | 0.74 | 0.50 |

### Fout-positieven op echte data

| Scenario | D01 | D02 | D03 | D04 | D05 | D06 |
|---|---|---|---|---|---|---|
| clean | 0.07 | 0.01 | **0.10** | 0.00 | 0.06 | 0.00 |
| volume_moved | 0.06 | 0.01 | **0.21** | 0.00 | 0.05 | 0.00 |
| anti_correlated | 0.07 | 0.01 | 0.18 | 0.00 | 0.04 | 0.00 |

### Wat er verandert ten opzichte van de synthetische basis

| Detector | Synthetisch | Echt | Verklaring |
|---|---|---|---|
| **D03** | AUC 0,97–0,98, FPR 0,02 | AUC 0,87–0,88, **FPR 0,10–0,21** | Echte BTC heeft van nature periodes waarin volume en beweging losser samenhangen. De detector slaat daardoor veel vaker onterecht aan |
| **D06** | AUC 0,82 | AUC **0,77** | Zakt onder de 0,80-grens. Recall blijft 0,54, precision blijft 1,00 — hij heeft geen fout-positieven, maar mist de helft |
| **D02** | ving `volume_moved` niet (0,79) | ving het wél (0,89) | Op echte data is de range-vorm anders; dit is geen verbetering van de detector maar een eigenschap van de reeks |
| **D01, D04, D05** | — | vrijwel gelijk | Robuust voor de keuze van de basisreeks |

**De belangrijkste les:** twee van de zes detectoren gedragen zich op echte data
materieel anders dan op onze eigen reeks. Wie alleen op synthetische data kalibreert,
kalibreert op zijn eigen injector.

## 5. Seed-gevoeligheid

Zelfde benchmark, vijf seeds, 60 dagen synthetisch. AUC per detector/scenario:

| Seed | D01/sticky | D01/moved | D02/sticky | D03/anti-corr | D04/zero | D06/event |
|---|---|---|---|---|---|---|
| 1 | 0,97 | 0,95 | 0,96 | 0,98 | 1,00 | 0,80 |
| 2 | 0,93 | 0,97 | 0,92 | 0,97 | 1,00 | 0,82 |
| 3 | 0,94 | 0,95 | 0,93 | 0,98 | 1,00 | **0,72** |
| 4 | 0,96 | 0,96 | 0,94 | 0,97 | 1,00 | 0,76 |
| 5 | 0,96 | 0,93 | 0,96 | 0,98 | 1,00 | 0,76 |
| 7 | 0,88 | 0,96 | 0,92 | 0,98 | 1,00 | 0,82 |

**D06 is de enige die echt varieert** (0,72–0,82). Bij seed 3 zakt hij onder de grens.
D03 en D04 zijn volledig stabiel; D01 en D02 schommelen licht.

## 6. Wat elke detector vangt

| Detector | Vangt (AUC ≥ 0,80) | Mist |
|---|---|---|
| **D01** volume-uitbijter | volume_sticky, volume_moved, event_spike | zero_gaps, flat_session, constant_volume, anti_correlated |
| **D02** volume per beweging | volume_sticky, event_spike | volume_moved, zero_gaps, flat_session, constant_volume, anti_correlated |
| **D03** prijs-volume-correlatie | flat_session, constant_volume, anti_correlated | volume_sticky, volume_moved, event_spike, zero_gaps |
| **D04** nul-volume | zero_gaps | alle andere |
| **D05** sessieprofiel | volume_sticky, volume_moved, event_spike | zero_gaps, flat_session, constant_volume, anti_correlated |
| **D06** event zonder range | event_spike | alle andere |

## 7. De conclusies — inclusief de twee die niet standhielden

**1. D01 scheidt nepvolume niet van echt volume.**
Op de synthetische reeks met seed 7 scoorde D01 *hoger* op de legitieme injectie
(0,96) dan op de nepversie (0,88). **Dat bleek niet stabiel:** over vijf seeds wisselt
het welke van de twee hoger scoort (zie §5). Wat wél over alle seeds en op echte data
overeind blijft: D01 vangt beide vrijwel even goed, met AUC 0,88–0,97. Hij ziet "veel
volume", niet "verdacht volume". Dat is de onderbouwing voor de stelling in de README:
op T0 meet je het symptoom, niet de oorzaak.

**2. De 0,00 van D01 op `zero_gaps` is geen geluk maar een richting.**
Een AUC van 0,00 betekent perfecte scheiding in de *verkeerde* richting: nul-volume
krijgt de laagste score van alle bars. D01 is dus blind voor dit patroon, en een
gerapporteerde "0,00" moet je altijd lezen als "omgekeerd", nooit als "geen signaal".
D04 vangt het wel, met 1,00/1,00/1,00 — op beide reeksen.

**3. D02 heeft een drempelprobleem, geen modelprobleem.**
AUC 0,92 maar recall 0,16 op `volume_sticky` bij drempel 3,5. De scheiding is er, de
drempel is te conservatief voor injecties van 3–9×. Verlagen helpt de recall maar kost
precision; dat is een afweging die je expliciet moet maken en documenteren.

**4. D05 slaat op alles wanneer het uurprofiel weg is.**
Op `flat_session` en `constant_volume` is de FPR op synthetische data 0,21–0,23: bijna
een kwart van de normale bars wordt gemarkeerd. Logisch — als het profiel ontbreekt, is
élke bar een afwijking — maar het maakt D05 onbruikbaar als zelfstandige detector.
Hij hoort alleen als bijdrage in D24.

**5. D06 is de scherpste, maar niet de stabielste.**
Precision 1,00 op beide reeksen en **nul** fout-positieven op de controlegroep
`volume_moved`. Maar de AUC zakt op echte data naar 0,77 en op seed 3 naar 0,72. Hij
vangt de piek zonder beweging en laat de legitieme piek met beweging lopen — dat is
precies waarom de eventkalender een harde eis is: zonder onafhankelijke events is D06
gewoon D02.

**6. D03 is de kampioen van de synthetische wereld en de zwakke broeder in het echt.**
AUC 0,97–0,98 en FPR 0,02 op onze eigen reeks; AUC 0,88 en **FPR 0,10–0,21** op echte
BTCUSDT-bars. Dit is het duidelijkste bewijs dat een benchmark op zelfgemaakte data je
een te rooskleurig beeld geeft.

## 8. De toets op échte labels (Mt. Gox)

Alles hierboven gebruikt onze eigen injectie. Er bestaat één publieke set met echte
wash-labels: de feature-tabel van Falk et al. (2026) op Mendeley, DOI
`10.17632/4hyxfwzpgg.2`, CC BY 4.0. `gox_ml_samples.csv` is 940 MB en heeft 17
kolommen met afgeleide features plus het label `wash`.

```bash
python scripts/probe_mendeley_features.py --file gox_ml_samples.csv --mb 24
```

Dat haalt 24 MB op met een HTTP-Range-verzoek en rekent in het geheugen — er wordt
niets opgeslagen. Uitkomst op 150.000 rijen (35,0% wash), AUC per feature:

| Feature | Nodig | AUC |
|---|---|---|
| `seller_7d_trade_count` | accounthistorie (T3) | 0,740 |
| `seller_24h_trade_count` | accounthistorie (T3) | 0,714 |
| `buyer_7d_trade_count` | accounthistorie (T3) | 0,712 |
| `seller_all_btc_sum` | accounthistorie (T3) | 0,704 |
| `seller_7d_btc_sum` | accounthistorie (T3) | 0,691 |
| `cumu_wash_percent_opt` | onduidelijk | 0,537 |
| `round_level` | **publieke bars (T0)** | 0,524 |
| `time_since_last_trade` | **publieke bars (T0)** | 0,505 |
| `price_deviation` | **publieke bars (T0)** | 0,501 |
| `hours` | **publieke bars (T0)** | 0,498 |
| `bitcoins` | **publieke bars (T0)** | 0,423 |

**De features die wij kunnen berekenen, scheiden niets.** Alles wat uit publieke bars
komt zit op 0,50. De scheiding zit in de tegenpartij-identiteit — en zelfs dan haalt de
beste *enkele* feature 0,74, tegenover de 0,97 die Falk et al. rapporteren met een
multivariate XGB over alle features samen.

Dit is de scherpste formulering van de stelling in de README die we tot nu toe hebben:
op T0 meet je het symptoom. Niet omdat onze detectoren slecht zijn, maar omdat de
informatie er niet in zit.

**Wat deze meting niet is:** één prefix van 150.000 rijen, enkelvoudige features, geen
cross-validatie, geen multivariate vergelijking met hun model. Het is een ondergrens
voor wat T0 oplevert, geen eindcijfer.

## 9. Wat dit niet bewijst

- **De injectie is van ons.** Een detector die onze 3–9×-piek herkent, herkent geen
  echte wash trading. De reeks is nu echt (§4), de *ingreep* nog steeds niet.
- **Eén maand, één pair, één venue.** September 2026, BTCUSDT, Binance. Of de FPR van
  D03 op een rustiger maand of een ander pair ook 0,10 is, weten we niet.
- **Zes detectoren is niet de catalogus.** D07–D26 staan er niet in; die vragen tick-,
  orderboek- of accountdata.
- **De injectie is sterker dan de werkelijkheid.** Wij zetten volume 3–9× hoger. Een
  echte wash trader die 1,3× doet, is met deze drempels onzichtbaar.

## 10. Wat hieruit volgt

| Actie | Waarom |
|---|---|
| ~~Benchmark op echte BTCUSDT-bars~~ | **Gedaan** — en het veranderde twee conclusies |
| ~~Seed-gevoeligheid (seed 1–5)~~ | **Gedaan** — D06 varieert 0,72–0,82; de rest is stabiel |
| ~~T0-features toetsen op echte labels~~ | **Gedaan** — §8: alles op 0,50 |
| D02-drempel expliciet afwegen en vastleggen | Recall 0,16 (synthetisch) / 0,43 (echt) is te laag om te publiceren |
| D03-validatie op meer maanden en pairs | FPR 0,10–0,21 op echte data is te hoog voor een detector die prioriteit 2 heeft |
| D05 alleen als bijdrage aan D24 gebruiken | FPR van 0,21 maakt hem als losse detector onbruikbaar |
| D01 nooit als verdenking presenteren | Hij vangt legitiem hoog volume vrijwel even goed als nepvolume |
| Niet verder investeren in T0 als *bewijs* | §8 laat zien dat de informatie er niet in zit; T0 blijft een triagefilter |
