# bronnen/

Index van alle bronnen die we gelezen hebben. Per bron staat hier ons oordeel over de
betrouwbaarheid.

**De volledige tekstconversies staan niet in deze repository.** Ze staan lokaal in deze
map, maar de rechten liggen bij de uitgevers, dus ze worden niet gepubliceerd. Wat je
hier in de repo vindt is de index; de bestanden zelf worden door `.gitignore`
tegengehouden.

De originele PDF's en EPUB's staan in [`../../sources/`](../../sources/) en worden om
dezelfde reden niet in versiebeheer opgenomen.

Bestandsnamen zijn ongewijzigd gelaten (zoals ze uit de conversie kwamen). Deze
index is de leesbare laag eroverheen.

## Wat we hebben

| Bestand | Bron | Type | Betrouwbaarheid |
|---|---|---|---|
| `Detecting and Quantifying Wash Trading.md` | Victor & Weintraud, WWW '21 | peer-reviewed, **data + code publiek** | **Hoog.** Enige bron met gelabeld resultaat per account op publieke data |
| `ssrn-4649565.md` | Falk, Tsoukalas & Zhang, *Detecting crypto wash trades via machine learning*, Research Policy (2026) | peer-reviewed, **dataset publiek** | **Hoog.** Gelabelde set van NFT-marktplaatsen + Mt. Gox (Mendeley `4hyxfwzpgg` v2). Beperking: geen CEX-spot |
| `aloosh-li-2024.md` | Aloosh & Li, *Direct Evidence of Bitcoin Wash Trading*, Management Science **70**(12), 8875–8921 (2024) | peer-reviewed, **volledige tekst vrij** | **Hoogste.** Gelekte Mt. Gox-administratie: 5,5 mln trades met trader-IDs. Enige ground truth op transactieniveau van een echte beurs |
| `amiram-2022.md` | Amiram, Lyandres & Rabetti, *Competition and Product Quality: Fake Trading on Crypto Exchanges* (2022); in 2025 verschenen als *Trading Volume Manipulation and Competition Among Centralized Crypto Exchanges*, Management Science **71**(10) | peer-reviewed, **conferentieversie vrij** | **Hoog.** 41 beurzen via Kaiko, 76 maanden. Benford + lognormaliteit + structurele breuken via PCA; concurrentie drijft nepvolume op |
| `w30783.md` | Cong, Li, Tang & Yang, *Crypto Wash Trading*, NBER 30783 (2022) | working paper, volledig | **Hoog.** De standaardreferentie: 448 mln transacties, 29 beurzen |
| `OASIcs.Tokenomics.2021.md` | Cong et al., *Detecting and Quantifying Crypto Wash Trading*, Tokenomics 2021, pp. 10:1–10:6 | proceedings, **6 pagina's** | Uitgebreide proceedingsversie met tabel 1; de volledige analyse staat in `w30783.md` |
| `Detecting_Wash_Trade_in_Financial_Mar_z_library_sk,_1lib_sk,.md` | Cao, Li, Coleman, Belatreche & McGinnity, *Detecting Wash Trade in Financial Market Using Digraphs and Dynamic Programming*, IEEE TNNLS **27**(11), 2351–2363 (2016) | peer-reviewed | **Hoog.** Formele definitie, matching-marges, gesloten cyclus |
| `Wash_trades_as_a_stock_market_manipul_z_library_sk,_1lib_sk,.md` | Imisiker & Tas, *J. Behavioral and Experimental Finance* (2018) | peer-reviewed | **Hoog.** Wash score + winstregressie. Eén beurs (ISE) |
| `srnysearca201901-5164833-183434.md` | Bitwise-presentatie aan de SEC (19 maart 2019), vastgelegd in een SEC-staffmemo van 20 maart 2019 | primaire bron, **belanghebbende partij** | Cijfers bruikbaar; Bitwise had commercieel belang. De memo zelf is van de SEC, de inhoud is van Bitwise |
| `coin-metrics-prices-methodology.md` | Coin Metrics Prices Methodology v1.0 (2023) | primaire methodologie | **Hoog.** Transparant en herleidbaar |
| `ptc0518263585.md` | Coinbase Derivatives, CFTC-certificering HYPE futures (2026) | primaire filing | **Hoog.** Voorbeeld van een manipulatiebestendige benchmark |
| `Blockchain Transaction Data Analytics - Complex Network Approaches.md` | Springer, eds. Wu, Lin & Zheng (2025) | peer-reviewed boek | **Hoog** voor graafmethoden; bevat géén wash-trading-detectie |
| `Crypto_and_Decentralized_Finance_Unde_z_library_sk,_1lib_sk,.md` | SpringerBriefs in Finance (2026) | peer-reviewed | **Hoog** voor risico's en aanvalstechnieken in DeFi |
| `New Adventures of CryptoDad - The Quest for Financial Freedom in the 21st Century, The.md` | Giancarlo (Wiley) | memoires/beleidsbetoog | **Kader**, geen detectie |
| `Trader_training_course_CSI_Global_Ed_z_library_sk,_1lib_sk,.md` | CSI Global Education (2008) | lesmateriaal | Matig. Canadees rulebook-perspectief, verouderd |
| `Proceedings_of_International_Conferen_z_library_sk,_1lib_sk,.md` | ICAIN 2025 | proceedings | Eén terloopse vermelding; verder niet relevant |
| `Etika_Bisnis_dalam_Perspektif_Manajem_z_library_sk,_1lib_sk,.md` | Indonesisch leerboek bedrijfsethiek | leerboek | Eén paragraaf over marktmanipulatie; niet technisch bruikbaar |
| `加密貨幣之王.md` | Roberts, *Kings of Crypto* (2021, Chinese vertaling) | journalistiek | Anekdotisch. Eén vermoeden van een concurrent (regel 1503) |
| `Cryptocurrency Trading & Investment Guide foecentralized Finance. Learn Bitcoin and Ethe.md` | Lazar | self-published | **Onbetrouwbaar.** Aantoonbaar onjuiste claims (regel 1242) en rekenfouten |

## Verantwoording

De onderbouwing per bron — met steekproef, periode en de kanttekening — staat in
[`../04-bronnen.md`](../04-bronnen.md). Gebruik die als je een cijfer wilt citeren.

## Toevoegen

Nieuwe bron toevoegen: converteer naar `.md` (zie `../../scripts/epub2md.py` voor
EPUB's), zet het bestand lokaal in deze map — het wordt door `.gitignore` buiten de
repo gehouden — en voeg **alleen** een regel toe aan de tabel hierboven, met een
betrouwbaarheidsoordeel. Een bron zonder oordeel is een bron waar de volgende lezer
niet op kan vertrouwen.
