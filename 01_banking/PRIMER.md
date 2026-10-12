# 🏦 Banking Primer: the business behind the use cases

New to banking? This page explains how the industry works, which department each use case helps, and every
term used in these use cases, in plain English.

[⬅ Back to Banking use cases](README.md)

---

## How it works

**How a bank makes money:** it pays savers a low interest rate on deposits and lends that money to people and
businesses at a higher rate. The difference (the *net interest margin*) is its main income. It also earns *fees* from
payments, cards, wealth advice, trade finance and FX.

**What makes it hard:**
1. **Risk is the job.** Profit disappears if borrowers don't repay (*credit risk*), if the bank runs out of cash (*liquidity risk*), or if processes, people or systems fail (*operational risk*).
2. **Heavily regulated.** Banks hold other people's money and are central to the economy, so regulators set rules on capital, liquidity, fighting financial crime and treating customers fairly. Much of a bank's work (and many use cases here) exists to meet these rules.

## Departments and use cases

| Department | What it does | Use cases |
|---|---|---|
| 🏦 **Lending (Credit)** | The bank's main business: it takes deposits and lends them out at a higher interest rate. The difference is its profit. The skill is lending to people and businesses who will pay back, so credit teams assess, approve, monitor and collect loans. | [01](01_credit_risk_assessment/), [02](02_loan_underwriting_assistant/), [03](03_sme_credit_memo_writer/), [04](04_credit_limit_optimizer/), [05](05_collections_strategy_agent/), [06](06_early_warning_signals/), [07](07_mortgage_prequalification_bot/), [08](08_loan_document_extractor/) |
| 🕵️ **Financial Crime Compliance** | Banks are legally required to stop criminals using them to launder money, finance terrorism, evade sanctions or commit fraud. They must know their customers, monitor transactions and report suspicions. Failures lead to multi-billion fines. | [09](09_aml_transaction_monitoring/), [10](10_kyc_onboarding_verifier/), [11](11_sanctions_screening_assistant/), [12](12_sar_narrative_generator/), [13](13_card_fraud_explainer/), [14](14_tbml_detector/), [15](15_adverse_media_screening/), [16](16_customer_risk_rating/), [17](17_mule_account_detector/) |
| 📜 **Regulation, Risk & Finance** | Because bank failures hurt everyone, regulators require banks to hold enough capital (to absorb losses) and liquidity (to pay what is due), provision for expected loan losses, validate their models, and report regularly. Risk and Finance teams run this. | [18](18_regulatory_reporting_agent/), [19](19_basel_capital_calculator/), [20](20_liquidity_lcr_nsfr_monitor/), [21](21_regulatory_change_tracker/), [22](22_stress_testing_narrator/), [23](23_ifrs9_ecl_calculator/), [24](24_policy_qa_rag/), [25](25_model_risk_validator/) |
| 📈 **Wealth & Investment Management** | Fee-earning advice and investment services: understanding clients' goals and risk appetite, building portfolios and making sure every recommendation is suitable. | [26](26_wealth_advisor_agent/), [27](27_portfolio_rebalancer/), [28](28_risk_profiling_agent/), [29](29_market_news_summarizer/), [30](30_retirement_planner/), [31](31_esg_investment_screener/), [32](32_suitability_checker/) |
| 🙋 **Retail Banking & Customer Experience** | Day-to-day banking for individuals: accounts, cards, loans and support through branches, apps and contact centres. Here the focus is service, fair treatment of customers and growing the relationship. | [33](33_customer_support_agent/), [34](34_complaint_classifier/), [35](35_personal_finance_coach/), [36](36_next_best_offer/), [37](37_churn_retention_agent/), [38](38_dispute_chargeback_assistant/), [39](39_multilingual_faq_rag/), [40](40_call_center_qa/) |
| 💱 **Treasury, Payments & Operations** | The 'plumbing': moving money domestically and internationally, trade finance for importers and exporters, FX, cash management for companies, and back-office matching and checking that keeps everything accurate. | [41](41_swift_payment_validator/), [42](42_cash_flow_forecaster/), [43](43_reconciliation_exception_agent/), [44](44_trade_finance_lc_checker/), [45](45_fx_hedging_advisor/), [46](46_invoice_cheque_extractor/) |
| 🏢 **Analytics, Research & Audit** | Functions that analyse companies (for lending or investing), and internal audit and operational risk, which check that the bank's own controls work. | [47](47_financial_statement_analyzer/), [48](48_earnings_call_analyzer/), [49](49_internal_audit_assistant/), [50](50_operational_risk_analyzer/) |

---

## Glossary

### Lending & credit

- <a id="collateral"></a>**Collateral**: An asset the bank can take if the loan is not repaid, e.g. property or stock.
- <a id="collections"></a>**Collections**: The team that contacts customers who have missed payments and agrees ways to pay, e.g. payment plans.
- <a id="covenant"></a>**Covenant**: A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early.
- <a id="credit-limit--utilisation"></a>**Credit limit / utilisation**: The maximum a customer can borrow on a card or line, and how much of it they are using (balance / limit).
- <a id="credit-memo"></a>**Credit memo**: The written paper a credit committee reads before approving a business loan: who the borrower is, the numbers, risks and recommendation.
- <a id="credit-risk"></a>**Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.
- <a id="credit-score--bureau-score"></a>**Credit score / bureau score**: A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk.
- <a id="delinquency--npa--npl"></a>**Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.
- <a id="dpd-days-past-due"></a>**DPD (Days Past Due)**: How many days a payment is late. 30, 60 and 90 DPD are the standard warning milestones.
- <a id="dscr-debt-service-coverage-ratio"></a>**DSCR (Debt Service Coverage Ratio)**: Cash profit (EBITDA) divided by loan repayments due. Below 1.0x the business cannot cover its debt from operations.
- <a id="dti-debt-to-income"></a>**DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.
- <a id="early-warning-signals-ews"></a>**Early Warning Signals (EWS)**: Signs that a healthy borrower may get into trouble, spotted before they miss payments.
- <a id="emi"></a>**EMI**: Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal.
- <a id="lti-loan-to-income"></a>**LTI (Loan-to-Income)**: Loan amount divided by annual income. Caps how big a loan is relative to what the borrower earns.
- <a id="ltv-loan-to-value"></a>**LTV (Loan-to-Value)**: Loan amount divided by the value of the property. 80% LTV means a 20% deposit; higher LTV means less cushion if prices fall.
- <a id="pre-qualification"></a>**Pre-qualification**: A quick, non-binding estimate of how much a customer could borrow, before a full application.
- <a id="propensity-to-pay"></a>**Propensity to pay**: A prediction of how likely a late customer is to pay, used to choose the right collection approach.
- <a id="risk-grade"></a>**Risk grade**: An internal rating (A, B, C...) that groups borrowers by riskiness and drives approval and pricing.
- <a id="sma--watch-list"></a>**SMA / watch-list**: Special Mention Account / watch-list: loans showing stress that get closer monitoring.
- <a id="underwriting"></a>**Underwriting**: Checking a loan application against the bank's rules and deciding whether to lend, how much and at what price.

### Financial crime

- <a id="adverse-media"></a>**Adverse media**: Negative news linking a customer to crime (fraud, bribery, laundering). Checked during onboarding and reviews.
- <a id="aml-anti-money-laundering"></a>**AML (Anti-Money Laundering)**: Laws and controls that stop criminals disguising illegal money as legitimate. Banks must monitor and report suspicious activity.
- <a id="app-fraud"></a>**APP fraud**: Authorised Push Payment fraud: victims are tricked into sending money themselves, e.g. a fake investment.
- <a id="card-fraud--cnp"></a>**Card fraud / CNP**: Unauthorised card use. Card-Not-Present (online/phone) fraud is the most common type.
- <a id="cdd--edd"></a>**CDD / EDD**: Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth).
- <a id="ctr-currency-transaction-report"></a>**CTR (Currency Transaction Report)**: A report banks file for large cash transactions (e.g. 10,000 or more).
- <a id="customer-risk-rating-crr"></a>**Customer Risk Rating (CRR)**: A Low / Medium / High money-laundering risk score per customer that decides how much due diligence and monitoring they get.
- <a id="false-positive"></a>**False positive**: An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives.
- <a id="kyc-know-your-customer"></a>**KYC (Know Your Customer)**: Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship.
- <a id="mcc"></a>**MCC**: Merchant Category Code: a 4-digit code describing what kind of business a card merchant is, e.g. 5411 grocery, 7995 gambling.
- <a id="mlro"></a>**MLRO**: Money Laundering Reporting Officer: the senior person accountable for deciding whether to file SARs.
- <a id="money-laundering-stages"></a>**Money laundering stages**: Placement (getting cash into the system), layering (moving it to hide the trail), integration (using it as 'clean' money).
- <a id="money-mule"></a>**Money mule**: A person whose account is used to receive and quickly pass on stolen money, often recruited with 'easy money' offers.
- <a id="pep"></a>**PEP**: Politically Exposed Person: someone with a prominent public role (or their family/associates). Higher bribery and corruption risk, so EDD is required.
- <a id="sanctions-screening"></a>**Sanctions screening**: Checking customers and payments against government lists of banned people, companies and countries.
- <a id="sar--str"></a>**SAR / STR**: Suspicious Activity (or Transaction) Report: what a bank files with the financial intelligence unit when it suspects money laundering.
- <a id="structuring-smurfing"></a>**Structuring (smurfing)**: Splitting cash deposits into amounts just under a reporting threshold to avoid triggering a report. Itself an offence.
- <a id="tbml-trade-based-money-laundering"></a>**TBML (Trade-Based Money Laundering)**: Disguising criminal money as trade, e.g. invoicing goods at fake prices to move value across borders.
- <a id="typology"></a>**Typology**: A known pattern of financial crime, e.g. structuring, mule accounts or trade-based laundering.

### Regulation & risk

- <a id="alco"></a>**ALCO**: Asset-Liability Committee: senior managers who oversee the bank's liquidity, funding and interest-rate risk.
- <a id="basel-event-types"></a>**Basel event types**: The 7 standard categories of operational loss (internal fraud, external fraud, system failures, process errors...).
- <a id="basel-iii"></a>**Basel III**: The global rulebook for how much capital and liquidity banks must hold, set by the Basel Committee.
- <a id="capital-cet1-tier-1-tier-2"></a>**Capital (CET1, Tier 1, Tier 2)**: The bank's own money that absorbs losses. CET1 (mostly shareholders' equity) is the highest-quality layer.
- <a id="capital-ratio"></a>**Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.
- <a id="ecl-expected-credit-loss"></a>**ECL (Expected Credit Loss)**: The loss a bank expects on a loan: PD x LGD x EAD. Booked as a provision in the accounts.
- <a id="gini--ks--psi"></a>**Gini / KS / PSI**: Model metrics: Gini and KS measure how well a score separates good and bad customers; PSI measures how much the population has shifted.
- <a id="hqla"></a>**HQLA**: High-Quality Liquid Assets: cash and assets (like government bonds) that can be sold quickly without big losses.
- <a id="icaap"></a>**ICAAP**: Internal Capital Adequacy Assessment Process: the bank's own assessment of the capital it needs, reviewed by the regulator.
- <a id="ifrs-9"></a>**IFRS 9**: The accounting standard that makes banks set aside provisions for expected (not just actual) loan losses.
- <a id="ifrs-9-stages"></a>**IFRS 9 stages**: Stage 1 performing (12-month ECL), Stage 2 significant increase in credit risk (lifetime ECL), Stage 3 credit-impaired.
- <a id="internal-audit"></a>**Internal audit**: The independent team that tests whether the bank's controls work and reports to the board's audit committee.
- <a id="lcr-liquidity-coverage-ratio"></a>**LCR (Liquidity Coverage Ratio)**: High-quality liquid assets / expected net cash outflows over 30 days of stress. Must be at least 100%.
- <a id="liquidity"></a>**Liquidity**: Having enough cash to pay what is due, even under stress. Banks can be solvent but still fail from lack of liquidity.
- <a id="maker-checker"></a>**Maker-checker**: A control where one person enters a transaction and a different person approves it (segregation of duties).
- <a id="model-risk"></a>**Model risk**: The risk of losses from a model that is wrong or misused. Regulators (e.g. SR 11-7) require independent model validation.
- <a id="nsfr-net-stable-funding-ratio"></a>**NSFR (Net Stable Funding Ratio)**: Stable funding available / stable funding required over one year. Must be at least 100%.
- <a id="operational-risk"></a>**Operational risk**: Losses from failed processes, people, systems or external events, e.g. IT outages, errors, fraud, floods.
- <a id="pd--lgd--ead"></a>**PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).
- <a id="regulatory-circular"></a>**Regulatory circular**: A notice from a regulator introducing new rules that banks must implement by a deadline.
- <a id="regulatory-reporting"></a>**Regulatory reporting**: Regular returns banks must send to their regulator (capital, liquidity, large exposures...). Errors can mean fines.
- <a id="rwa-risk-weighted-assets"></a>**RWA (Risk-Weighted Assets)**: Assets adjusted for risk: a government bond might count 0%, an unrated corporate loan 100%. Capital requirements are a % of RWA.
- <a id="sicr"></a>**SICR**: Significant Increase in Credit Risk since the loan was made. Moves a loan from Stage 1 to Stage 2.
- <a id="stress-testing"></a>**Stress testing**: Simulating a severe recession (GDP down, unemployment up) to check the bank would still have enough capital.

### Wealth & investment

- <a id="asset-allocation"></a>**Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- <a id="capital-gains-tax"></a>**Capital gains tax**: Tax on profit from selling an investment. Often lower for long-term holdings, so trade timing matters.
- <a id="esg"></a>**ESG**: Environmental, Social and Governance factors used to screen investments for sustainability.
- <a id="mis-selling"></a>**Mis-selling**: Selling a product that is unsuitable or not properly explained. Leads to compensation and regulatory fines.
- <a id="rebalancing"></a>**Rebalancing**: Buying and selling to bring a portfolio back to its target allocation after markets move it.
- <a id="relationship-manager-rm"></a>**Relationship Manager (RM)**: The banker who owns a client relationship and is their main point of contact.
- <a id="retirement-corpus"></a>**Retirement corpus**: The total savings needed at retirement to fund living costs for the rest of one's life.
- <a id="risk-profile"></a>**Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.
- <a id="sip"></a>**SIP**: Systematic Investment Plan: investing a fixed amount every month into a fund.
- <a id="suitability"></a>**Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.
- <a id="wealth-management"></a>**Wealth management**: Advice and investment services for individuals, from mass affluent to private banking clients.

### Retail & customer

- <a id="503020-rule"></a>**50/30/20 rule**: A budgeting rule: 50% of income on needs, 30% on wants, 20% on savings.
- <a id="call-quality-assurance-qa"></a>**Call quality assurance (QA)**: Reviewing a sample of calls to check staff follow security, compliance and service standards.
- <a id="chargeback"></a>**Chargeback**: Reversing a card payment through the card network (Visa/Mastercard) when a customer has a valid dispute.
- <a id="churn--attrition"></a>**Churn / attrition**: Customers leaving the bank or moving their main banking elsewhere.
- <a id="cross-sell--next-best-offer"></a>**Cross-sell / Next Best Offer**: Offering an existing customer the product they most likely need next.
- <a id="customer-complaint-handling"></a>**Customer complaint handling**: Regulators set deadlines (e.g. resolve within 30 days) and require reporting of complaint trends.
- <a id="reason-code"></a>**Reason code**: The card network's code for why a chargeback is raised (fraud, goods not received...), each with its own evidence rules.
- <a id="retail-banking"></a>**Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.
- <a id="vulnerable-customer"></a>**Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.

### Payments & operations

- <a id="bic--iban--ifsc"></a>**BIC / IBAN / IFSC**: Bank and account identifiers: BIC (bank code, 8 or 11 characters), IBAN (international account number with a checksum), IFSC (Indian branch code).
- <a id="bill-of-lading-bl"></a>**Bill of Lading (B/L)**: The shipping document issued by the carrier: a receipt for goods and proof of shipment. A 'clean' B/L has no damage notes.
- <a id="cash-flow-forecasting"></a>**Cash flow forecasting**: Projecting future cash in and out (often 13 weeks) so a company can plan funding.
- <a id="charges-code-ourshaben"></a>**Charges code (OUR/SHA/BEN)**: Who pays the transfer fees: OUR = sender, SHA = shared, BEN = beneficiary.
- <a id="cheque-truncation--ocr"></a>**Cheque truncation / OCR**: Processing cheques from scanned images; OCR reads the printed and handwritten fields.
- <a id="discrepancy"></a>**Discrepancy**: A mismatch between presented documents and LC terms. Any discrepancy lets the bank refuse to pay.
- <a id="fx-exposure--hedging"></a>**FX exposure / hedging**: Risk that currency moves change the home-currency value of foreign receipts or payments; hedging locks in a rate.
- <a id="fx-forward"></a>**FX forward**: A contract to exchange currency at a fixed rate on a future date. Removes uncertainty for a known cash flow.
- <a id="gstin"></a>**GSTIN**: India's 15-character Goods and Services Tax identification number for a business.
- <a id="incoterms-eg-cif"></a>**Incoterms (e.g. CIF)**: Standard trade terms defining who pays for shipping and insurance. CIF = seller pays Cost, Insurance and Freight.
- <a id="letter-of-credit-lc"></a>**Letter of Credit (LC)**: A bank's promise to pay an exporter if they present documents that exactly match the LC's terms.
- <a id="nostro-account"></a>**Nostro account**: An account a bank holds with another bank in a foreign currency, used to settle payments.
- <a id="reconciliation"></a>**Reconciliation**: Matching the bank's internal ledger against external statements to make sure every entry agrees. Mismatches are 'breaks'.
- <a id="stp-straight-through-processing"></a>**STP (Straight-Through Processing)**: A payment that is processed end-to-end with no manual intervention. Failures need costly manual repair.
- <a id="swift--mt103"></a>**SWIFT / MT103**: SWIFT is the network banks use for international payments; MT103 is the message format for a customer transfer.
- <a id="trade-finance"></a>**Trade finance**: Bank services that help importers and exporters trade safely, e.g. Letters of Credit and guarantees.
- <a id="ucp-600"></a>**UCP 600**: The international rules (from the ICC) that govern how Letters of Credit work and how documents are checked.
- <a id="working-capital"></a>**Working capital**: Money tied up in day-to-day operations (stock, receivables minus payables). Banks fund it with overdrafts and credit lines.

### Corporate finance

- <a id="ebitda--ebit"></a>**EBITDA / EBIT**: Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit.
- <a id="financial-statements"></a>**Financial statements**: Income statement (profit), balance sheet (what is owned and owed) and cash flow statement.
- <a id="free-cash-flow"></a>**Free cash flow**: Operating cash flow minus capital expenditure: the cash really available to repay debt or pay dividends.
- <a id="guidance"></a>**Guidance**: Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording.
- <a id="leverage-debt-to-equity"></a>**Leverage (debt-to-equity)**: How much a company relies on borrowing. Higher leverage means higher risk if earnings fall.
- <a id="liquidity-ratios-current-ratio"></a>**Liquidity ratios (current ratio)**: Current assets / current liabilities: can the company pay its bills due within a year?
- <a id="margins"></a>**Margins**: Profit as a % of revenue (gross, operating, net). Falling margins signal pricing pressure or rising costs.
- <a id="nim-net-interest-margin"></a>**NIM (Net Interest Margin)**: A bank's interest income minus interest paid, as a % of assets. The core measure of lending profitability.

---

*Definitions are simplified for learning. Exact rules vary by country and regulator.*
