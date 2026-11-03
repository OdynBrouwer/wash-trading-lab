# data/ — niet in versiebeheer

Hier staan werkmonsters van externe datasets. Ze zijn **niet** opgenomen in de
repository: te groot, en herdistributie is alleen toegestaan onder de licentie van
de bron.

## Wat er nu staat

| Bestand | Herkomst | Omvang | Wat het is |
|---|---|---|---|
| `EtherDeltaTrades.slice.csv` | [Zenodo 4540223](https://zenodo.org/records/4540223) (Victor & Weintraud, WWW '21, CC-BY-4.0) | 100 MB | De **eerste 100 MB** van `EtherDeltaTrades.csv` (totaal 1.003 MB). Dekt 10 feb – 26 aug 2017 |

De slice is bewust genomen: het volledige pakket is **3.004 MB** (IDEX 2.001 MB +
EtherDelta 1.003 MB + twee kleine hulpbestanden) en dat is te veel om ongevraagd in
een gesynchroniseerde map te zetten.

## Opnieuw ophalen

Volledig bestand (1 GB):

```powershell
$u = 'https://zenodo.org/api/records/4540223/files/EtherDeltaTrades.csv/content'
Invoke-WebRequest -Uri $u -OutFile data\EtherDeltaTrades.csv
```

Alleen een prefix (zoals de slice hier):

```powershell
Invoke-WebRequest -Uri $u -Headers @{'Range'='bytes=0-104857599'} `
                  -OutFile data\EtherDeltaTrades.slice.csv
```

IDEX heeft dezelfde API-vorm met `IDEXTrades.csv` (2 GB).

## Kolommen

`EtherDeltaTrades.csv`
: `transaction_hash, block_number, timestamp, tokenGet, amountGet, tokenGive,
amountGive, get, give`

- `get` ontvangt `tokenGet`, `give` levert `tokenGive`.
- Is één van beide de nul-adres (`0x000…0`), dan is dat de ETH-kant → volume.
- Trades tussen twee tokens worden overgeslagen (zoals in de paper).

`IDEXTrades.csv`
: `transaction_hash, status, block_number, gas, gas_price, timestamp, amountBuy,
amountSell, expires, nonce, amount, tradeNonce, feeMake, feeTake, tokenBuy,
tokenSell, maker, taker`

- Self-trade: `maker == taker`.

## Waarschuwing bij het lezen van resultaten

Een slice is **niet** representatief. De Victor & Weintraud-cijfers gelden over
2017-09/2017-02 tot 2021-05; dit is alleen de eerste zes maanden van EtherDelta,
toen het volume nog laag was. Vergelijk dus nooit absolute aantallen met de paper.
