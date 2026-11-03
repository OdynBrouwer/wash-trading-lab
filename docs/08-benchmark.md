# 08 — Benchmark: welke T0-detector vangt welke injectie

Resultaten van `scripts/run_benchmark.py` op 60 dagen synthetische 15-minutenbars,
seed 7. Herhaalbaar met:

```bash
python scripts/run_benchmark.py --days 60 --seed 7
python -m unittest discover -s tests -v
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
benchmark toetst de **implementatie**, niet de wereld. Zie §5.

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

## 3. Resultaten

### AUC per scenario

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

## 4. Wat elke detector vangt

| Detector | Vangt (AUC ≥ 0,80) | Mist |
|---|---|---|
| **D01** volume-uitbijter | volume_sticky, volume_moved, event_spike | zero_gaps, flat_session, constant_volume, anti_correlated |
| **D02** volume per beweging | volume_sticky, event_spike | volume_moved, zero_gaps, flat_session, constant_volume, anti_correlated |
| **D03** prijs-volume-correlatie | flat_session, constant_volume, anti_correlated | volume_sticky, volume_moved, event_spike, zero_gaps |
| **D04** nul-volume | zero_gaps | alle andere |
| **D05** sessieprofiel | volume_sticky, volume_moved, event_spike | zero_gaps, flat_session, constant_volume, anti_correlated |
| **D06** event zonder range | event_spike | alle andere |

## 5. De vijf dingen die dit ons vertelt

**1. D01 scheidt nepvolume niet van echt volume — integendeel.**
Op `volume_moved`, waar het volume legitiem is, scoort D01 **hoger** (AUC 0,96) dan op
`volume_sticky` (0,88). Hij ziet "veel volume", niet "verdacht volume". Dit is de beste
onderbouwing die we tot nu toe hebben voor de stelling in de README: op T0 meet je het
symptoom, niet de oorzaak. Een T0-score mag daarom nooit als verdenking worden
gepresenteerd.

**2. De 0,00 van D01 op `zero_gaps` is geen geluk maar een richting.**
Een AUC van 0,00 betekent perfecte scheiding in de *verkeerde* richting: nul-volume
krijgt de laagste score van alle bars. D01 is dus blind voor dit patroon, en een
gerapporteerde "0,00" moet je altijd lezen als "omgekeerd", nooit als "geen signaal".
D04 vangt het wel, met 1,00/1,00/1,00.

**3. D02 heeft een drempelprobleem, geen modelprobleem.**
AUC 0,92 maar recall 0,16 op `volume_sticky`. De scheiding is er, de drempel (3,5) is
te conservatief voor injecties van 3–9×. Verlagen helpt de recall maar kost precision;
dat is een afweging die je expliciet moet maken en documenteren, niet stilzwijgend.

**4. D05 slaat op alles wanneer het uurprofiel weg is.**
Op `flat_session` en `constant_volume` is de FPR 0,21–0,23: bijna een kwart van de
normale bars wordt gemarkeerd. Logisch — als het profiel ontbreekt, is élke bar een
afwijking — maar het maakt D05 onbruikbaar als zelfstandige detector. Hij hoort alleen
als bijdrage in D24, precies zoals de prioritering al zegt.

**5. D06 is de enige die het verschil maakt dat ertoe doet.**
Precision 1,00, AUC 0,82, recall 0,63, en **nul** fout-positieven op de controlegroep
`volume_moved`. Hij vangt de piek zonder beweging en laat de legitieme piek met
beweging lopen. Dat is precies waarom de eventkalender een harde eis is: zonder
onafhankelijke events is D06 gewoon D02.

## 6. Wat dit niet bewijst

- **De injectie is van ons.** Een detector die onze 3–9×-piek herkent, herkent geen
  echte wash trading. De volgende stap is dezelfde benchmark op **echte** Binance-bars,
  via `injector.load_ohlcv_csv()`. Dat is nog niet gedaan.
- **De basisreeks is synthetisch.** Hij heeft een uurprofiel, samenhang tussen range en
  volume, en nieuwspieken — maar hij is geen markt. Absolute getallen zijn niet te
  vergelijken met echte data.
- **Zes detectoren is niet de catalogus.** D07–D26 staan er niet in; die vragen tick-,
  orderboek- of accountdata.
- **Eén seed.** De getallen zijn reproduceerbaar, maar niet getest op seed-gevoeligheid.
  Wie hierop wil bouwen, draait eerst `--seed 1..5` en kijkt hoe stabiel het beeld is.

## 7. Wat hieruit volgt

| Actie | Waarom |
|---|---|
| Benchmark herhalen op echte BTCUSDT-bars | De synthetische basis is een tussenstap, geen meting |
| Seed-gevoeligheid meten (seed 1–5) | Eén seed is één datapunt |
| D02-drempel expliciet afwegen en vastleggen | Recall 0,16 is te laag om te publiceren |
| D05 alleen als bijdrage aan D24 gebruiken | FPR van 0,21 maakt hem als losse detector onbruikbaar |
| D01 nooit als verdenking presenteren | Hij scoort hoger op legitiem volume dan op nepvolume |
