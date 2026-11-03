# bronnen/

Alle documenten die we in bezit hebben, als Markdown-conversie. De originele
PDF's en EPUB's staan in [`../../sources/`](../../sources/) en worden niet in
versiebeheer opgenomen.

Bestandsnamen zijn ongewijzigd gelaten (zoals ze uit de conversie kwamen). Deze
index is de leesbare laag eroverheen.

## Wat we hebben

| Bestand | Bron | Type | Betrouwbaarheid |
|---|---|---|---|
| `Detecting and Quantifying Wash Trading.md` | Victor & Weintraud, WWW '21 | peer-reviewed, **data + code publiek** | **Hoog.** Enige bron met gelabeld resultaat per account op publieke data |
| `w30783.md` | Cong, Li, Tang & Yang, *Crypto Wash Trading*, NBER 30783 (2022) | working paper, volledig | **Hoog.** De standaardreferentie: 448 mln transacties, 29 beurzen |
| `OASIcs.Tokenomics.2021.md` | Cong et al., proceedingsversie | proceedings, **6 pagina's** | Alleen de samenvatting; gebruik `w30783.md` |
| `Detecting_Wash_Trade_in_Financial_Mar_z_library_sk,_1lib_sk,.md` | Cao, Li, Coleman, Belatreche & McGinnity, *IEEE TNNLS* (2015) | peer-reviewed | **Hoog.** Formele definitie, matching-marges, gesloten cyclus |
| `Wash_trades_as_a_stock_market_manipul_z_library_sk,_1lib_sk,.md` | Imisiker & Tas, *J. Behavioral and Experimental Finance* (2018) | peer-reviewed | **Hoog.** Wash score + winstregressie. Eén beurs (ISE) |
| `srnysearca201901-5164833-183434.md` | Bitwise-presentatie aan de SEC (2019) | primaire bron, **belanghebbende partij** | Cijfers bruikbaar; Bitwise had commercieel belang |
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
EPUB's), zet het bestand hier neer, en voeg een regel toe aan de tabel hierboven
**met** een betrouwbaarheidsoordeel. Een bron zonder oordeel is een bron waar de
volgende lezer niet op kan vertrouwen.
