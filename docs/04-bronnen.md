# 04 — Bronnen

Geannoteerde bibliografie. Per bron: wat erin staat, hoe betrouwbaar hij is, en of we
hem daadwerkelijk hebben.

## 1. De cijfers naast elkaar

| Bron | Steekproef | Uitkomst |
|---|---|---|
| Bitwise Asset Management (SEC-memo, 2019) | 83 exchanges | ~95% van het BTC-spotvolume op CoinMarketCap nep of niet-economisch |
| Forbes / Javier Paz (26 aug. 2022) | 157 exchanges | ~51%; kleine beurzen tot ~95% te hoog; "weinig tot geen toezicht" (Binance, Bybit) claimden $217 mrd tegen $89 mrd gemeten; wereldwijd dagvolume $128 mrd tegen $262 mrd opgeteld (14 juni) |
| Cong, Li, Tang & Yang (NBER w30783) | 29 centrale exchanges | >70% wash trading op **ongereguleerde** venues; gereguleerde venues gedroegen zich als conventionele markten |
| Kaiko (2023-meting) | top-8 venues | Binance 64,3% van het volume tegen 30,7% van de diepte; top-8 91,7% diepte tegen 89,5% volume; 72% van de ETH-liquiditeit op vijf beurzen |
| Bitcenter Research (2023) | 7 exchanges | Phemex: echt volume 5–25% van gerapporteerd; laagste prijs-volume-correlatie van de zeven |
| Columbia-universiteit (nov. 2025) | Polymarket, 3 jaar | ~25% van het volume wash trading, piek ~60% in dec. 2024; sport ~45%, verkiezingen ~17% |
| Cong et al. — twee schatters vergeleken | 29 exchanges | Roundness-schatter **77,5%**; Benford-schatter **16,3%** — factor vijf verschil. Roundness is hun hoofdschatter |
| Victor & Weintraud (WWW '21) | IDEX + EtherDelta, 2017–2020 | **$159 mln** wash-volume; 3,99% resp. 1,30% van alle trades; 31,54% resp. 42,12% van de tokens ooit gewasht; op EtherDelta ~10% van de tokens vrijwel volledig gewasht |

**Waarom 51% en 95% niet in tegenspraak zijn:** ze meten deels verschillende
grootheden (wash trading versus alle niet-economisch volume), over verschillende
steekproeven en periodes. De enige consistente bevinding over álle studies is het gat
tussen gereguleerde en ongereguleerde venues. Wie één percentage noemt zonder
steekproef en definitie, overdrijft wat het onderzoek ondersteunt.

## 2. Wat we in de workspace hebben

| Bestand | Bron | Type | Betrouwbaarheid |
|---|---|---|---|
| `Detecting_Wash_Trade_in_Financial_Mar_...md/.pdf` | Cao, Li, Coleman, Belatreche & McGinnity, *IEEE TNNLS* (2015) | peer-reviewed | **Hoog.** Formele definitie, matching-marges, gesloten cyclus. Vergt order-/accountdata |
| `Wash_trades_as_a_stock_market_manipul...md/.pdf` | Imisiker & Tas, *J. Behavioral and Experimental Finance* (2018) | peer-reviewed | **Hoog.** Wash score + winstregressie. Eén beurs (ISE) |
| `OASIcs.Tokenomics.2021.md/.pdf` | Cong, Li, Tang & Yang, *Detecting and Quantifying Crypto Wash Trading* | proceedings, **6 pagina's** | **Hoog**, maar dit is alleen de samenvatting |
| `w30783.md` | Cong, Li, Tang & Yang, *Crypto Wash Trading*, NBER Working Paper 30783 (dec. 2022) | working paper, **volledig** | **Hoog.** De standaardreferentie: 448.475.535 transacties, 29 beurzen, 3 gereguleerd. Let op: niet peer-reviewed op dit moment van schrijven |
| `Detecting and Quantifying Wash Trading.md/.pdf` | Victor & Weintraud, *Detecting and Quantifying Wash Trading on Decentralized Cryptocurrency Exchanges*, WWW '21 | peer-reviewed, **data + code publiek** | **Hoog.** Enige bron met gelabeld resultaat per account op publieke data. Data: Zenodo `4540223`; code: GitHub `friedhelmvictor/lob-dex-wash-trading-paper` |
| `srnysearca201901-5164833-183434.md/.pdf` | Bitwise-presentatie aan de SEC (19 maart 2019) | primaire bron, **belanghebbende partij** | Cijfers bruikbaar, maar Bitwise had commercieel belang bij een lage marktkwaliteit |
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

## 3. Wat ontbreekt (en prioriteit heeft)

| # | Ontbrekend | Waarom belangrijk | Status |
|---|---|---|---|
| 1 | Victor & Weintraud, *Detecting and quantifying wash trading on DEX*, WWW 2021 | Enige echte wash-trading-detector voor DEX's | **GESLOTEN** — volledig gelezen, formules in §10, detector D25 |
| 2 | Cong et al., volledige NBER-versie (w30783) | De detectiemethodiek (Benford, roundness, staart) staat alleen in het volledige paper | **GESLOTEN** — volledig gelezen, roundness-regressie in §11 |
| 3 | Een gelabelde dataset met wash trades op CEX-spot | Bestaat niet publiek | `OPEN` — zes routes in [03-datalandschap.md](03-datalandschap.md) §6.1 |
| 4 | Een publieke bron met orderboek-events inclusief cancels | Nodig voor F4 (spoofing) | `DEELS` — cancellaties zijn afleidbaar uit diepte-diffs, zie [03-datalandschap.md](03-datalandschap.md) §6.2 |

## 4. Webartikelen die we lazen — met oordeel

| Bron | Oordeel |
|---|---|
| Investopedia, *Wash Trading* | Degelijke uitleg en definitie; geen methode |
| Vultax Research, *Crypto Wash Trading and Real Liquidity* | **Commercieel belang**: verkoopt de screens die het artikel aanprijst. Geeft zijn eigen beperkingen wel eerlijk toe. Cijfers alleen gebruiken met de oorspronkelijke bron erbij |
| Finage, *How to Detect Fake Volume in Stock Markets* | Marketingblog voor een data-API. Methoden zijn gangbaar, geen onderbouwing |
| Marcio Rosa, *How to Spot Fake Volume on Small Exchanges* | Vijf praktische checks, geen bron, geen methode |
| Bitcenter Research (Medium) | Klein maar concreet: correlatiemethode met getallen. Niet peer-reviewed |
| CoinJar, *Defence against the dark arts* | Goede illustratie van het "nul-volume"-signaal van Bitwise; beursblog |
| Cointelegraph (2 sep. 2022) | Journalistieke samenvatting van het Forbes-onderzoek; de originele Forbes-pagina gaf 403 en is niet ingezien |
| WSJ, *Most Bitcoin Trading Faked...* | **Niet gelezen** — paywall |

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
