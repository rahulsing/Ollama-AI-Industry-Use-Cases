# Metro 2 Account Status Codes: internal crosswalk (summary)

| Code | Meaning | Internal bucket |
|---|---|---|
| 11 | Current account (0–29 days past due) | Current |
| 71 | 30–59 days past due | 30+ |
| 78 | 60–89 days past due | 30+, 60+ |
| 80 | 90–119 days past due | 30+, 60+ |
| 82 | 120–149 days past due | 30+, 60+ |
| 83 | 150–179 days past due | 30+, 60+ |
| 97 | Unpaid balance reported as a loss (charged off) | Charged off, not delinquent |
| 13 | Paid or closed, zero balance | Closed |

Our core system stores this code in the column `DLQ_CD`.
