# Wash trading & nepvolume — alle formules op een rij

Verzameling van de wiskundige formules achter wash-trading-detectie en fake-volume-analyse.
Per formule staat de **bron** vermeld. Formules zonder bronaanduiding zijn standaard
marktdata-identiteiten (geen specifieke paper).

> **Lees dit eerst:** geen van deze formules bewijst opzettelijke manipulatie. Ze meten of
> gerapporteerd volume zich statistisch gedraagt zoals echte handel. Dat is een
> waarschijnlijkheidsuitspraak, geen identificatie van een dader.

---

## 0. Notatie

| Symbool | Betekenis |
|---|---|
| $P_t, V_t$ | prijs en volume in periode $t$ |
| $O_t, H_t, L_t, C_t$ | open, high, low, close van candle $t$ |
| $r_t$ | rendement, $r_t = \ln(C_t / C_{t-1})$ |
| $T_n$ | trader-/account-ID $n$ |
| $L_k$ | order $k$ |
| $\delta$ | tolerantievector $\delta = [\delta_p, \delta_t, \delta_v]$ (prijs, tijd, volume) |
| $n$ | lookback-lengte |
| $A, B, M$ | best ask, best bid, mid $M = (A+B)/2$ |
| $q(p)$ | rustend volume op prijsniveau $p$ |

---

## 1. Definitie: wanneer is iets een wash trade?

### 1.1 Order-representatie met teken
**Bron:** Cao, Li, Coleman, Belatreche & McGinnity, *Detecting Wash Trade in Financial
Market Using Digraphs and Dynamic Programming*, IEEE TNNLS (2015), eq. (1).

Een order is een tuple; verkoop krijgt een negatief teken op trader én volume:

$$\text{Order} = (T_n,\ \text{type},\ P_k,\ \pm V_k)$$

$$\text{Verkooporder} = (-T_n,\ P_k,\ -V_k)$$

Een positie is de som van opeenvolgende orders:

$$\text{Position} = \{(\text{Order}_1), (\text{Order}_2), \dots, (\text{Order}_n)\}$$

### 1.2 De wash-conditie
**Bron:** Cao et al. (2015), eq. (2) en de bijbehorende slotalert.

Een verzameling orders vormt een wash trade als de gesigneerde trader-ID's **en** de
gesigneerde volumes tegen elkaar wegvallen:

$$\sum_{k \in S} \text{OrderPair}_k = \left(\text{"0"},\ P_T \pm \delta_{Tp},\ \pm\delta_v\right)$$

Concreet: de collusiegroep staat netto op nul → geen effectieve eigendomsoverdracht.
De marge $\delta_{Tp}$ is de transactiemarge, $\delta_v$ het niet-gematchte restvolume
(manipulatoren laten bewust 1–2 % ongematcht om niet op te vallen).

### 1.3 De drie matching-condities
**Bron:** Cao et al. (2015), eq. (3), (4), (5).

Voor een buy-order $K$ die matcht met $K-1$ sell-orders $1 \dots K-1$:

**(3) Krappe tijdsintervallen**

$$\left| t_1 - t_K \right| < \delta_t$$

**(4) Uitvoerbare, kleine prijsverschillen**

$$P_K - \min(P_1, \dots, P_{K-1}) < \delta_p$$

**(5) Grotendeels gematchte volumes**

$$\left| \sum_{k=1}^{K-1} V_k - V_K \right| \le \delta_v$$

Praktisch betekent (5): het restpercentage

$$\text{restvolume} = \frac{\left| V_K - \sum_{k=1}^{K-1} V_k \right|}{\sum_{k=1}^{K-1} V_k} \times 100\%$$

moet klein zijn (in de voorbeelden van de paper ~1 %).

### 1.4 Gesloten transactiecyclus
**Bron:** Cao et al. (2015), Feature 2.

Enkel gematchte orders zijn nog geen wash trade. Pas als de uitvoeringen een **gesloten
cyclus** over de traders vormen, is de positie van de hele groep onveranderd:

$$\text{cyclus}: T_1 \to T_2 \to \dots \to T_m \to T_1$$

met per stap één richting (met de klok mee of tegen de klok in), zodat elke trader de
"parcel" doorgeeft en niemand netto iets overhoudt.

---

## 2. Account-niveau: de wash score

**Bron:** Imisiker & Tas, *Wash Trades as a Stock Market Manipulation Tool*, Journal of
Behavioral and Experimental Finance (2018), eq. (1).

$$\text{WashScore}_{i,j} = \frac{\text{aantal wash trades van account } j \text{ in aandeel } i}{\text{totaal aantal trades van account } j \text{ in aandeel } i}$$

Dus een percentage tussen 0 en 1. Hun dataset (Istanbul Stock Exchange, 9.999.582
account×aandeel-combinaties): in 97.398 gevallen (1 %) kwam minstens één wash trade voor,
met een gemiddelde wash score van **0,042** bij de niet-nul gevallen.

### 2.1 Winst-regressie
**Bron:** Imisiker & Tas (2018), eq. (2).

$$R_{\text{stock}(i),\text{account}(j)} = \beta_0 + \sum_{k=1}^{n} \beta_k \cdot \text{WashScore}(k)_{\text{stock}(i),\text{account}(j)} + \Theta_S + \varepsilon_{\text{stock}(i),\text{account}(j)}$$

waarbij $\text{WashScore}(k)$ dummievariabelen zijn per deciel, en $\Theta_S$ vaste effecten
per aandeel. Bevinding: tot ~10 % wash trades is het meest winstgevend (0,5 % maandelijkse
excess return); boven ~30 % wordt het effect insignificant — te veel nepvolume kost meer
aan transactiekosten dan het aan aandacht oplevert.

---

## 3. Statistische detectie op trade-niveau

Deze tests kijken of de *vorm* van de trade-verdeling op echte handel lijkt. Ze zijn de kern
van Cong, Li, Tang & Yang (*Crypto Wash Trading*, NBER Working Paper 30783, later
*Management Science*), die >70 % wash trading vond op ongereguleerde venues.

> **Beperking tot CEX.** Victor & Weintraud (WWW '21, §4.3) vonden dat de trade-size-
> verdelingen op DEX juist **normaal** gedrag vertonen (lokale pieken op ronde getallen,
> dalende frequentie bij grotere bedragen). Zij noemen deze verdelingen *"likely unsuitable
> as an indicator for wash trading on DEX"*. §3.1–§3.4 zijn dus **CEX-gereedschap**; pas ze
> niet toe op DEX-data zonder die waarschuwing. Voor kwantificering zie §11.

### 3.1 Eerste-cijfer-verdeling (Benford)
Echte transactiegroottes volgen bij benadering de wet van Benford; gegenereerde groottes vaak
niet.

$$P(d) = \log_{10}\!\left(1 + \frac{1}{d}\right), \qquad d \in \{1, 2, \dots, 9\}$$

Toets met Pearson-$\chi^2$:

$$\chi^2 = \sum_{d=1}^{9} \frac{\left(O_d - N \cdot P(d)\right)^2}{N \cdot P(d)}$$

met $O_d$ = waargenomen aantal trades met eerste cijfer $d$, $N$ = totaal aantal trades.
Vrijheidsgraden $= 8$. Grote $\chi^2$ → verwerp "organisch".

### 3.2 Roundness-ratio (ronde getallen)
Bots handelen in ronde eenheden (10, 100, 1000). Definieer $k$ = aantal trailing nullen:

$$R_k = \frac{\#\{ \text{trades} : V \equiv 0 \pmod{10^{k}} \}}{N}$$

Vergelijk met dezelfde ratio op een gereguleerde referentievenue. Een sterke verhoging van
$R_1$ en $R_2$ is een klassiek artefact van geautomatiseerde wash trading.

> **Let op het teken.** Falk, Tsoukalas & Zhang (2026, Research Policy) vinden op drie
> NFT-marktplaatsen het omgekeerde: **legitieme** trades clusteren daar *méér* rond ronde
> getallen dan wash trades ("legitimate trades exhibit slightly more clustering around round
> numbers"). Hetzelfde geldt voor Benford in §3.1: legitieme trades wijken daar *méér* af.
> De richting van dit signaal is dus niet universeel. Gebruik §3.1 en §3.2 alleen binnen één
> venue en één asset-klasse, en nooit als vergelijking tussen markten.

### 3.2b Wat dit betekent voor de catalogus
D07 (roundness) en D08 (Benford) zijn daarmee niet alleen "zwak op DEX", ze kunnen op sommige
markten de **verkeerde kant** op wijzen. Dat is een zwaardere fout dan een gemiste detectie:
je markeert dan de eerlijkste handel. Zie `02-detectoren.md`, D07 en D08.

### 3.3 Uniformiteit van trade-groottes
Te *weinig* spreiding is verdacht (mensen en instituten variëren nu eenmaal).

$$\text{CV} = \frac{\sigma_V}{\mu_V}$$

Met de mediaan als robuuste variant:

$$\text{rCV} = \frac{\text{MAD}(V)}{\text{mediaan}(V)}, \qquad \text{MAD}(V) = \text{mediaan}\left(\left|V_i - \text{mediaan}(V)\right|\right)$$

### 3.4 Staartverdeling / power law
In een echte markt volgen de grootste trades bij benadering een power law:

$$P(V > x) \sim x^{-\alpha}$$

Hill-schatter voor de staartindex:

$$\hat{\alpha} = \left[ \frac{1}{n} \sum_{i=1}^{n} \ln\!\left(\frac{V_{(i)}}{V_{(n+1)}}\right) \right]^{-1}$$

met $V_{(1)} \ge V_{(2)} \ge \dots$ de aflopend gesorteerde groottes. Een ontbrekende
staart (te weinig écht grote trades) wijst op volume dat niet door kapitaal gedragen wordt.

---

## 4. Prijs-volume-relatie

Dit is het deel dat **wél** op een chart te berekenen is.

### 4.1 Pearson-correlatie tussen beweging en volume
**Bron:** Bitcenter Research (2023) — gebruikte dit om Phemex te identificeren.

$$\rho = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

met $x_i = |r_i|$ (absolute move) en $y_i = V_i$.

Echt: $\rho$ duidelijk positief. Nep: $\rho \approx 0$ — volume dat verschijnt terwijl de
prijs stilstaat. Bitcenter vond voor Phemex de laagste correlatie van zeven exchanges en
schatte het echte volume op **5–25 %** van het gerapporteerde.

### 4.2 Volume per bewegingseenheid
Hoeveel volume is er nodig geweest voor de beweging die je ziet?

$$E_t = \frac{V_t}{\left| r_t \right| + \epsilon}, \qquad \epsilon \to 0^{+}$$

of op range-basis (Wyckoff "effort vs. result"):

$$V\!R_t = \frac{V_t}{H_t - L_t}$$

Extreem hoge $E_t$ of $V\!R_t$ = veel moeite, weinig resultaat = absorptie óf nepvolume.
Extreem lage waarde = beweging op dun volume (kwetsbaar).

### 4.3 Volume z-score (uitbijter-detectie)
$$\mu_V = \frac{1}{n}\sum_{i=1}^{n} V_{t-i}, \qquad \sigma_V = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}\left(V_{t-i} - \mu_V\right)^2}$$

$$z_t = \frac{V_t - \mu_V}{\sigma_V}$$

Robuuste variant met mediaan en MAD (beter bestand tegen de uitbijters zelf):

$$z^{\text{rob}}_t = \frac{V_t - \text{mediaan}(V)}{1{,}4826 \cdot \text{MAD}(V)}$$

### 4.4 Prijsimpact per eenheid volume (Kyle's lambda)
$$\Delta p_t = \lambda \cdot \text{OF}_t + \varepsilon_t$$

met $\text{OF}_t$ = gesigneerd orderflow-volume (buy − sell). Hoge $\lambda$ = dun boek.
Een venue met veel gerapporteerd volume maar lage $\lambda$ is verdacht: veel handel, geen
prijsimpact.

### 4.5 Amihud-illiquiditeit
$$\text{ILLIQ}_t = \frac{\left| r_t \right|}{DVOL_t}$$

(gemiddeld over $D$ periodes: $\text{ILLIQ} = \frac{1}{D}\sum_{t} \frac{|r_t|}{DVOL_t}$.)

### 4.6 Sessieprofiel-afwijking
Echt volume heeft een uurprofiel (Aziatisch/EU/US). Meet per uur $h$ de afwijking van het
eigen historische patroon:

$$d_h = \frac{V_h - \hat{V}_h}{\hat{\sigma}_h}$$

met $\hat{V}_h$ = historisch gemiddelde voor dat uur. Volume dat vlak is over alle uren, of
piekt om 04:00 UTC zonder nieuws, wijkt af.

### 4.7 Nul-volume-detectie
**Bron:** Bitwise Asset Management (SEC-memo, 2019) noemt "multiple hours (and days) with zero
volume" expliciet als signaal.

$$\text{nulRatio} = \frac{\#\{ t : V_t = 0 \}}{n}$$

Meerdere uren exact nul, terwijl de uren ervoor volume hadden, suggereert dat het volume
ervoor niet echt was. Echte markten hebben vrijwel nooit exact nul.

### 4.8 Volume-intensiteit (VI)
Hoeveel volume is dit vergeleken met wat normaal is op dit moment? Dit is **niet** hetzelfde
als $V\!R$ uit §4.2: dat zet volume tegen *prijsrange*, dit zet volume tegen *zichzelf in het
verleden*.

$$VI_t = \frac{V_t}{\text{mediaan}(V_{\text{baseline}})}$$

$VI_t = 1$ is normaal, $VI_t > 1$ is meer dan normaal. De mediaan, niet het gemiddelde: één
uitschieter mag de basislijn niet verschuiven.

**Keuze van de basislijn.** Niet "mediaan van dezelfde weekdag op hetzelfde uur" alleen: bij
28 dagen levert dat vier observaties per bucket, en een mediaan van vier is niet robuust.
Neem de mediaan over **alle** dagen in het venster binnen dat uur, en toets daarna of er een
weekdagfactor is. Is die er, corrigeer dan met een factor $\phi_{\text{dag}}$ per weekdag.
Venster: standaard 28 dagen, minimum 14, uitbreidbaar naar 56 (zie `02-detectoren.md`, D05).

**Niet dubbel normaliseren.** Wie $VI$ al door de basislijn heeft gedeeld, hoeft dat in de
detectorscore niet nog eens te doen: $\text{mediaan}(VI_{\text{baseline}}) \approx 1$ per
constructie, dus een extra deling verandert niets en suggereert ten onrechte een tweede
correctie.

---

## 5. Liquiditeit vs. volume

Kernpunt uit de Kaiko-data: volume is *wat al gebeurd is*, diepte is *wat nu kan zonder de
prijs te bewegen*. Binance: 64,3 % van het volume maar 30,7 % van de diepte.

### 5.1 Quoted spread (relatief)
$$S = \frac{A - B}{M}, \qquad M = \frac{A + B}{2}$$

in basispunten: $S_{\text{bp}} = 10\,000 \cdot \frac{A-B}{M}$.

### 5.2 Diepte binnen een band
$$D(\varepsilon) = \sum_{p \in [M(1-\varepsilon),\, M]} q_{\text{bid}}(p) \;+\; \sum_{p \in [M,\, M(1+\varepsilon)]} q_{\text{ask}}(p)$$

Gebruikelijke banden: $\varepsilon \in \{0{,}1\%,\ 1\%,\ 2\%\}$.

### 5.3 Diepte/volume-ratio (de belangrijkste publieke check)
$$\kappa = \frac{D(\varepsilon)}{V_{\text{dag}}}$$

Groot $\kappa$-gat tussen venues op hetzelfde pair = één van hen rapporteert volume dat het
boek niet kan dragen.

### 5.4 Effectieve spread / gerealiseerde slippage
$$\text{slippage}_{\text{bp}} = 10\,000 \cdot \frac{\text{VWAP}_{\text{fill}} - M_{\text{beslissing}}}{M_{\text{beslissing}}}$$

(teken omdraaien voor verkoop). Dit is de enige meting op *jouw* ordergrootte.

### 5.5 Diepte-herstel (resilience)
$$t_{\text{refill}}(x) = \min\left\{ \tau : D_{t+\tau}(\varepsilon) \ge x \cdot D_{t^-}(\varepsilon) \right\}$$

Meestal $x = 0{,}9$. Snel herstel = echte market makers; traag of nooit = het boek was op.

---

## 6. Benchmarks: hoe nepvolume een "eerlijke" prijs vergiftigt

**Bron:** Coin Metrics *Prices Methodology* v1.0 (in deze workspace: `coin-metrics-prices-methodology.md`).

### 6.1 VWAP
$$\text{VWAP} = \frac{\sum_{i=1}^{n} P_i Q_i}{\sum_{i=1}^{n} Q_i}$$

Zwak punt: één enorme nep-print verschuift VWAP direct. Daarom gebruiken benchmarks een
mediaan in plaats van een gemiddelde.

### 6.2 Volume-weighted median (VWM)
Sorteer de trades op prijs en neem de prijs waarbij het cumulatieve volume 50 % passeert:

$$\text{VWM} = P_{k^{*}}, \qquad k^{*} = \min\left\{ k : \sum_{i=1}^{k} Q_{(i)} \ge \frac{1}{2}\sum_{i=1}^{n} Q_{(i)} \right\}$$

Veel robuuster tegen wash trading dan VWAP: nepvolume aan de randen verandert de mediaan niet.

### 6.3 TWAP
$$\text{TWAP} = \frac{1}{T}\int_{0}^{T} P(t)\,dt \;\;\approx\;\; \frac{1}{n}\sum_{i=1}^{n} P_i$$

Negeert volume volledig → immuun voor volume-manipulatie, maar ook blind voor liquiditeit.

### 6.4 Inverse-variantie-gewogen mediaan
Coin Metrics weegt elke bron met $1/\sigma_i^2$ en neemt daarvan de gewogen mediaan:

$$w_i = \frac{1/\sigma_i^{2}}{\sum_{j} 1/\sigma_j^{2}}$$

Venues met een stabiele, smalle prijsreeks (doorgaans de gereguleerde) krijgen zo automatisch
meer gewicht.

---

## 7. Chart-indicatoren (OHLCV-only)

Deze zijn in TradingView te berekenen; de rest van dit document niet.

### 7.1 OBV
$$\text{OBV}_t = \text{OBV}_{t-1} + \operatorname{sgn}(C_t - C_{t-1}) \cdot V_t$$

### 7.2 Chaikin Money Flow
$$\text{MFM}_t = \frac{(C_t - L_t) - (H_t - C_t)}{H_t - L_t}, \qquad \text{CMF}_n = \frac{\sum_{i=1}^{n} \text{MFM}_{t-i+1} \cdot V_{t-i+1}}{\sum_{i=1}^{n} V_{t-i+1}}$$

### 7.3 Money Flow Index
$$\text{TP}_t = \frac{H_t + L_t + C_t}{3}, \qquad \text{MF}_t = \text{TP}_t \cdot V_t$$

$$\text{MR} = \frac{\sum \text{MF}_t \,[\text{TP}_t > \text{TP}_{t-1}]}{\sum \text{MF}_t \,[\text{TP}_t < \text{TP}_{t-1}]}, \qquad \text{MFI} = 100 - \frac{100}{1 + \text{MR}}$$

### 7.4 Volume Price Trend
$$\text{VPT}_t = \text{VPT}_{t-1} + V_t \cdot \frac{C_t - C_{t-1}}{C_{t-1}}$$

### 7.5 Roeptoets: "nepvolume-verdachtheid" per candle
Een eenvoudige samengestelde score uit de bovenstaande, alle termen genormaliseerd naar
$[0,1]$:

$$W_t = w_1 \cdot \mathbb{1}\!\left[z_t > 3\right] + w_2 \cdot \left(1 - \frac{|r_t|}{\overline{|r|}}\right) + w_3 \cdot \mathbb{1}\!\left[V_t = 0\right] + w_4 \cdot \left| d_h \right|$$

met $\sum w_i = 1$. Dit is een **heuristiek**, geen model uit de literatuur — de gewichten
moet je zelf kalibreren op een markt waarvan je weet dat ze schoon is.

---

## 8. Wat géén enkele formule kan

| Vraag | Formule? | Waarom niet |
|---|---|---|
| Is dit wash trading of gewoon een actieve bot? | ❌ | Zelfde statistische voetafdruk |
| Wie deed het? | ❌ | Geen accountdata in publieke feeds |
| Was het met opzet? | ❌ | Intentie staat in geen enkele dataset |
| Hoeveel % van het volume is nep? | ⚠️ | Alleen als *schatting* met een expliciete aanname |

Elke paper in dit veld zegt dit zelf ook. Wie één exact percentage noemt zonder steekproef,
periode en definitie te noemen, overdrijft wat het onderzoek ondersteunt.

---

## 9. Bronnenlijst met kanttekening

| Bron | Type | Betrouwbaarheid |
|---|---|---|
| Cao et al., IEEE TNNLS 2015 | peer-reviewed | Hoog — maar vereist order-/accountdata |
| Imisiker & Tas, JBEF 2018 | peer-reviewed | Hoog — vereist accountdata, één beurs |
| Cong, Li, Tang & Yang (NBER 30783) | working paper → Management Science | Hoog — de standaardreferentie |
| Bitwise (SEC-memo 2019) | primaire bron, belanghebbende partij | Cijfers bruikbaar, maar Bitwise had commercieel belang bij een lage uitkomst |
| Coin Metrics Prices Methodology | primaire methodologie | Hoog — transparant en herleidbaar |
| Kaiko liquiditeitsdata | commerciële dataleverancier | Hoog voor diepte; steekproef/periodes benoemen |
| Forbes / Javier Paz 2022 | journalistiek | 51 % over 157 exchanges; origineel hier niet in te zien (paywall) |
| Cointelegraph, CoinJar, Investopedia | journalistiek/uitleg | Goed als samenvatting, niet als bewijs |
| Bitcenter Research (Medium), Finage, Marcio Rosa, Vultax | commercieel / blog | Methodes bruikbaar als idee; verkoopt vaak het product dat het aanprijst |
| Victor & Weintraud, WWW '21 | peer-reviewed, data + code publiek | **Hoog.** Enige methode met gelabeld resultaat per account op publieke data |
| Cong et al., NBER 30783 (volledig) | working paper | **Hoog.** De standaardreferentie; 448 mln transacties over 29 beurzen |

---

## 10. Cyclusdetectie met strongly connected components (DEX)

**Bron:** Victor & Weintraud, *Detecting and Quantifying Wash Trading on Decentralized
Cryptocurrency Exchanges*, WWW '21, pp. 23–32, DOI 10.1145/3442381.3449824.
Data: Zenodo `4540223`. Code: GitHub `friedhelmvictor/lob-dex-wash-trading-paper`.

De enige methode in dit document die op **publieke** data tot een gelabeld resultaat per
account komt, omdat elke DEX-trade on-chain staat met de betrokken adressen.

### 10.1 Een trade als gesigneerd paar
**Bron:** eq. (1). Trader $a_j$ verkoopt volume $V$ aan trader $a_i$:

$$T = (+a_i,\ -a_j)\,V$$

### 10.2 Positieverandering over meerdere trades
**Bron:** eq. (2). Kopers en verkopers worden apart opgeteld; het teken gaat naar het volume:

$$\sum_{k=1}^{n} T_k = (+a_i, -a_j)V_1 + (+a_j, -a_i)V_2 = \{[a_i]\,V_1 - V_2,\ [a_j]\,-V_1 + V_2\} = \{[a_i]\,p_i,\ [a_j]\,p_j\} = P$$

### 10.3 De wash-conditie
**Bron:** eq. (3). Er moet een deelverzameling $S_W \subseteq S_T$ bestaan zodat elke
deelnemer netto op nul staat:

$$S_W = \sum_{T_k \in S_W} (+a_i, -a_j)\,V_k = \{[a_i]\,p_i, \dots, [a_j]\,p_j\} = \{[a_i]\,0 \pm v, \dots, [a_j]\,0 \pm v\}$$

### 10.4 De marge
**Bron:** eq. (4). Exacte gelijkheid is onrealistisch: handelaren matchen bewust niet
perfect, en kosten knabbelen aan het kapitaal. Daarom een marge $m$ op het gemiddelde
trade-volume:

$$v = m \cdot \frac{\sum_{T_k \in S_W} |V_k|}{|S_W|}, \qquad m = 0{,}01$$

### 10.5 Waarom niet alle subsets
Cao et al. toetsen de machtsverzameling → $O(2^n)$, onbruikbaar bij honderdduizenden trades.
Victor & Weintraud doen twee dingen:

1. **Kandidaatverzamelingen** via herhaald tellen van strongly connected components
   (algoritme 1). Een SCC is een maximale deelverzameling knopen waarin elk tweetal via
   gerichte paden bereikbaar is; elke SCC bevat minstens één cyclus.
2. **Volume matching** per SCC, per token, per tijdvenster, door iteratief de laatste trade
   te verwijderen (algoritme 2) — dus $n$ in plaats van $2^n$ toetsen.

Algoritme 1 in woorden: vereenvoudig de multigraaf (multi-edges → gewicht), bereken herhaald
alle SCC's en tel hoe vaak elke knoopverzameling voorkomt, verlaag daarna elk gewicht met 1
en verwijder gewicht-0-randen. Herhaal tot er geen randen meer zijn.

### 10.6 Parameters en resultaten
| Parameter | Waarde |
|---|---|
| SCC-voorkomen als kandidaat | ≥ 100 keer |
| Marge $m$ | 1 % |
| Tijdvensters | 1 uur, 1 dag, 1 week (drie passes) |

| | IDEX | EtherDelta |
|---|---|---|
| Wash trades | 213.029 (3,99 % van alle trades) | 69.711 (1,30 %) |
| Waarvan self-trades | 28.193 | 58.791 |
| Wash-volume | $83,5 mln | $75,8 mln |
| Tokens ooit gewasht | 31,54 % | 42,12 % |
| Tokens vrijwel volledig gewasht | <1 % | ~10 % |
| Betaalde wash-fees | $250.594 | $227.540 |

Totaal **$159 mln** — een **ondergrens**, want de parameters zijn conservatief gekozen.

### 10.7 Waarschuwing voor onze eigen catalogus
**Bron:** §4.3. De trade-size-verdelingen op beide DEX vertonen lokale pieken op ronde
getallen en een dalende frequentie bij grotere bedragen — dus **normaal handelsgedrag**.
Gevolg: §3.1–§3.4 zijn CEX-gereedschap; zie de waarschuwing bij §3.

---

## 11. Volume schatten met de roundness-ratio

**Bron:** Cong, Li, Tang & Yang, *Crypto Wash Trading*, NBER Working Paper 30783 (dec. 2022),
§4.1–§4.2. Dit is hun **hoofdschatter** voor het aandeel nepvolume.

### 11.1 Idee
Echte menselijke trades hebben ronde groottes; bot-gegenereerd nepvolume is onafgerond. Het
aandeel onafgeronde trades boven de benchmarkratio is dan het nepvolume.

### 11.2 Benchmark-regressie
**Bron:** eq. (6), pooled over de gereguleerde beurzen, weekfrequentie:

$$\ln\left(\text{UnroundedVol}_{i,t}\right) = \alpha + \beta \ln\left(\text{RoundVol}_{i,t}\right) + \gamma X_{i,t} + \varepsilon_{i,t}$$

met $\text{UnroundedVol}$ en $\text{RoundVol}$ het volume in onafgeronde versus ronde
groottes, en $X$ optioneel beurskenmerken (leeftijd, rang, webverkeer, unieke bezoekers).
Het legitieme onafgeronde volume van een ongereguleerde beurs wordt met deze parameters
voorspeld; het overschot is wash volume:

$$\text{WashVol}_{i,t} = \max\left(0,\ \text{UnroundedVol}^{\text{obs}}_{i,t} - \widehat{\text{UnroundedVol}}_{i,t}\right)$$

### 11.3 Twee schatters, factor vijf verschil
| Schatter | Ongereguleerd | Tier-1 | Tier-2 | Gereguleerd |
|---|---|---|---|---|
| Roundness-ratio (hoofdschatter) | **77,5 %** (mediaan 79,1 %) | 53,4 % | 81,7 % | <5 % (kruisvalidatie) |
| Benford-contrafeitelijk | 16,3 % | 12,9 % | 18,5 % | 3,1 % afwijking |

De auteurs noemen de Benford-uitkomst zelf *"somewhat lower bounds"*: die wet ziet alleen het
eerste cijfer en mist nepvolume dat alle negen cijfers raakt.

**Praktische les:** gebruik de roundness-ratio om te *kwantificeren* en Benford alleen als
*robuustheidstoets*. Wie Benford als hoofdmaat neemt, onderschat met een factor vijf.

### 11.4 Wat de auteurs zelf toegeven
> "we do not claim that the detection tools will continue being as effective forever"

Zij zeggen expliciet dat wash traders van hun werk kunnen leren en dat de tests niet
uitputtend zijn. Elk model dat deze methoden gebruikt, hoort die zin over te nemen.

---

*Opgesteld op 2026-11-02. Formules uit §1–§2 zijn letterlijk uit de genoemde papers;
§3–§5 zijn standaard statistiek/liquiditeitsmaten zoals gebruikt in de genoemde studies;
§7.5 is een eigen heuristiek en géén publicatie; §10 en §11 zijn letterlijk uit Victor &
Weintraud (WWW '21) en Cong et al. (NBER 30783).*
