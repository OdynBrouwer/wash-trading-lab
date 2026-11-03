# 04 — Bronnen

Geannoteerde bibliografie. Per bron: wat erin staat, hoe betrouwbaar hij is, en of we
hem daadwerkelijk hebben.

## 1. De cijfers naast elkaar

| Bron | Steekproef | Uitkomst |
|---|---|---|
| Bitwise Asset Management (SEC-memo, 2019) | **81** exchanges | ~95% van het BTC-spotvolume op CoinMarketCap nep of niet-economisch. Letterlijk: *"approximately 95% of this volume is fake and/or non-economic in nature"* (regel 143). Van die 81 hebben er **10** echt volume |
| Forbes / Javier Paz (26 aug. 2022) | 157 exchanges | ~51%: $128 mrd gemeten tegen $262 mrd opgeteld (14 juni, **bitcoin**, niet alle crypto). De groep "weinig tot geen toezicht" — **Binance, MEXC Global én Bybit** — claimde $217 mrd tegen $89 mrd gemeten. De 95% in dit artikel is de korting op **één** beurs (BitCoke), niet een bereik voor kleine beurzen |
| Cong, Li, Tang & Yang (NBER w30783) | 29 centrale exchanges | >70% wash trading op **ongereguleerde** venues; gereguleerde venues gedroegen zich als conventionele markten |
| Kaiko — *The Crypto Liquidity Concentration Report* (7 sep. 2023) | top-8 venues | Binance 64,3% van het volume tegen 30,7% van de diepte; top-8 91,7% diepte tegen 89,5% volume |
| Kaiko — *72% of ETH Liquidity is Concentrated on 5 Exchanges* (29 mei 2023) | 5 venues | 72% van de ETH-diepte zit op Binance, Bitfinex, OKX, Coinbase en Kraken. **Kaiko meet geen nepvolume** — dit is een structuurvergelijking, geen oordeel |
| Bitcenter Research (8 juni 2023) | 7 exchanges | Phemex: echt volume 5–25% van gerapporteerd; laagste prijs-volume-correlatie van de zeven. **Sterk eigen belang:** Bitcenter is zelf een beurs en noemt een concurrent nep |
| Columbia-universiteit (6 nov. 2025) | Polymarket, 3 jaar | ~25% van het volume wash trading, piek ~60% in dec. 2024 (letterlijk in het abstract). De uitsplitsing **sport ~45%, verkiezingen ~17% is NIET bevestigd** — niet in het abstract, niet in de berichtgeving. Wat er wél staat: *"in some weeks, over 90% of trades in those categories appeared inauthentic"* |
| Pennec, Fiedler & Ante (Finance Research Letters, 2021) | 12 exchanges, webverkeer + klantfondsen | Wash-beurzen overdrijven hun volume met **factor 25–50**; gemengde beurzen met factor 1,25–33. Geen transactiedata: het is een vergelijking van gerapporteerd tegen voorspeld volume, gekalibreerd op de beurzen die wél klopten |
| Cong et al. — twee schatters vergeleken | 29 exchanges | Roundness-schatter **77,5%**; Benford-schatter **16,3%** — factor vijf verschil. Roundness is hun hoofdschatter |
| **Aloosh & Li (Management Science, 2024)** — *directe ground truth* | Mt. Gox, 26 juni 2011 – 20 mei 2013; 5.548.867 trades, 98.391 trader-IDs | **1,4%** van het BTC-volume en **2,1%** van de transacties, gepleegd door 2.887 IDs (2,93%). Die IDs zijn samen goed voor **32,5%** van het volume. Definitie: dezelfde trader-ID aan beide kanten → dit is een **ondergrens**. De auteurs verklaren het lage cijfer uit het ontbreken van concurrentie in die periode |
| Amiram, Lyandres & Rabetti (Management Science, 2025) | Kaiko-transactiedata, **41 beurzen**, juni 2013 – sep. 2019 (76 maanden) | Geen percentage maar een **verband**: hoe sterker de concurrentie op een pair, hoe méér nepvolume. +1 sd Herfindahl-concentratie ⇒ **0,1–0,2 sd minder** nepvolume. Beurzen die hun volume opblazen misleiden beleggers kort en worden op lange termijn gestraft. Dit is de bron die Aloosh & Li aanhalen om hun lage 1,4% te verklaren |
| Victor & Weintraud (WWW '21) | IDEX + EtherDelta, 2017–2020 | **$159 mln** wash-volume; 3,99% resp. 1,30% van alle trades; 31,54% resp. 42,12% van de tokens ooit gewasht; op EtherDelta ~10% van de tokens vrijwel volledig gewasht |
| Falk, Tsoukalas & Zhang (Research Policy, 2026) | 3 NFT-marktplaatsen, ~27,7 mln trades | **37,58%** van de trades en **60,08%** van de waarde wash. Let op: **NFT, geen CEX** — de spreiding is groot (LooksRare 95,68% van de waarde, OpenSea 26,39%) |
| Victor & Weintraud (WWW '21) | IDEX + EtherDelta, 2017–2020 | **$159 mln** wash-volume; 3,99% resp. 1,30% van alle trades; 31,54% resp. 42,12% van de tokens ooit gewasht; op EtherDelta ~10% van de tokens vrijwel volledig gewasht |
| Falk, Tsoukalas & Zhang (Research Policy, 2026) | 3 NFT-marktplaatsen, ~27,7 mln trades | **37,58%** van de trades en **60,08%** van de waarde wash. Let op: **NFT, geen CEX** — de spreiding is groot (LooksRare 95,68% van de waarde, OpenSea 26,39%) |

**Waarom 51% en 95% niet in tegenspraak zijn:** ze meten deels verschillende
grootheden (wash trading versus alle niet-economisch volume), over verschillende
steekproeven en periodes. De enige consistente bevinding over álle studies is het gat
tussen gereguleerde en ongereguleerde venues. Wie één percentage noemt zonder
steekproef en definitie, overdrijft wat het onderzoek ondersteunt.

## 2. Wat we in de workspace hebben

| Bestand | Bron | Type | Betrouwbaarheid |
|---|---|---|---|
| `Detecting_Wash_Trade_in_Financial_Mar_...md/.pdf` | Cao, Li, Coleman, Belatreche & McGinnity, *Detecting Wash Trade in Financial Market Using Digraphs and Dynamic Programming*, IEEE TNNLS **27**(11), 2351–2363 (2016) | peer-reviewed | **Hoog.** Formele definitie, matching-marges, gesloten cyclus. Vergt order-/accountdata |
| `Wash_trades_as_a_stock_market_manipul...md/.pdf` | Imisiker & Tas, *J. Behavioral and Experimental Finance* (2018) | peer-reviewed | **Hoog.** Wash score + winstregressie. Eén beurs (ISE) |
| `OASIcs.Tokenomics.2021.md/.pdf` | Cong, Li, Tang & Yang, *Detecting and Quantifying Crypto Wash Trading*, Tokenomics 2021, pp. **10:1–10:6** | proceedings, **6 pagina's** | **Hoog.** Dit is de uitgebreide proceedings-versie met tabel 1 (wash-percentage per beursregime), geen losse samenvatting. De volledige analyse staat in `w30783.md` |
| `w30783.md` | Cong, Li, Tang & Yang, *Crypto Wash Trading*, NBER Working Paper 30783 (dec. 2022) | working paper, **volledig** | **Hoog.** De standaardreferentie: 448.475.535 transacties, 29 beurzen, 3 gereguleerd. Let op: niet peer-reviewed op dit moment van schrijven |
| `Detecting and Quantifying Wash Trading.md/.pdf` | Victor & Weintraud, *Detecting and Quantifying Wash Trading on Decentralized Cryptocurrency Exchanges*, WWW '21 | peer-reviewed, **data + code publiek** | **Hoog.** Enige bron met gelabeld resultaat per account op publieke data. Data: Zenodo `4540223`; code: GitHub `friedhelmvictor/lob-dex-wash-trading-paper` |
| `ssrn-4649565.md` (PDF in `sources/`) | Falk, Tsoukalas & Zhang, *Detecting crypto wash trades via machine learning*, Research Policy (2026), SSRN 4649565 | peer-reviewed, **dataset publiek** | **Hoog.** Eerste bron met een *gelabelde* set op on-chain data (NFT-marktplaatsen + Mt. Gox) én een eerlijke vergelijking met de indirecte methoden. Beperking: NFT/DEX, geen CEX-spot. Dataset: Mendeley `4hyxfwzpgg` v2 (CC BY 4.0) |
| `aloosh-li-2024.md` (PDF in `sources/`) | Aloosh & Li, *Direct Evidence of Bitcoin Wash Trading*, Management Science **70**(12), 8875–8921 (2024). Gelezen versie: working paper van 28 aug. 2023, vrij beschikbaar via DORAS (Dublin City University) | peer-reviewed, **volledige tekst vrij** | **Hoog — de belangrijkste bron die we hebben.** Enige dataset met individuele transactieregisters van een echte beurs. Toetst de indirecte methoden tegen ground truth: Benford, clustering, lognormaliteit en structural breaks zijn nuttig; **de staartindex (power law) wijst de verkeerde kant op** |
| `amiram-2022.md` (PDF in `sources/`) | Amiram, Lyandres & Rabetti, *Competition and Product Quality: Fake Trading on Crypto Exchanges* (29 mei 2022), conferentieversie van wat in 2025 in Management Science verscheen als *Trading Volume Manipulation and Competition Among Centralized Crypto Exchanges*, **71**(10), 8604–8622 | peer-reviewed; gelezen versie is een **vrij toegankelijke conferentieversie** | **Hoog.** 41 beurzen via Kaiko, 76 maanden. Combineert drie maten (Benford, KS-afstand tot lognormaal, structurele breuken) via PCA, en valideert die tegen webpopulariteit, regelgevingsstatus, gemelde manipulatiezaken en de Chinese beursban van 2017. **Let op:** dit is de versie van 2022; de auteurs schreven toen al dat ze naar ~60 beurzen en juli 2021 wilden uitbreiden |
| `srnysearca201901-5164833-183434.md/.pdf` | Bitwise-presentatie aan de SEC (19 maart 2019), vastgelegd in een SEC-staffmemo van 20 maart 2019 (Lauren Yates, File No. SR-NYSEArca-2019-01) | primaire bron, **belanghebbende partij** | Cijfers bruikbaar, maar Bitwise had commercieel belang bij een lage marktkwaliteit. Let op de dubbelheid: de **memo** is van de SEC, de **inhoud** is van Bitwise |
| `coin-metrics-prices-methodology.md/.pdf` | Coin Metrics Prices Methodology v1.0 (2023) | primaire methodologie | **Hoog.** Transparant, herleidbaar |
| `Blockchain Transaction Data Analytics.../` | Springer, eds. Wu, Lin & Zheng (2025) | peer-reviewed boek | **Hoog** voor graafmethoden; bevat **geen** wash-trading-detectie |
| `Crypto_and_Decentralized_Finance_Unde...md/.pdf` | SpringerBriefs in Finance (2026) | peer-reviewed | **Hoog** voor risico's en aanvalstechnieken in DeFi |
| `ptc0518263585.md/.pdf` | Coinbase Derivatives, CFTC-certificering HYPE futures (2026) | primaire filing | **Hoog.** Nuttig als voorbeeld van manipulatiebestendige benchmark-opzet |
| `Trader_training_course_CSI_...md/.pdf` | CSI Global Education (2008) | lesmateriaal | Matig. Canadees rulebook-perspectief, verouderd |
| `Proceedings_of_International_Conferen_...md/.pdf` | ICAIN 2025 | proceedings | Bevat één terloopse vermelding; verder niet relevant |
| `Etika_Bisnis_dalam_Perspektif_Manajem...md/.pdf` | Indonesisch leerboek bedrijfsethiek | leerboek | Bevat één paragraaf over marktmanipulatie; niet bruikbaar als technische bron |
| `New Adventures of CryptoDad/` | Giancarlo (Wiley) | memoires/beleidsbetoog | **Kader**, geen detectie. Eén definitie van wash trading (regel 3950) |
| `加密貨幣之王/` | Roberts, *Kings of Crypto* (2021, Chinese vertaling) | journalistiek | Anekdotisch. Eén vermoeden van een concurrent (regel 1503) |
| `Cryptocurrency Trading & Investment Guide.../` | Lazar | self-published | **Onbetrouwbaar.** Bevat aantoonbaar onjuiste claims (regel 1242: DEX's zouden tegen wash trading beschermen) en rekenfouten |
| `Let Them Eat Crypto...pdf` | Howson, *Let Them Eat Crypto* (2023), 194 pp. | journalistiek/kritisch boek | **Kader**, geen detectie. Staat in `sources/` maar is **nooit geconverteerd of gelezen** — dus nooit geciteerd. Bewust buiten gebruik |
| `(2) X.pdf` | Screenshot van een post op X (@agintender, 30 maart), in het Chinees, over CEX-volume | sociale media, **geen document** | **Niet bruikbaar.** Eén pagina, geen verifieerbare bron, geen methode. Noemt bedragen (o.a. $3.610) en percentages (39%, 46%) voor Binance, OKX, Bitget en Gate.io zonder herkomst. Niet citeren |

### Wat er in hun dataset zit — en wat niet

De Mendeley-set is **geen trade-data maar een feature-tabel**. `gox_ml_samples.csv`
(940 MB, ~5,9 mln rijen) heeft 17 kolommen: `bitcoins`, `round_level`,
`buyer/seller_24h/7d_trade_count`, vier `btc_sum`-totalen, `price_deviation`,
`time_since_last_trade`, `hours`, `cumu_wash_percent_opt` en het label `wash`.
Geen wallet-ID, geen tijdstip, geen OHLCV. De NFT-bestanden (`Blur` 330 MB,
`LooksRare` 37 MB, `OpenSea` 2 GB) hebben dezelfde vorm.

Gevolg: **geen enkele D01–D06 kan hierop draaien.** Ze vragen allemaal een tijdreeks
van bars. Wat er wél kan is de vraag die ertoe doet: welke *soort* feature scheidt?

Gemeten met `scripts/probe_mendeley_features.py --mb 24` (150.000 rijen, 35,0% wash):

| Feature | Nodig | AUC |
|---|---|---|
| `seller_7d_trade_count` | accounthistorie (T3) | 0,740 |
| `seller_24h_trade_count` | accounthistorie (T3) | 0,714 |
| `buyer_7d_trade_count` | accounthistorie (T3) | 0,712 |
| `seller_all_btc_sum` | accounthistorie (T3) | 0,704 |
| `cumu_wash_percent_opt` | onduidelijk | 0,537 |
| `round_level` | **publieke bars (T0)** | 0,524 |
| `time_since_last_trade` | **publieke bars (T0)** | 0,505 |
| `price_deviation` | **publieke bars (T0)** | 0,501 |
| `hours` | **publieke bars (T0)** | 0,498 |
| `bitcoins` | **publieke bars (T0)** | 0,423 |

**Dit is het hardste bewijs dat we hebben voor de stelling dat T0 het symptoom meet.**
Op echte gelabelde Mt. Gox-data scoren álle features die je uit publieke bars kunt
halen op 0,50 — muntworp. De scheiding zit volledig in de tegenpartij-identiteit. Dat
is geen implementatiefout van ons; het is een eigenschap van de informatie.

Twee dingen die deze meting **niet** zegt: het is één prefix van 150.000 rijen
(waarschijnlijk aaneengesloten in tijd), en het zijn enkelvoudige features zonder
cross-validatie. Hun 0,97 komt uit een multivariate XGB met alles tegelijk.

Teruggetrokken verdenking: `cumu_wash_percent_opt` leek een label in vermomming, maar
scoort 0,54. Geen leakage.

## 3. Wat ontbreekt (en prioriteit heeft)

| # | Ontbrekend | Waarom belangrijk | Status |
|---|---|---|---|
| 1 | Victor & Weintraud, *Detecting and quantifying wash trading on DEX*, WWW 2021 | Enige echte wash-trading-detector voor DEX's | **GESLOTEN** — volledig gelezen, formules in §10, detector D25 |
| 2 | Cong et al., volledige NBER-versie (w30783) | De detectiemethodiek (Benford, roundness, staart) staat alleen in het volledige paper | **GESLOTEN** — volledig gelezen, roundness-regressie in §11 |
| 3 | Een gelabelde dataset met wash trades op CEX-spot | Bestaat niet publiek | `DEELS` — zes routes in [03-datalandschap.md](03-datalandschap.md) §6.1. **Wel beschikbaar:** een gelabelde **DEX/NFT**-set (Mendeley `4hyxfwzpgg` v2) plus een Mt. Gox-feature-tabel. Die tabel is een *feature*-set, geen tijdreeks, dus D01–D06 kunnen er niet op draaien — maar hij is bruikbaar als externe toets van wat T0-features opleveren (zie de tabel hierboven: 0,50) |
| 4 | Een publieke bron met orderboek-events inclusief cancels | Nodig voor F4 (spoofing) | `DEELS` — cancellaties zijn afleidbaar uit diepte-diffs, zie [03-datalandschap.md](03-datalandschap.md) §6.2 |
| 5 | Aloosh & Li (2024), *Direct Evidence of Bitcoin Wash Trading*, Management Science **70**(12), 8875–8921 | De enige directe CEX-achtige ground truth: gelekte Mt. Gox-data met individuele traders | **GESLOTEN** — volledig gelezen (84 pp.). Bevindingen in §1 en in [02-detectoren.md](02-detectoren.md) bij D07, D08 en D10. DOI `10.1287/mnsc.2021.01448`; vrije versie via [DORAS](https://doras.dcu.ie/32898/) |
| 6 | Amiram, Lyandres & Rabetti (2025), *Trading Volume Manipulation and Competition Among Centralized Crypto Exchanges*, Management Science **71**(10), 8604–8622 | **Dit is CEX**, dus precies onze scope | **GESLOTEN** — gelezen als de conferentieversie van 29 mei 2022 (78 pp., vrij via het Coller-archief van Tel Aviv University). Bevindingen in §1. DOI `10.1287/mnsc.2021.02903`; voorloper SSRN `10.2139/ssrn.3745617` |
| 7 | Pennec, Fiedler & Ante (2021), *Wash trading at cryptocurrency exchanges*, Finance Research Letters **43**, 101982 | **CEX, 12 beurzen**, en de enige bron die het volume van wash-beurzen kwantificeert (factor 25–50). Cijfer staat in §1; we hebben de tekst zelf niet | `TE LEZEN` — DOI `10.1016/j.frl.2021.101982` |

## 4. Webartikelen — met oordeel, datum en vindplaats

Sinds de broncontrole van november 2026 is van elke rij hieronder de primaire tekst
daadwerkelijk ingezien. Live-URL's van Forbes, Medium en SSRN geven 403 aan
geautomatiseerde clients; die zijn via de Wayback Machine gelezen.

| Bron | Oordeel | Vindplaats |
|---|---|---|
| Investopedia, *Wash Trading* | Degelijke uitleg en definitie; geen methode | investopedia.com |
| Vultax Research, *Crypto Wash Trading and Real Liquidity* | **Commercieel belang**: verkoopt de screens die het artikel aanprijst. Geeft zijn eigen beperkingen wel eerlijk toe. Cijfers alleen gebruiken met de oorspronkelijke bron erbij. Dit is ook hoe de Kaiko-cijfers dit project binnenkwamen — secundair | vultax.com/research |
| Finage, *How to Detect Fake Volume in Stock Markets* | Marketingblog voor een data-API. Methoden zijn gangbaar, geen onderbouwing | finage.co.uk |
| Marcio Rosa, *How to Spot Fake Volume on Small Exchanges* | Vijf praktische checks, geen bron, geen methode | medium.com |
| Bitcenter Research, *How to Estimate Fake Trading Volume on Cryptocurrency Exchanges?* (8 juni 2023) | Klein maar concreet: correlatiemethode met getallen. **Sterk eigen belang** — Bitcenter is zelf een beurs en noemt een concurrent nep. Niet peer-reviewed | medium.com/@servicewilliamson; Wayback 21 juni 2023 |
| CoinJar, *Defence against the dark arts* | Goede illustratie van het "nul-volume"-signaal van Bitwise; beursblog | coinjar.com |
| Forbes / Javier Paz, *More Than Half Of All Bitcoin Trades Are Fake* (26 aug. 2022) | Nu **wel** gelezen. Eigen "Real Volume"-studie, gekoppeld aan Forbes' eigen beursranglijst → commercieel belang. Methode: kortingspercentages op basis van vergunningen, SimilarWeb-verkeer en interviews — **geen** detectie op transactieniveau | Wayback 26-08-2022 22:28 UTC; herdruk forbesafrica.com 22-09-2022 |
| Kaiko, *The Crypto Liquidity Concentration Report* (7 sep. 2023) en *72% of ETH Liquidity is Concentrated on 5 Exchanges* (29 mei 2023) | Twee aparte publicaties met twee datums, geen één meting. Verkoopt marktdata; het rapport showcaset hun "Asset Liquidity Metrics". Meet **geen** nepvolume — het is diepte tegenover volume | kaiko.com/resources |
| Columbia, *Network-Based Detection of Wash Trading* (Sirolly, Ma, Kanoria & Sethi, 6 nov. 2025) | Universitair, **geen** commercieel belang. Enige bron hier die naar tegenpartijstructuur kijkt (gesloten clusters). Niet peer-reviewed, 82 pp. | SSRN `10.2139/ssrn.5714122`; pers via Bloomberg en CoinDesk 7 nov. 2025 |
| Cointelegraph (2 sep. 2022) | Journalistieke samenvatting van het Forbes-onderzoek. **Maakt van de Columbia-piek "July 2024"** terwijl het abstract december 2024 zegt — tweedehands dus onbetrouwbaar op details | cointelegraph.com |
| WSJ, *Most Bitcoin Trading Faked by Unregulated Exchanges, Study Finds* (19 feb. 2019) | **Niet gelezen** — paywall. Let op: dit is de **Bitwise**-berichtgeving uit 2019, niet het Forbes-onderzoek uit 2022; die twee worden vaak verwisseld | wsj.com |

## 5. Themapublicaties die het kader geven

| Bron | Wat het regelt |
|---|---|
| Verordening (EU) 2023/1114 (**MiCAR**) | Verbiedt marktmanipulatie in crypto-activa en verplicht handelsplatformen tot detectie en preventie; van toepassing sinds 30 december 2024 |
| CME **Rule 575** (overgenomen door de CFTC) | Maakt vooraf afgestemde orders (wash/matched trades) expliciet verboden |
| CFTC-advies prediction markets (25 feb. 2026) | Noemt wash sales en vooraf afgestemde handel expliciet als te handhaven gedrag |
| DOJ-aanklachten (okt. 2024: 18 personen/entiteiten na een door de FBI gemaakte token; maart 2026: 10 personen, gelinkt aan Gotbit, Vortex, Antier en Contrarian) | Bewijs dat volume-for-hire daadwerkelijk verkocht wordt. **Let op:** dit zijn aantijgingen tot bewezen; de maart 2026-zaak kennen we alleen uit tweedehandse berichtgeving |

## 6. Citeerregels voor dit project

1. Elk getal krijgt: bron, steekproef, periode, en definitie van "nep".
2. Onderscheid expliciet tussen **letterlijk uit de bron** en **eigen reconstructie**.
   In [`washtrading-formules.md`](washtrading-formules.md) staat dat per sectie aangegeven.
3. Commerciële belangen benoemen, ook als de cijfers kloppen.
4. Wat niet gelezen is, wordt niet geciteerd. "Niet gelezen" is een geldige status.
5. Geen tweedehandse citaten van tweedehandse citaten. Als Cointelegraph Forbes
   samenvat, citeren we Cointelegraph *over* Forbes, niet Forbes.
6. Elk cijfer in §1 is **letterlijk in de tekst van de bron** teruggezocht, niet uit een
   samenvatting overgenomen. Staat er een cijfer waarvan we de herkomst niet kunnen
   aanwijzen, dan gaat het eruit of krijgt het "niet bevestigd" én de vindplaats erbij.

## 7. Broncontrole van 3 november 2026

Alle bronnen zijn één keer systematisch langsgelopen. Wat er is gebeurd:

| Wat | Hoe | Uitkomst |
|---|---|---|
| Metadata (auteur, jaar, tijdschrift, DOI, volume, pagina's) | Crossref-API per DOI, OpenAlex en Semantic Scholar als aanvulling | 5 van de 6 academici klopten. **Cao et al. stond op 2015; het is 2016** (TNNLS 27(11), 2351–2363) |
| Cijfers in §1 | Patroongewricht teruggezocht in onze eigen tekstconversies | Alles bevestigd bij Cong, Victor & Weintraud en Falk et al. Bitwise: **95% klopt, "83 exchanges" niet** (het zijn er 81) |
| Commerciële en journalistieke cijfers zonder bestand | Wayback Machine, OpenAlex, Semantic Scholar | Forbes/Paz, Kaiko (2 rapporten), Bitcenter (8 juni 2023) en Columbia (SSRN) gecontroleerd. Drie formuleringen gecorrigeerd; één uitsplitsing **niet bevestigd** |
| Losse bestanden in `sources/` | Inventaris vergeleken met deze index | Twee bestanden stonden nergens: Howson (nooit gelezen) en een screenshot van een X-post (niet bruikbaar) |
| Nieuwe bron gevonden | Crossref-zoekopdracht op "wash trading centralized exchange" | Pennec, Fiedler & Ante (2021), Finance Research Letters — CEX, 12 beurzen, factor 25–50. Opgenomen in §1 en §3 |
| Open-access gezocht | OpenAlex `open_access`, Unpaywall en Semantic Scholar per DOI | **Aloosh & Li stond vrij op DORAS** (Dublin City University) en is volledig gelezen. **Ook Amiram et al.**: de gepubliceerde versie is paywalled, maar de conferentieversie van 2022 staat vrij op het Coller-archief van Tel Aviv University en is gelezen. Pennec et al. is nergens open |

**Wat nog niet gecontroleerd kon worden:**

- Columbia (Sirolly et al.): alleen het abstract en de berichtgeving. SSRN geeft 403 en
  er is geen open versie, dus de paper-body is niet ingezien.
- Pennec, Fiedler & Ante: alleen het abstract via Semantic Scholar. De methodesectie
  kennen we niet en de paper is niet open te krijgen.
- Van Aloosh & Li en Amiram et al. lazen we **eerdere versies**, niet de definitieve
  Management Science-tekst. De strekking is gelijk; details kunnen afwijken.
- WSJ (19 feb. 2019): paywall.
