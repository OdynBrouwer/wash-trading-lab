# 00 — Scope

Wat dit project wel en niet onderzoekt, en wanneer het geslaagd is.

## 1. Wat is "de scam"

In dit project bedoelen we met *nepvolume*: **gerapporteerd handelsvolume dat niet
voortkomt uit een economische transactie tussen onafhankelijke partijen met
tegengestelde bedoelingen.**

Dat is breder dan de juridische definitie van wash trading, en dat is precies waar de
literatuur uit elkaar loopt. Twee categorieën:

| Term | Definitie | Voorbeeld |
|---|---|---|
| **Wash trading** (smal) | Trades waarbij het economisch belang niet van eigenaar wisselt — een account tegen zichzelf, of twee accounts onder gemeenschappelijke controle | Market maker vult zijn eigen order |
| **Non-economic volume** (breed) | Elke handel die niet om het prijsrisico wordt aangegaan: incentive-trading, fee-rebates, volume-for-hire, airdrop-farming, handelscompetities | Firm handelt met verlies omdat de rebate het verlies dekt |

Het tweede is een superset van het eerste. Wie alleen wash trading telt, komt lager
uit dan wie alle niet-economisch volume telt. **Daarom is het verschil tussen 51% en
95% geen tegenspraak maar een definitieverschil** — zie [04-bronnen.md](04-bronnen.md) §3.

**Let op:** "non-economic volume" is de term zoals de literatuur hem gebruikt, niet onze
eigen classificatie. Als classificatie is hij te zwak, want hij is niet falsifieerbaar: alles
wat je niet begrijpt belandt erin. Wij classificeren daarom op twee assen — economische
geldigheid en herkomst van het volume. Zie
[01-taxonomie.md](01-taxonomie.md) §1.1. De term blijft in dit document staan omdat je
zonder hem niet kunt uitleggen waar de spreiding van 51% tot 95% vandaan komt.

## 2. In scope

1. **CEX spot** — nepvolume op centrale beurzen. Dit is de eerste scope: de meeste
   bronnen, de meeste praktische relevantie, en de data is deels publiek (T0–T2).
2. **Taxonomie die ook DEX, NFT-marktplaatsen en prediction markets dekt**, zodat het
   project later kan uitbreiden zonder herschrijven.
3. **Detectoren op publieke data**, van OHLCV tot orderboek tot on-chain.
4. **Methoden om detectoren te valideren**, inclusief synthetische ground truth
   (zie [03-datalandschap.md](03-datalandschap.md) §4).

## 3. Out of scope (voorlopig)

| Onderwerp | Waarom niet nu |
|---|---|
| Naamgeving van specifieke beurzen als "schuldig" | Juridisch riskant en wetenschappelijk niet te onderbouwen met publieke data |
| Accountidentificatie (wie zit achter een wallet) | Vergt KYC-data die het project niet heeft en niet hoort te hebben |
| Prijsmanipulatie als doel op zich (pump-and-dump, spoofing als *prijs*truc) | Alleen meenemen voor zover het volume raakt; spoofing raakt **orderboek**, niet *volume* — zie [01-taxonomie.md](01-taxonomie.md) §3 |
| Handelsadvies of signalen | Geen onderdeel van het project |
| Betaalde databronnen als vereiste | Het project moet bruikbaar zijn zonder abonnement |

## 4. Uitgangspunten (niet onderhandelbaar)

1. **Signaal, geen vonnis.** Elke output is een risicoscore of een statistische
   afwijking, nooit een uitspraak over opzet of schuld.
2. **Probabilistisch, met foutmarge.** Een detector zonder benoemde foutenkans is
   onbruikbaar.
3. **Data-eerlijkheid.** Bij elke detector staat welke data nodig is, en wat je
   *niet* kunt concluderen als je die data niet hebt.
4. **Brongetrouwheid.** Geen getal zonder steekproef, periode en definitie.
5. **Commerciële belangen benoemd.** Een leverancier die zijn eigen screener aanprijst
   is geen neutrale bron.
6. **Reproduceerbaarheid.** Elke detector moet door een derde opnieuw te draaien zijn
   met dezelfde input.

## 5. Succescriteria

Het project is geslaagd als:

| # | Criterium | Meetbaar |
|---|---|---|
| 1 | Elke detector heeft een tier, een formule en een benoemde valkuil | 100% van de catalogus |
| 2 | Er is een synthetische benchmark met bekende ground truth | Injectie van nepvolume in echte data, met bekende omvang |
| 3 | Elke detector is op die benchmark gescoord (precision/recall) | Tabel met resultaten, inclusief de gevallen waarin hij faalt |
| 4 | Het project zegt expliciet welke vragen het niet kan beantwoorden | Sectie in README + [02-detectoren.md](02-detectoren.md) |
| 5 | Een buitenstaander kan het draaien met alleen gratis data | Handleiding vanaf T0 |

Criterium 3 is het belangrijkste en het minst vanzelfsprekend: **zonder ground truth
is een detector een mening.** Daarom is de synthetische benchmark geen bijzaak maar
voorwaarde.

## 6. Wat "de scam" niet is

Los van de definities, drie dingen die vaak ten onrechte als bewijs gelden:

- **Hoog volume is geen bewijs van echtheid.** Het is juist het cijfer dat het
  makkelijkst te fabriceren is.
- **Een lage spread is geen bewijs van liquiditeit.** Eén kleine order op de touch
  geeft een krappe spread zonder dat er diepte achter zit.
- **Statistische afwijking is geen bewijs van opzet.** Elke detector in dit project
  meet vorm, niet bedoeling. Dat staat in elke paper in dit veld ook zo.
