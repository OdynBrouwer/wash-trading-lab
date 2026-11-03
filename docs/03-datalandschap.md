# 03 — Datalandschap

Welke data bestaat er, wat is gratis, wat ontbreekt structureel — en hoe je zonder
ground truth tóch iets kunt valideren.

## 1. Per tier

### T0 — OHLCV
| Bron-type | Wat je krijgt | Beperking |
|---|---|---|
| Beurs-API (REST) | candles per interval | Beperkte historie; herberekend per interval, dus niet bit-vast |
| Aggregators | samengevoegd volume over venues | **Maskeert juist het probleem**: aggregatie verbergt welke venue afwijkt |
| TradingView / grafiek | OHLCV + indicatoren | Historie beperkt per plan |

**Belangrijk:** voor nepvolume-detectie is een *aggregaat* minder bruikbaar dan
per-venue data. Een detector moet kunnen zeggen "deze venue wijkt af van de andere op
hetzelfde pair, op hetzelfde moment" — dat kan alleen met data per venue.

### T1 — Tick-data (trades)
| Bron-type | Wat je krijgt | Beperking |
|---|---|---|
| Beurs-websocket | live trades, soms met agressor-kant | Geen historie; je moet zelf opslaan |
| Historische tick-archieven (commercieel) | trades + orderboek-events over jaren | Betaald; prijs op te vragen, niet in dit document |
| On-chain DEX | elke swap, met wallet | Alleen DEX, niet CEX |

**Kritisch punt:** de agressor-kant (wie initieerde de trade) is niet altijd
beschikbaar. Zonder dat veld zijn D11 (gepaarde prints) en D18 (Kyle's λ) niet
betrouwbaar te berekenen. Dit is een harde eis, geen nice-to-have.

### T2 — Orderboek
| Bron-type | Wat je krijgt | Beperking |
|---|---|---|
| Websocket depth-stream | snapshots + updates | Meestal **geen cancels** als apart event; je moet ze afleiden uit de diff |
| Volledige book-events (commercieel) | add/cancel/trade per niveau, met tijdstip | Duur; klein aantal venues |
| Zelf reconstrueren | uit diffs | Foutgevoelig; sequence-gaten zijn dodelijk |

**Zonder cancels geen spoofing-detectie.** Dit is de belangrijkste structurele
beperking van T2 op gratis data.

### T3 — Accounts en on-chain
| Bron-type | Wat je krijgt | Beperking |
|---|---|---|
| Publieke blockchain | alle transfers, met adres | Geen identiteit; clustering is heuristiek |
| Block-explorer-API's | gelabelde adressen | Labels zijn momentopnames, niet reproduceerbaar |
| CEX-accountdata | echte wash score | **Niet publiek.** Alleen beurs of toezichthouder |

**Conclusie:** de enige plek waar de *definitie* van wash trading (geen
eigendomsovergang) direct meetbaar is, is óf on-chain (waar alles publiek is) óf
binnen een beurs (waar wij niet komen). Voor CEX-spot op publieke data blijft het
bij symptomen. Dat is geen tekortkoming van het project maar een eigenschap van de
data, en het moet in de README staan.

## 2. Het labelprobleem

Er bestaat **geen publieke dataset** met gelabelde wash trades op CEX-spot. De
gelabelde datasets in de literatuur gaan over phishing, Ponzi en scams (zoals
Elliptic en de datasets in het Springer-boek), niet over volume.

Gevolg: je kunt een detector niet "trainen" en ook niet zonder meer meten hoe goed
hij is. Elke precision/recall die je in de literatuur ziet, is berekend op een
*model* van wat nepvolume is, niet op waargenomen bedrog.

Dat is geen detail. Het betekent dat dit project moet kiezen uit drie houdingen:

| Houding | Gevolg |
|---|---|
| Doen alsof je ground truth hebt | Onwetenschappelijk; elke score is schijnprecisie |
| Helemaal geen validatie | Onbruikbaar; je weet niet of een detector ruis meet |
| **Synthetische ground truth, met benoemde beperking** | Eerlijk en bruikbaar, mits je de beperking hardop zegt |

Dit project kiest de derde.

## 3. Synthetische benchmark (ontwerp)

Doel: een detector kunnen scoren op data waarvan je de waarheid kent.

**Opzet**

1. Neem een echte, schone trade-stream van een gereguleerde venue als basis.
2. Injecteer kunstmatig nepvolume met een **bekend** aandeel $p$ (bijv. 5%, 20%, 50%).
3. Laat de detector een schatting $\hat p$ geven.
4. Scoor: fout $\lvert \hat p - p \rvert$, precision/recall per detector,
   en de mate waarin de detector de *geïnjecteerde* trades precies aanwijst.

**Injectieparameters die je moet variëren** (want elk ervan breekt een andere detector):

| Parameter | Variatie | Welke detector het breekt |
|---|---|---|
| Omvang van de injectie | 1% → 60% | alle |
| Grootteverdeling | uniform, rond, echte verdeling gevolgd | D07, D08, D09, D10 |
| Regelmaat in tijd | periodiek, Poisson, gebundeld | D12, D01 |
| Prijsgedrag | prijs ongemoeid laten vs. licht meetrekken | D02, D03 |
| Tegenpartij-structuur | willekeurig vs. vaste kleine groep | D22 |
| Duur | continu vs. korte bursts | D05 |

**De beperking die je móet benoemen:** een detector die de injectie terugvindt, bewijst
alleen dat hij *die* injectie terugvindt. Echte manipulatie kan anders zijn. De
benchmark meet dus twee dingen: (a) of de implementatie correct is, en (b) welke
detectoren gevoelig zijn voor welk artefact — niet of ze de werkelijkheid vangen.

Dat is nog steeds veel waard: het voorkomt stille rekenfouten en het maakt de
zwakke plekken zichtbaar.

## 4. Databewaring en reproduceerbaarheid

- Ruwe data hoort **niet** in de repository (groot, en deels herdistributie-beperkt).
  `data/` dus in `.gitignore`, met een `data/README.md` dat beschrijft hoe je de
  data opnieuw ophaalt.
- Elke detector moet met een **kleine vaste testset** in de repo te draaien zijn:
  een paar duizend trades is genoeg voor een regressietest.
- Tijdstempels altijd in UTC, altijd met tijdzone expliciet. Verkeerde tijdzone is de
  meest voorkomende bron van "detector werkt niet".
- Geen persoonlijke data. Geen KYC. Geen e-mailadressen. Wallet-adressen zijn
  publiek, maar behandel ze als gevoelig.

## 5. Openstaande data-vragen

- `OPEN` — Welke gratis bron levert **per-venue** historische OHLCV van voldoende
  lengte, met een betrouwbare tijdstempel? Nog niet vastgesteld.
- `DEELS OPGELOST` — Orderboek-events met cancels: bestaan niet als kant-en-klare publieke
  feed, maar cancellaties zijn **afleidbaar** uit diepte-diffs. Zie §6.2.
- `OPEN` — Hoe lang moet de basislijn zijn voor D05 (sessieprofiel) om niet elke week
  opnieuw te kalibreren?
- `OPEN` — Wat is het minimaal aantal trades voor D08 (Benford) om niet op ruis te
  toetsen? Vermoeden: duizenden, maar niet onderbouwd.

---

## 6. De twee structurele gaten: wat je zelf kunt doen

### 6.1 Een gelabelde CEX-spot dataset

Bestaat niet publiek. Cong et al. werkten met propriétaire TokenInsight-data
(448.475.535 transacties, 29 beurzen); Bitwise met eigen scherm-scraping. Niemand heeft
het vrijgegeven.

| # | Route | Wat je krijgt | Kosten/risico |
|---|---|---|---|
| **1** | **Victor & Weintraud-dataset**: Zenodo `4540223`, code op GitHub `friedhelmvictor/lob-dex-wash-trading-paper` | Gelabelde wash trades op **accountniveau** mét bedragen. DEX, niet CEX — maar de structuren (self-trade, 2-account, cycli) zijn identiek | Gratis. Beste startpunt |
| **2** | **Aloosh & Li (2021)** natrekken: verifiëren de Cong-methodologie met **gelekte Mt. Gox-data** waarin je individuele traders hun eigen orders ziet clearen | Dichtstbijzijnde echte **CEX**-ground truth op accountniveau die bestaat | Paper zoeken; ruwe data mogelijk niet publiek |
| **3** | **Synthetische injectie** (§3) | Ground truth voor CEX-OHLCV met bekende omvang | Gratis; meet alleen of de implementatie klopt |
| **4** | Zelf ground truth maken op **testnet/sandbox** | Echte orderflow met bekende labels | **Alleen testnet.** Wash trading op een live beurs is strafbaar onder MiCAR en Rule 575 |
| 5 | Zwakke labels via kruislingse detectoren | Probabilistische dataset | Circulariteit: je labelt met het model dat je wilt valideren |
| 6 | Dataverzoek bij platform of toezichthouder onder MiCAR | Echte data | MiCAR verplicht tot detectie, niet tot publicatie. Kans klein |

**Advies:** 1 + 2 nu, 3 parallel. Het vaststellen dát er geen publieke CEX-dataset bestaat
— mét een inventarisatie van wat er wel is — is zelf een publicatie waard.

### 6.2 Orderboek-events met cancels

Hier is het goede nieuws anders: **dit kun je zelf bouwen.**

De meeste CEX-feeds geven geen order-ID-events, alleen diepte-diffs. Maar een cancel is
afleidbaar:

$$\text{cancel}(p,t) = \Delta q(p,t) < 0 \quad \text{zonder dat er een trade op } p \text{ rond } t \text{ was}$$

Sluit dus een depth-diff-stream én een trade-stream op volgnummer op elkaar aan, en
classificeer elke afname van een prijsniveau als **fill** of **annulering**. Dan heb je de
cancel-ratio (D17) die nu nog `OPEN` staat.

| Route | Wat het oplevert | Beperking |
|---|---|---|
| **Zelf reconstrueren uit diffs + trades** | cancel-ratio, order-to-trade, levenstijd per prijsniveau | Geen accountattributie; icebergs en hidden orders blijven onzichtbaar |
| **On-chain LOB-DEX** (EtherDelta, IDEX) | annuleringen zijn on-chain events: publiek, permanent, mét adres | Alleen DEX |
| Commerciële tick-archieven | volledige book-events met cancels over jaren | Betaald |

**Wat je kunt bijdragen:** de reconstructiemethode uitwerken, valideren tegen een venue waar
je wél cancellvelden hebt, en als opensource-tool publiceren. Dat bestaat nog niet als net
pakket — en het is precies het gereedschap dat iedereen mist die zelf nepvolume wil meten.

**Wat je niet kunt oplossen:** op een CEX blijft F4 geaggregeerd. Zonder account-ID weet je
*dát* er meer geannuleerd wordt dan fills verklaren, niet *wie*.
