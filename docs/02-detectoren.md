# 02 — Catalogus van detectoren

Elke detector met: tier, input, formule, output, valkuil en status.

Formules staan in [`washtrading-formules.md`](washtrading-formules.md);
dit document verwijst ernaar in plaats van ze te dupliceren.

**Status-legenda**
- `SPEC` — gespecificeerd, nog niet geïmplementeerd
- `PROTO` — prototype bestaat (nog niet in dit project)
- `OPEN` — specificatie incompleet, aanvulling nodig
- `ZWAK` — werkt, maar met bekende hoge foutenkans; alleen als onderdeel van een geheel

---

## T0 — Alleen OHLCV

Haalbaar voor iedereen met een grafiek. Meet het **symptoom**, nooit de oorzaak.

### D01 — Robuuste volume-uitbijter
| | |
|---|---|
| **Doel** | Volume dat niet bij zijn eigen historie past |
| **Input** | $V_t$, lookback $n$ |
| **Formule** | Formules §4.3: $z^{\text{rob}}_t = \dfrac{V_t - \text{mediaan}(V)}{1{,}4826 \cdot \text{MAD}(V)}$ |
| **Output** | score per candle |
| **Valkuil** | Nieuws, listings en expiraties geven dezelfde piek. Zonder context is dit ruis. **Gemeten:** hij vangt legitiem hoog volume (AUC 0,96) vrijwel even goed als nepvolume (0,88) — zie [08-benchmark.md](08-benchmark.md) §7.1 |
| **Status** | `PROTO` — `scripts/detectors_t0.py`, gescoord in [08-benchmark.md](08-benchmark.md) |

### D02 — Volume per bewegingseenheid
| | |
|---|---|
| **Doel** | Veel volume zonder prijsresultaat |
| **Input** | $V_t$, $H_t$, $L_t$, $C_t$ |
| **Formule** | Formules §4.2: $V\!R_t = V_t / (H_t - L_t)$ en $E_t = V_t / \lvert r_t \rvert$ |
| **Output** | ratio per candle; hoge waarde = veel moeite, weinig resultaat |
| **Valkuil** | Werkt ook bij echte absorptie (grote passieve order). Niet onderscheidbaar van nepvolume op T0. **Gemeten:** AUC 0,92 maar recall 0,16 bij drempel 3,5 — het model scheidt wel, de drempel is te streng |
| **Status** | `PROTO` — `scripts/detectors_t0.py`, gescoord in [08-benchmark.md](08-benchmark.md) |

### D03 — Rollende prijs-volume-correlatie
| | |
|---|---|
| **Doel** | Volume dat niet meebeweegt met de prijs |
| **Input** | $\lvert r_t \rvert$ en $V_t$ over venster $n$ |
| **Formule** | Formules §4.1 (Pearson) |
| **Output** | $\rho \in [-1, 1]$; laag/negatief is verdacht |
| **Referentie** | Bitcenter (2023) gebruikte dit om één beurs te identificeren met de laagste correlatie van zeven |
| **Valkuil** | $\rho$ is niet stationair; gebruik een rollend venster en vergelijk met **peer-markten**, niet met een absolute drempel. **Gemeten:** vangt de drie vorm-injecties op synthetische data met AUC 0,97–0,98 en is stil op volumepieken (0,55–0,74) — precies zoals bedoeld. **Op echte BTCUSDT-bars zakt dit naar AUC 0,87–0,88 en loopt de FPR op naar 0,10–0,21** — zie [08-benchmark.md](08-benchmark.md) §4 |
| **Status** | `PROTO` — `scripts/detectors_t0.py`, gescoord in [08-benchmark.md](08-benchmark.md) |

### D04 — Nul-volume en stale candles
| | |
|---|---|
| **Doel** | Uren of dagen met exact nul volume |
| **Input** | $V_t$ |
| **Formule** | Formules §4.7: $\text{nulRatio} = \#\{t: V_t = 0\} / n$ |
| **Output** | ratio |
| **Referentie** | Bitwise (SEC 2019) noemt "multiple hours (and days) with zero volume" expliciet als signaal |
| **Valkuil** | Een kleine beurs heeft legitiem dunne uren. Het signaal is de **discontinuïteit**: uren met veel volume, dan exact nul, dan weer volume. **Gemeten:** de enige detector met 1,00/1,00/1,00 — maar dat is een triviale overeenkomst met de injectie |
| **Status** | `PROTO` — `scripts/detectors_t0.py`, gescoord in [08-benchmark.md](08-benchmark.md) |

### D05 — Sessieprofiel-afwijking
| | |
|---|---|
| **Doel** | Volume dat geen dag-en-nachtpatroon heeft |
| **Input** | $V$ per uur, historie per uur |
| **Formule** | Formules §4.6: $d_h = (V_h - \hat V_h)/\hat\sigma_h$ |
| **Parameters** | basislijn 28 dagen (minimum 14, uitbreidbaar naar 56); zie Formules §4.8 voor de keuze van de mediaan |
| **Output** | afwijking per uur |
| **Valkuil** | Vereist minstens enkele weken historie en een markt met een echt sessieprofiel. Bij 24-uurs crypto is het patroon zwakker dan bij aandelen. **Reken de basislijn niet per "zelfde uur, zelfde weekdag"**: 28 dagen geeft dan vier observaties per bucket, en een mediaan van vier is niet robuust. Neem de mediaan over alle dagen binnen dat uur en toets daarna of er een weekdagfactor is |
| **Status** | `ZWAK` — `scripts/detectors_t0.py`. **Gemeten:** FPR 0,21–0,23 zodra het uurprofiel ontbreekt; als losse detector onbruikbaar, alleen als bijdrage aan D24 |

### D06 — Volume zonder range-expansie rond een event
| | |
|---|---|
| **Doel** | Prijsgerichte trucs (F5) rond fixings, listings, expiraties |
| **Input** | $V_t$, $H_t$, $L_t$, event-kalender |
| **Formule** | Twee onafhankelijke grootheden. Volume-intensiteit uit Formules §4.8: $VI_t = V_t/\text{mediaan}(V_{\text{baseline}})$. Range-respons: $RE = \text{mediaan}(R_{\text{event}})/\text{mediaan}(R_{\text{baseline}})$ met $R_t = H_t - L_t$. Score: $D06 = \text{mediaan}(VI_{\text{event}})$ |
| **Parameters** | eventvenster ±30 minuten; baseline dezelfde duur op vergelijkbare niet-eventdagen; minimaal 10 referentieperiodes |
| **Output** | $VI$, $RE$ en de combinatie |
| **Interpretatie** | hoog $VI$ + laag $RE$ = verdacht; hoog + hoog = normale eventactiviteit; laag + hoog = lage liquiditeit; laag + laag = geen bijzondere activiteit |
| **Valkuil** | Eén normalisatie, niet twee: $VI$ deelt al door de basislijn, dus een extra deling door $\text{mediaan}(VI_{\text{baseline}})$ is per constructie ≈ 1. Vergelijk bovendien gelijke tijdsintervallen en vergelijkbare tijdstippen, anders vertekent het dag-nachtritme de uitkomst |
| **Status** | `PROTO` — `scripts/detectors_t0.py`. **Gemeten:** precision 1,00, AUC 0,82, recall 0,63, en **nul** fout-positieven op de controlegroep met echte beweging. Op echte BTCUSDT-bars zakt de AUC naar 0,77 en over vijf seeds varieert hij 0,72–0,82 — de minst stabiele van de zes. Harde afhankelijkheid blijft een event-kalender met bron, publicatietijd en eventtijd. Zonder kalender valt dit terug op D02 |

---

## T1 — Tick-data (trades)

Hiermee test je de **vorm** van de trade-verdeling. Dit is de kern van het werk van
Cong, Li, Tang & Yang (NBER 30783): >70% wash trading op ongereguleerde venues,
gemeten op 29 centrale beurzen.

> **Alleen bruikbaar op CEX.** Victor & Weintraud (WWW '21, §4.3) onderzochten dezelfde
> verdelingen op DEX en vonden dat ze **normaal** handelsgedrag vertonen: lokale pieken op
> ronde getallen, dalende frequentie bij grotere bedragen. Hun conclusie: *"likely
> unsuitable as an indicator for wash trading on DEX"*. D07–D10 zijn dus CEX-gereedschap.

### D07 — Roundness-ratio
| | |
|---|---|
| **Doel** | Onnatuurlijk veel ronde trade-groottes |
| **Input** | alle trade-groottes $V_i$ |
| **Formule** | Formules §3.2: $R_k = \#\{V \equiv 0 \pmod{10^k}\} / N$ |
| **Output** | $R_1$, $R_2$, $R_3$ |
| **Valkuil** | Retailleden handelen ook rond. Vergelijk met een gereguleerde referentievenue op **hetzelfde pair, dezelfde periode** |
| **Beperking** | **CEX-only.** Op DEX zijn ronde pieken juist normaal gedrag (Victor & Weintraud 2021, §4.3) |
| **Tekenrisico** | Op NFT-marktplaatsen vonden Falk, Tsoukalas & Zhang (2026) dat **legitieme** trades *méér* rond ronde getallen clusteren dan wash trades. Het signaal kan dus omklappen. Gebruik D07 alleen binnen één venue, nooit als vergelijking tussen venues of asset-klassen |
| **Status** | `SPEC` (CEX) |

### D08 — Eerste-cijfer-verdeling (Benford)
| | |
|---|---|
| **Doel** | Cijferverdeling die niet op organische handel lijkt |
| **Input** | trade-groottes |
| **Formule** | Formules §3.1: $P(d) = \log_{10}(1 + 1/d)$ plus $\chi^2$-toets, df = 8 |
| **Output** | $\chi^2$, p-waarde, per-cijfer-afwijking |
| **Referentie** | Cong et al. (NBER 30783): de Benford-gebaseerde schatter komt op **16,3%** tegen **77,5%** voor hun roundness-schatter — factor vijf verschil. De auteurs noemen Benford zelf *"somewhat lower bounds"* |
| **Valkuil** | Benford geldt voor groottes over **meerdere ordes van grootte**. Bij een pair met een smalle prijsrange of bij afgeronde tick-groottes faalt de wet ook zonder manipulatie. Bovendien ziet de wet alleen het eerste cijfer, dus mist hij nepvolume dat alle negen cijfers raakt. Gebruik hem als robuustheidstoets, nooit als hoofdmaat |
| **Parameters** | Operationele drempel, **geen bewezen statistisch minimum**: <500 trades niet classificeren; 500–999 alleen exploratief; 1.000–4.999 voorlopig; 5.000–9.999 screening; 10.000+ robuuster. Gebruik een goodness-of-fit-toets met bootstrap-calibratie in plaats van alleen $\chi^2$ |
| **Beperking** | **CEX-only** (Victor & Weintraud 2021, §4.3) |
| **Tekenrisico** | Falk, Tsoukalas & Zhang (2026): op NFT wijken **legitieme** trades *méér* van Benford af dan wash trades. Een gevonden afwijking is dus geen bewijs van manipulatie, en op sommige markten wijst hij de verkeerde kant op |
| **Status** | `ZWAK` |

### D09 — Uniformiteit van trade-groottes
| | |
|---|---|
| **Doel** | Te weinig spreiding |
| **Input** | trade-groottes |
| **Formule** | Formules §3.3: $\text{CV} = \sigma_V/\mu_V$ en robuust $\text{rCV} = \text{MAD}/\text{mediaan}$ |
| **Output** | CV, rCV |
| **Valkuil** | Market makers met vaste lot-groottes geven ook lage CV |
| **Beperking** | **CEX-only** (Victor & Weintraud 2021, §4.3) |
| **Status** | `SPEC` (CEX) |

### D10 — Staartindex (power law)
| | |
|---|---|
| **Doel** | Ontbrekende staart: te weinig écht grote trades |
| **Input** | trade-groottes |
| **Formule** | Formules §3.4: Hill-schatter $\hat\alpha$ |
| **Output** | $\hat\alpha$ |
| **Valkuil** | Hill is gevoelig voor de keuze van $n$ (hoeveel staartpunten). Rapporteer altijd de gevoeligheid |
| **Beperking** | **CEX-only** (Victor & Weintraud 2021, §4.3) |
| **Status** | `SPEC` (CEX) |

### D11 — Gepaarde prints
| | |
|---|---|
| **Doel** | Twee prints die een spiegelbeeld zijn: zelfde prijs, zelfde grootte, tegengestelde kant, binnen $\delta_t$ |
| **Input** | trade-stream met agressor-kant |
| **Formule** | vereenvoudigde vorm van Cao's condities: $\lvert t_b - t_s \rvert < \delta_t \wedge \lvert V_b - V_s \rvert \le \delta_v \wedge \lvert P_b - P_s \rvert < \delta_p$ |
| **Output** | aantal paren per venster, aandeel in volume |
| **Valkuil** | **Grootste fout-positief-bron van het hele project.** Op drukke momenten zijn spiegelprints normaal: een market maker vult twee kanten. Alleen een *opeenvolging* van paren zonder prijsbeweging is verdacht |
| **Status** | `ZWAK` |

### D12 — Regelmaat in inter-arrival-tijden
| | |
|---|---|
| **Doel** | Machine-achtige cadans |
| **Input** | tijdstempels |
| **Formule** | $\text{CV}(\Delta t)$ en autocorrelatie van $\Delta t$ |
| **Output** | regulariteitsscore |
| **Valkuil** | Echte bots handelen ook regelmatig. Dit meet automatisering, niet manipulat |
| **Status** | `ZWAK` |

---

## T2 — Orderboek

Hier zit F4 (spoofing) en een groot deel van F5. Let op: **deze detectoren meten geen
wash trading.** Ze meten schijnliquiditeit.

### D13 — Diepte/volume-ratio
| | |
|---|---|
| **Doel** | Gerapporteerd volume dat het boek niet kan dragen |
| **Input** | $q(p)$ rond mid, dagvolume |
| **Formule** | Formules §5.2 en §5.3: $\kappa = D(\varepsilon)/V_{\text{dag}}$ |
| **Output** | $\kappa$ per band ($\varepsilon = 0{,}1\%, 1\%, 2\%$) |
| **Referentie** | Kaiko: Binance 64,3% van het volume tegen 30,7% van de diepte. Top-8: 91,7% diepte tegen 89,5% volume |
| **Valkuil** | Vereist gelijktijdige snapshots van meerdere venues op hetzelfde pair en moment |
| **Status** | `SPEC` |

### D14 — Spread onder belasting
| | |
|---|---|
| **Doel** | Spread die niet verwijdt wanneer volume piekt |
| **Input** | spread-tijdreeks, volume-tijdreeks, diepte in dezelfde band |
| **Formule** | Spread in bp uit Formules §5.1, volume-intensiteit uit §4.8, diepte $D(\varepsilon)$ uit §5.2. Score: $D14 = S^{\text{stress}}_{\text{bp}} / S^{\text{normaal}}_{\text{bp}}$ |
| **Output** | spread-ratio, $VI$ en diepte in dezelfde band ($\varepsilon \in \{0{,}1\%,\,1\%,\,2\%\}$) |
| **Interpretatie** | spread stabiel + diepte hoog = waarschijnlijk echte liquiditeit; stabiel + diepte laag = mogelijk verdachte prijsweergave; verwijdt + diepte laag = normale stressreactie; verwijdt + diepte hoog = mogelijk veranderde risicopremie |
| **Valkuil** | Een spread die niet verwijdt bij hoog volume is op zichzelf **geen** bewijs van nepvolume: een uitzonderlijk diep boek geeft hetzelfde beeld. Een negatieve correlatie alleen is dus onvoldoende. De dieptemeting is verplicht voor een sterke uitspraak; zonder diepte is D14 alleen een ondersteunende indicator bij D01 en D13–D17 |
| **Status** | `SPEC` |

### D15 — Slippage op eigen ordergrootte
| | |
|---|---|
| **Doel** | Wat je werkelijk betaalt, in plaats van wat de spread belooft |
| **Input** | mid op beslismoment, VWAP van eigen fills |
| **Formule** | Formules §5.4 |
| **Output** | slippage in bp per venue en per grootteklasse |
| **Valkuil** | Dit is de enige meting op *jouw* formaat, dus de eerlijkste; maar je hebt eigen fills nodig (paper trading volstaat niet exact). **Let op:** dit is de enige detector in de T2-reeks die *niet* met diepte-diffs alleen te draaien is — een diff zegt niets over hoe jóuw order gevuld werd |
| **Status** | `OPEN` — vereist eigen fills, geen formuleprobleem |

### D16 — Diepte-herstel
| | |
|---|---|
| **Doel** | Hoe snel het boek zich na consumptie herstelt |
| **Input** | diepte-tijdreeks |
| **Formule** | Formules §5.5: $t_{\text{refill}}(x)$ met $x = 0{,}9$ |
| **Output** | hersteltijd |
| **Valkuil** | Vereist hoge-frequentie snapshots; bij 1-minuut-resolutie onmeetbaar |
| **Status** | `OPEN` |

### D17 — Order-to-trade en cancel-ratio
| | |
|---|---|
| **Doel** | Spoofing/layering (F4) |
| **Input** | diepte-diffs + trade-stream (afgeleide cancel-ratio), of order-events met order-ID's als de venue die levert |
| **Formule** | $\text{OTR} = \#\text{orders}/\#\text{trades}$, $\text{CR} = \#\text{cancels}/\#\text{orders}$, plus levenstijd-verdeling |
| **Output** | ratio's per account of per prijsniveau |
| **Valkuil** | Zonder account-ID alleen geaggregeerd meetbaar, wat de foutenkans sterk verhoogt. **Noem een verdwenen hoeveelheid nooit een cancel**: spreek van `depth_decrease`, en splits in `trade_explained_decrease` (door een waargenomen trade verklaard) en `unexplained_decrease` (niet verklaard). Alleen die laatste is interessant voor spoofingonderzoek, en zelfs dan blijft het een hypothese |
| **Status** | `SPEC` — de cancel-ratio is afleidbaar uit diepte-diffs plus de trade-stream, zie [03-datalandschap.md](03-datalandschap.md) §6.2 |

### D18 — Prijsimpact per eenheid orderflow (Kyle's λ)
| | |
|---|---|
| **Doel** | Veel volume, geen impact |
| **Input** | gesigneerd orderflow-volume, prijsverandering |
| **Formule** | Formules §4.4: $\Delta p_t = \lambda \cdot \text{OF}_t + \varepsilon_t$ |
| **Output** | $\lambda$ |
| **Valkuil** | Vereist agressor-classificatie (wie initieerde de trade). Niet beschikbaar in elke feed |
| **Status** | `SPEC` |

---

## T3 — Accounts en on-chain

Hier pas wordt eigendom meetbaar — en dus de eigenlijke definitie van wash trading.

### D19 — Wash score per account
| | |
|---|---|
| **Doel** | Aandeel wash trades in het handelen van één account |
| **Input** | trade-records met account-IDs |
| **Formule** | Formules §2: $\text{WashScore}_{i,j} = \dfrac{\#\text{wash trades}}{\#\text{trades}}$ |
| **Output** | percentage per account per instrument |
| **Referentie** | Imisiker & Tas (2018), Istanbul Stock Exchange: in 1% van 9.999.582 account×aandeel-gevallen kwam minstens één wash trade voor; gemiddelde wash score 0,042 bij de niet-nul gevallen |
| **Valkuil** | Vereist accountdata die een buitenstaander niet heeft. Op een CEX alleen beschikbaar voor de beurs of de toezichthouder |
| **Status** | `OPEN` |

### D20 — Gesloten transactiecyclus
| | |
|---|---|
| **Doel** | De collusiegroep als geheel staat netto op nul |
| **Input** | orders met trader-ID, prijs, volume, tijdstip |
| **Formule** | Formules §1.2–§1.4 |
| **Output** | alarmering bij een gesloten cyclus |
| **Referentie** | Cao et al. (2015) |
| **Valkuil** | Vergt de volledige orderstroom van alle deelnemers. Op on-chain data wél mogelijk, want elke transfer is publiek |
| **Status** | `SPEC` (on-chain haalbaar) |

### D21 — Round-trip deposit/withdraw
| | |
|---|---|
| **Doel** | Opnemen en hetzelfde bedrag direct terugstorten = onnodige stap met kosten |
| **Input** | on-chain transfers naar/van een beursadres |
| **Formule** | geen; patroonherkenning op bedrag + richting + $\Delta t$ |
| **Referentie** | Springer *Blockchain Transaction Data Analytics*, regel 3505: een account neemt 0,4 ETH op bij Cryptopia en stort hetzelfde bedrag terug — "kan wijzen op misbruik als mixer óf op wash trading" |
| **Valkuil** | Zwak bewijs: dit kan ook een gebruiker zijn die van gedachten verandert. De bron noemt het zelf als *interpretatie*, niet als meting |
| **Status** | `ZWAK` |

### D22 — Tegenpartij-concentratie
| | |
|---|---|
| **Doel** | Wallets die vooral met een kleine vaste groep handelen |
| **Input** | volledige fill-historie met tegenpartij-identiteit (alleen mogelijk als fills on-chain staan) |
| **Formule** | aandeel van het volume met de top-$k$ tegenpartijen; entropie van de tegenpartij-verdeling |
| **Output** | concentratiescore |
| **Referentie** | Columbia (nov. 2025) op Polymarket: ~25% van het volume over drie jaar, piek ~60% in dec. 2024; sportmarkten ~45%, verkiezingen ~17% |
| **Valkuil** | Werkt alleen op markten die elke fill publiceren. Niet op CEX |
| **Status** | `SPEC` (on-chain haalbaar) |

### D23 — Cluster- en eigenaarschapssignalen
| | |
|---|---|
| **Doel** | Meerdere accounts, één eigenaar |
| **Input** | transactie-attributen, deposit-adreshergebruik, funding-patronen |
| **Formule** | heuristieken (multiple-input, deposit-address reuse, self-authorization) |
| **Output** | adresclusters |
| **Valkuil** | Heuristieken, geen bewijs. Precisie is beperkt; de literatuur noemt dit expliciet als open probleem |
| **Status** | `OPEN` |

### D25 — Cyclusdetectie via strongly connected components
| | |
|---|---|
| **Doel** | Accounts vinden die herhaald in kringetjes handelen, en bewijzen dat de groep netto op nul staat |
| **Input** | trades met **tegenpartij-identiteit** per token (dus on-chain DEX) |
| **Formule** | Formules §10: eq. (1)–(4), marge $v = m \cdot \overline{|V|}$ met $m = 0{,}01$ |
| **Output** | per SCC een gelabelde set wash trades + bedrag |
| **Referentie** | Victor & Weintraud (WWW '21): $159 mln op IDEX + EtherDelta; 31,54% resp. 42,12% van de tokens ooit gewasht |
| **Valkuil** | De kraan staat wijd open voor fout-positieven: kies de SCC-drempel (≥100 voorkomens) en de marge conservatief, en rapporteer het resultaat als **ondergrens**. Self-trades zijn ondubbelzinnig, twee-account-structuren niet |
| **Status** | `PROTO` — `scripts/d25_scc_wash.py`, pure standaardbibliotheek. Gedraaid op een 100 MB-slice van EtherDelta (342.305 trades, 10 feb – 26 aug 2017): **2.882 self-trades** (15.541 ETH) en **119 multi-account wash trades** in 43 sets (36× twee deelnemers, 6× drie, 1× vier). Let op: dit is een slice, geen representatieve meting |

---

## Cross-bron

### D26 — Gerapporteerd versus gemeten volume
| | |
|---|---|
| **Doel** | Het gat meten tussen wat een beurs **opgeeft** en wat er feitelijk **verhandeld** is |
| **Input** | (a) gerapporteerd 24u-volume per beurs uit een aggregator-API; (b) zelf gemeten volume uit de tick-stream van dezelfde beurs, dezelfde periode en **exact dezelfde pair-set** |
| **Formule** | $G_{i,t} = \dfrac{V^{\text{claim}}_{i,t} - V^{\text{meten}}_{i,t}}{V^{\text{claim}}_{i,t}}$, plus een rollend gemiddelde over $n$ dagen |
| **Output** | gatpercentage per beurs per dag, met het teken als richting |
| **Referentie** | Bitwise (2019) vergeleek het door CoinMarketCap gerapporteerde volume met eigen metingen → ~95% op niet-gereguleerde beurzen. Kaiko: Binance 64,3% van het volume tegen 30,7% van de diepte |
| **Valkuil** | Drie manieren om jezelf voor de gek te houden: (1) aggregator-volume is meestal een som over pairs die jij níet meet → alleen vergelijken op dezelfde pair-set; (2) elk gat in je eigen collector ziet eruit als nepvolume → koppel dit aan het gatenlog; (3) tijdzone- en afrondingsverschillen |
| **Interpretatie** | $G > 0$: de beurs claimt meer dan je zelf zag — het interessante geval. $G < 0$: jij hebt minder gemeten dan de beurs claimde, wat meestal een **collectorprobleem** is, geen beursprobleem |
| **Status** | `SPEC` — vereist een eigen collector. Op historische data is de claim-kant niet meer te reconstrueren, want aggregators bewaren geen historie van hun ranglijsten |

> **Waarom dit een eigen detector is.** Dit is de enige detector die twee onafhankelijke bronnen vergelijkt in plaats van één bron te beoordelen. En het is de enige die meet wat de *markt wijsgemaakt wordt*, niet wat er in het boek gebeurt. Zie [07-datalaag.md](07-datalaag.md) §2.

---

## Samengesteld

### D24 — Gecombineerde risicoscore
| | |
|---|---|
| **Doel** | Meerdere signalen wegen tot één score |
| **Input** | uitkomsten van D01–D26 die op jouw tier beschikbaar zijn |
| **Formule** | gewogen som, gewichten gekalibreerd op de synthetische benchmark |
| **Output** | score 0–100 met **benoemde onzekerheid** |
| **Valkuil** | Een samengestelde score verbergt welke detector hem drijft. Altijd de bijdragen per detector tonen (vergelijk hoe Vultax zijn "Vi IQ" presenteert: domeinscores naast het totaal) |
| **Status** | `OPEN` — pas zinvol als D01–D23 op de benchmark gescoord zijn |

---

## Prioritering

| Prioriteit | Detectoren | Waarom |
|---|---|---|
| 1 | D13, D20, D22, D25, D26 | Meest direct bewijs van het eigenlijke probleem, en meetbaar op data die bestaat |
| 2 | D01, D02, D03, D04 | T0, dus iedereen kan ze draaien; goed voor de eerste release |
| 3 | D07, D09, D10, D18 | Vorm van de verdeling; vereist tick-data |
| 4 | D11, D12, D08, D21 | Zwakke detectoren; alleen als onderdeel van D24 |
| 5 | D14–D17, D19, D23 | Vereisen data die de meeste gebruikers niet hebben |

**Belangrijk:** prioriteit 1 is niet "het makkelijkst", maar "het meest de moeite waard".
Prioriteit 2 is wat het snelst bruikbaar is voor buitenstaanders. Die twee lopen niet
gelijk, en dat is een bewuste keuze die in [05-roadmap.md](05-roadmap.md) wordt uitgewerkt.
