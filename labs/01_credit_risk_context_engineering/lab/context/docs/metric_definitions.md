# Credit Risk Metric Definitions (synthetic, for training)

## 30+ Day Delinquency Rate
The share of **balance**, not the share of accounts, that is 30 or more days past due at a month-end snapshot.
- Numerator: outstanding balance of open accounts 30+ days past due.
- Denominator: outstanding balance of all open accounts.
- Charged-off and closed accounts are excluded from both numerator and denominator.

## Seriously delinquent balance (60+ DPD)
Outstanding balance of open accounts that are 60 or more days past due. Charged-off balances are excluded.

## Vintage analysis
A vintage is the group of loans originated in the same month. Older vintages have had more time to default, so vintages must be compared **at the same age**: the cumulative charge-off rate at the same number of months on book (MOB). Our standard comparison point is **MOB 12**.
A vintage with a high charge-off rate early in its life signals weak underwriting or fraud (early payment default), even when its losses to date are smaller than those of older vintages.

## Net charge-off rate
Annualized: 12 × (charge-offs in the month − recoveries in the month) / outstanding balance.
