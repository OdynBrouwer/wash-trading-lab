# 06 — Juridisch en ethisch kader

Dit document is geen juridisch advies. Het legt vast welke regels het project zichzelf
oplegt, zodat output niet als beschuldiging kan worden gelezen.

## 1. De kernregel

> **Output is een statistisch signaal, geen vaststelling van schuld.**

Elke detector in dit project meet of data afwijkt van wat organische handel
produceert. Geen enkele detector op publieke data kan vaststellen:

- **wie** het deed (eigendom is niet zichtbaar in publieke feeds);
- **of het met opzet** gebeurde (intentie staat in geen dataset);
- **of het onwettig** was (non-economic volume is niet per definitie verboden).

Daarom gebruikt het project woorden als "afwijkend", "verhoogd risico" en
"statistisch inconsistent met organische handel" — nooit "manipulatie", "fraude" of
"schuldig" als conclusie.

## 2. Formuleringen

| Fout | Goed |
|---|---|
| "Beurs X doet aan wash trading" | "Op beurs X wijkt de verhouding tussen gerapporteerd volume en zichtbare diepte af van de zeven andere gemeten venues in dezelfde periode" |
| "Dit volume is nep" | "Dit volume heeft een statistisch profiel dat niet overeenkomt met organische handel" |
| "Deze detector vindt wash trading" | "Deze detector markeert trades waarvan de kans groter is dat ze niet-economisch zijn" |
| "Bewezen" | "Gemeten, met deze foutmarge, op deze steekproef" |
| "95% van het volume is nep" | "Bitwise rapporteerde in 2019 ~95% voor een steekproef van 83 exchanges, met een definitie van nep die zowel wash trading als niet-economisch volume omvat" |

## 3. Namen van venues

**Besluit (beslissing 3 in [05-roadmap.md](05-roadmap.md) §3):** een venue noemen mag, maar
nooit als schuldig, en alleen als:

1. de gemeten waarde, de periode en de methode erbij staan;
2. er een vergelijkingspunt is (dezelfde meting op andere venues, zelfde moment);
3. de beperkingen van de meting in dezelfde alinea staan;
4. de confidence en de onzekerheidsmarge gerapporteerd worden;
5. er een correctieprocedure is: een venue kan reageren en de meting wordt opnieuw
   gedaan.

Reden: een onjuiste beschuldiging van marktmanipulatie is in Nederland en België
juridisch aanvechtbaar (smaad/laster, en in België ook de ruimere
beledigingsgronden), en in de EU commercieel schadelijk. Zelfs een juiste meting kan
lasterlijk zijn als hij als schuldbewijs wordt gepresenteerd.

**Wat wel mag:** een geanonimiseerde rangorde publiceren ("venue A t/m H") met de
meetwaarden, en de namen alleen op verzoek delen met een onderbouwde onderzoeksvraag.

## 4. Regelgevend kader (context, geen advies)

| Kader | Relevant omdat |
|---|---|
| **MiCAR** (Verordening (EU) 2023/1114) | Verbiedt marktmanipulatie in crypto-activa en verplicht handelsplatformen tot detectie en preventie. Van toepassing sinds 30 december 2024 |
| **CME Rule 575**, overgenomen door de CFTC | Maakt vooraf afgestemde orders expliciet verboden, ook zonder bewezen effect op de prijs |
| **CFTC-advies prediction markets** (25 feb. 2026) | Noemt wash sales en vooraf afgestemde handel als gedrag dat op elke aangewezen markt gehandhaafd wordt |
| **IOSCO Principles for Financial Benchmarks** | Waarom benchmarks als VWM en inverse-variantie-weging bestaan; relevant voor D06 en de Coin Metrics-sectie |
| **IFRS 13 / FASB ASC 820** | Fair-value-kader; verklaart waarom "principal market price"-methodieken volume negeren |

Belangrijk voor het project: **de regels bestaan, de handhaving is het probleem.**
Dat is precies de ruimte waarin een detectietool nuttig is — niet als rechter, maar
als meetinstrument dat een gesprek mogelijk maakt.

## 5. Data en privacy

- Geen persoonlijke data verzamelen, geen KYC, geen e-mailadressen, geen namen.
- Wallet-adressen zijn technisch publiek, maar worden als gevoelig behandeld: geen
  koppeling aan natuurlijke personen, ook niet als die koppeling ergens anders
  publiek is.
- Verwijderverzoeken: als iemand aantoont dat een adres aan hem toebehoort en
  publicatie schade veroorzaakt, wordt de vermelding verwijderd. Dat kost het project
  niets en voorkomt escalatie.
- Ruwe data wordt niet geherdistribueerd als de bronvoorwaarden dat verbieden.

## 6. Ethische grenzen

1. **Geen detectietool die als wapen werkt.** Een detector die precies zegt welke
   specifieke order van welke deelnemer nep is, kan ook gebruikt worden om
   tegenpartijen te slim af te zijn. Daarom publiceert het project methoden en
   geaggregeerde uitkomsten, geen realtime individuele aanklachten.
2. **Geen helpdesk voor manipulation.** Het project legt uit hoe je nepvolume
   *herkent*, niet hoe je het *maakt*. Waar een methode beide kanten op werkt, wordt
   dat benoemd.
3. **Eerlijk over eigen zwakte.** Elke detector die slecht presteert, wordt als zodanig
   gepubliceerd. Een project dat alleen successen toont, is niet te vertrouwen.
4. **Geen verkoopbelang.** Geen affiliate-links, geen betaalde vermeldingen, geen
   "premium tier" die de conclusie beïnvloedt. Dat is precies de fout die we bij
   andere bronnen hebben aangewezen.

## 7. Disclaimer-template voor de README

> Dit project meet statistische eigenschappen van publieke marktdata. Het stelt niet
> vast of een marktdeelnemer zich schuldig maakt aan marktmanipulatie, en de
> uitkomsten zijn geen bewijs van opzet of onwettigheid. Elke score is een
> waarschijnlijkheidsindicatie met een foutmarge. Niets in dit project is
> beleggingsadvies. Genoemde bedragen, percentages en namen van derden zijn
> afkomstig uit de in `docs/04-bronnen.md` vermelde bronnen en worden aan die bronnen
> toegeschreven, niet aan dit project.
