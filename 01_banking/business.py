"""Plain-English business context for people new to banking (used by build_docs.py and ui.py)."""

INDUSTRY_101 = """\
**How a bank makes money:** it pays savers a low interest rate on deposits and lends that money to people and
businesses at a higher rate. The difference (the *net interest margin*) is its main income. It also earns *fees* from
payments, cards, wealth advice, trade finance and FX.

**What makes it hard:**
1. **Risk is the job.** Profit disappears if borrowers don't repay (*credit risk*), if the bank runs out of cash (*liquidity risk*), or if processes, people or systems fail (*operational risk*).
2. **Heavily regulated.** Banks hold other people's money and are central to the economy, so regulators set rules on capital, liquidity, fighting financial crime and treating customers fairly. Much of a bank's work (and many use cases here) exists to meet these rules.
"""

# --------------------------------------------------------------------------- #
# Glossary: term -> (group, definition)
# --------------------------------------------------------------------------- #
GLOSSARY = {
    # Lending & credit
    "Credit risk": ("Lending & credit", "The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender."),
    "Underwriting": ("Lending & credit", "Checking a loan application against the bank's rules and deciding whether to lend, how much and at what price."),
    "DTI (Debt-to-Income)": ("Lending & credit", "Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments."),
    "LTI (Loan-to-Income)": ("Lending & credit", "Loan amount divided by annual income. Caps how big a loan is relative to what the borrower earns."),
    "LTV (Loan-to-Value)": ("Lending & credit", "Loan amount divided by the value of the property. 80% LTV means a 20% deposit; higher LTV means less cushion if prices fall."),
    "EMI": ("Lending & credit", "Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal."),
    "Credit score / bureau score": ("Lending & credit", "A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk."),
    "Risk grade": ("Lending & credit", "An internal rating (A, B, C...) that groups borrowers by riskiness and drives approval and pricing."),
    "Credit memo": ("Lending & credit", "The written paper a credit committee reads before approving a business loan: who the borrower is, the numbers, risks and recommendation."),
    "DSCR (Debt Service Coverage Ratio)": ("Lending & credit", "Cash profit (EBITDA) divided by loan repayments due. Below 1.0x the business cannot cover its debt from operations."),
    "Covenant": ("Lending & credit", "A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early."),
    "Collateral": ("Lending & credit", "An asset the bank can take if the loan is not repaid, e.g. property or stock."),
    "Credit limit / utilisation": ("Lending & credit", "The maximum a customer can borrow on a card or line, and how much of it they are using (balance / limit)."),
    "DPD (Days Past Due)": ("Lending & credit", "How many days a payment is late. 30, 60 and 90 DPD are the standard warning milestones."),
    "Delinquency / NPA / NPL": ("Lending & credit", "A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan."),
    "Collections": ("Lending & credit", "The team that contacts customers who have missed payments and agrees ways to pay, e.g. payment plans."),
    "Propensity to pay": ("Lending & credit", "A prediction of how likely a late customer is to pay, used to choose the right collection approach."),
    "Early Warning Signals (EWS)": ("Lending & credit", "Signs that a healthy borrower may get into trouble, spotted before they miss payments."),
    "SMA / watch-list": ("Lending & credit", "Special Mention Account / watch-list: loans showing stress that get closer monitoring."),
    "Pre-qualification": ("Lending & credit", "A quick, non-binding estimate of how much a customer could borrow, before a full application."),
    # Financial crime
    "AML (Anti-Money Laundering)": ("Financial crime", "Laws and controls that stop criminals disguising illegal money as legitimate. Banks must monitor and report suspicious activity."),
    "Money laundering stages": ("Financial crime", "Placement (getting cash into the system), layering (moving it to hide the trail), integration (using it as 'clean' money)."),
    "Structuring (smurfing)": ("Financial crime", "Splitting cash deposits into amounts just under a reporting threshold to avoid triggering a report. Itself an offence."),
    "CTR (Currency Transaction Report)": ("Financial crime", "A report banks file for large cash transactions (e.g. 10,000 or more)."),
    "SAR / STR": ("Financial crime", "Suspicious Activity (or Transaction) Report: what a bank files with the financial intelligence unit when it suspects money laundering."),
    "MLRO": ("Financial crime", "Money Laundering Reporting Officer: the senior person accountable for deciding whether to file SARs."),
    "Typology": ("Financial crime", "A known pattern of financial crime, e.g. structuring, mule accounts or trade-based laundering."),
    "KYC (Know Your Customer)": ("Financial crime", "Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship."),
    "CDD / EDD": ("Financial crime", "Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth)."),
    "PEP": ("Financial crime", "Politically Exposed Person: someone with a prominent public role (or their family/associates). Higher bribery and corruption risk, so EDD is required."),
    "Sanctions screening": ("Financial crime", "Checking customers and payments against government lists of banned people, companies and countries."),
    "False positive": ("Financial crime", "An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives."),
    "Adverse media": ("Financial crime", "Negative news linking a customer to crime (fraud, bribery, laundering). Checked during onboarding and reviews."),
    "Customer Risk Rating (CRR)": ("Financial crime", "A Low / Medium / High money-laundering risk score per customer that decides how much due diligence and monitoring they get."),
    "Money mule": ("Financial crime", "A person whose account is used to receive and quickly pass on stolen money, often recruited with 'easy money' offers."),
    "APP fraud": ("Financial crime", "Authorised Push Payment fraud: victims are tricked into sending money themselves, e.g. a fake investment."),
    "TBML (Trade-Based Money Laundering)": ("Financial crime", "Disguising criminal money as trade, e.g. invoicing goods at fake prices to move value across borders."),
    "Card fraud / CNP": ("Financial crime", "Unauthorised card use. Card-Not-Present (online/phone) fraud is the most common type."),
    "MCC": ("Financial crime", "Merchant Category Code: a 4-digit code describing what kind of business a card merchant is, e.g. 5411 grocery, 7995 gambling."),
    # Regulation & risk
    "Regulatory reporting": ("Regulation & risk", "Regular returns banks must send to their regulator (capital, liquidity, large exposures...). Errors can mean fines."),
    "Basel III": ("Regulation & risk", "The global rulebook for how much capital and liquidity banks must hold, set by the Basel Committee."),
    "Capital (CET1, Tier 1, Tier 2)": ("Regulation & risk", "The bank's own money that absorbs losses. CET1 (mostly shareholders' equity) is the highest-quality layer."),
    "RWA (Risk-Weighted Assets)": ("Regulation & risk", "Assets adjusted for risk: a government bond might count 0%, an unrated corporate loan 100%. Capital requirements are a % of RWA."),
    "Capital ratio": ("Regulation & risk", "Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom."),
    "Liquidity": ("Regulation & risk", "Having enough cash to pay what is due, even under stress. Banks can be solvent but still fail from lack of liquidity."),
    "LCR (Liquidity Coverage Ratio)": ("Regulation & risk", "High-quality liquid assets / expected net cash outflows over 30 days of stress. Must be at least 100%."),
    "NSFR (Net Stable Funding Ratio)": ("Regulation & risk", "Stable funding available / stable funding required over one year. Must be at least 100%."),
    "HQLA": ("Regulation & risk", "High-Quality Liquid Assets: cash and assets (like government bonds) that can be sold quickly without big losses."),
    "ALCO": ("Regulation & risk", "Asset-Liability Committee: senior managers who oversee the bank's liquidity, funding and interest-rate risk."),
    "Stress testing": ("Regulation & risk", "Simulating a severe recession (GDP down, unemployment up) to check the bank would still have enough capital."),
    "ICAAP": ("Regulation & risk", "Internal Capital Adequacy Assessment Process: the bank's own assessment of the capital it needs, reviewed by the regulator."),
    "IFRS 9": ("Regulation & risk", "The accounting standard that makes banks set aside provisions for expected (not just actual) loan losses."),
    "ECL (Expected Credit Loss)": ("Regulation & risk", "The loss a bank expects on a loan: PD x LGD x EAD. Booked as a provision in the accounts."),
    "PD / LGD / EAD": ("Regulation & risk", "Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed)."),
    "IFRS 9 stages": ("Regulation & risk", "Stage 1 performing (12-month ECL), Stage 2 significant increase in credit risk (lifetime ECL), Stage 3 credit-impaired."),
    "SICR": ("Regulation & risk", "Significant Increase in Credit Risk since the loan was made. Moves a loan from Stage 1 to Stage 2."),
    "Model risk": ("Regulation & risk", "The risk of losses from a model that is wrong or misused. Regulators (e.g. SR 11-7) require independent model validation."),
    "Gini / KS / PSI": ("Regulation & risk", "Model metrics: Gini and KS measure how well a score separates good and bad customers; PSI measures how much the population has shifted."),
    "Regulatory circular": ("Regulation & risk", "A notice from a regulator introducing new rules that banks must implement by a deadline."),
    "Operational risk": ("Regulation & risk", "Losses from failed processes, people, systems or external events, e.g. IT outages, errors, fraud, floods."),
    "Basel event types": ("Regulation & risk", "The 7 standard categories of operational loss (internal fraud, external fraud, system failures, process errors...)."),
    "Internal audit": ("Regulation & risk", "The independent team that tests whether the bank's controls work and reports to the board's audit committee."),
    "Maker-checker": ("Regulation & risk", "A control where one person enters a transaction and a different person approves it (segregation of duties)."),
    # Wealth & investment
    "Wealth management": ("Wealth & investment", "Advice and investment services for individuals, from mass affluent to private banking clients."),
    "Asset allocation": ("Wealth & investment", "How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return."),
    "Risk profile": ("Wealth & investment", "How much investment risk a client is willing and able to take, usually from a questionnaire."),
    "Suitability": ("Wealth & investment", "The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon."),
    "Mis-selling": ("Wealth & investment", "Selling a product that is unsuitable or not properly explained. Leads to compensation and regulatory fines."),
    "Rebalancing": ("Wealth & investment", "Buying and selling to bring a portfolio back to its target allocation after markets move it."),
    "SIP": ("Wealth & investment", "Systematic Investment Plan: investing a fixed amount every month into a fund."),
    "Capital gains tax": ("Wealth & investment", "Tax on profit from selling an investment. Often lower for long-term holdings, so trade timing matters."),
    "ESG": ("Wealth & investment", "Environmental, Social and Governance factors used to screen investments for sustainability."),
    "Relationship Manager (RM)": ("Wealth & investment", "The banker who owns a client relationship and is their main point of contact."),
    "Retirement corpus": ("Wealth & investment", "The total savings needed at retirement to fund living costs for the rest of one's life."),
    # Retail & customer
    "Retail banking": ("Retail & customer", "Banking for individuals: accounts, cards, loans, mortgages and savings."),
    "Customer complaint handling": ("Retail & customer", "Regulators set deadlines (e.g. resolve within 30 days) and require reporting of complaint trends."),
    "Vulnerable customer": ("Retail & customer", "Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them."),
    "Chargeback": ("Retail & customer", "Reversing a card payment through the card network (Visa/Mastercard) when a customer has a valid dispute."),
    "Reason code": ("Retail & customer", "The card network's code for why a chargeback is raised (fraud, goods not received...), each with its own evidence rules."),
    "Cross-sell / Next Best Offer": ("Retail & customer", "Offering an existing customer the product they most likely need next."),
    "Churn / attrition": ("Retail & customer", "Customers leaving the bank or moving their main banking elsewhere."),
    "50/30/20 rule": ("Retail & customer", "A budgeting rule: 50% of income on needs, 30% on wants, 20% on savings."),
    "Call quality assurance (QA)": ("Retail & customer", "Reviewing a sample of calls to check staff follow security, compliance and service standards."),
    # Payments, treasury, operations
    "SWIFT / MT103": ("Payments & operations", "SWIFT is the network banks use for international payments; MT103 is the message format for a customer transfer."),
    "STP (Straight-Through Processing)": ("Payments & operations", "A payment that is processed end-to-end with no manual intervention. Failures need costly manual repair."),
    "BIC / IBAN / IFSC": ("Payments & operations", "Bank and account identifiers: BIC (bank code, 8 or 11 characters), IBAN (international account number with a checksum), IFSC (Indian branch code)."),
    "Charges code (OUR/SHA/BEN)": ("Payments & operations", "Who pays the transfer fees: OUR = sender, SHA = shared, BEN = beneficiary."),
    "Reconciliation": ("Payments & operations", "Matching the bank's internal ledger against external statements to make sure every entry agrees. Mismatches are 'breaks'."),
    "Nostro account": ("Payments & operations", "An account a bank holds with another bank in a foreign currency, used to settle payments."),
    "Trade finance": ("Payments & operations", "Bank services that help importers and exporters trade safely, e.g. Letters of Credit and guarantees."),
    "Letter of Credit (LC)": ("Payments & operations", "A bank's promise to pay an exporter if they present documents that exactly match the LC's terms."),
    "UCP 600": ("Payments & operations", "The international rules (from the ICC) that govern how Letters of Credit work and how documents are checked."),
    "Discrepancy": ("Payments & operations", "A mismatch between presented documents and LC terms. Any discrepancy lets the bank refuse to pay."),
    "Bill of Lading (B/L)": ("Payments & operations", "The shipping document issued by the carrier: a receipt for goods and proof of shipment. A 'clean' B/L has no damage notes."),
    "Incoterms (e.g. CIF)": ("Payments & operations", "Standard trade terms defining who pays for shipping and insurance. CIF = seller pays Cost, Insurance and Freight."),
    "Cash flow forecasting": ("Payments & operations", "Projecting future cash in and out (often 13 weeks) so a company can plan funding."),
    "Working capital": ("Payments & operations", "Money tied up in day-to-day operations (stock, receivables minus payables). Banks fund it with overdrafts and credit lines."),
    "FX exposure / hedging": ("Payments & operations", "Risk that currency moves change the home-currency value of foreign receipts or payments; hedging locks in a rate."),
    "FX forward": ("Payments & operations", "A contract to exchange currency at a fixed rate on a future date. Removes uncertainty for a known cash flow."),
    "GSTIN": ("Payments & operations", "India's 15-character Goods and Services Tax identification number for a business."),
    "Cheque truncation / OCR": ("Payments & operations", "Processing cheques from scanned images; OCR reads the printed and handwritten fields."),
    # Corporate finance
    "Financial statements": ("Corporate finance", "Income statement (profit), balance sheet (what is owned and owed) and cash flow statement."),
    "EBITDA / EBIT": ("Corporate finance", "Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit."),
    "Margins": ("Corporate finance", "Profit as a % of revenue (gross, operating, net). Falling margins signal pricing pressure or rising costs."),
    "Leverage (debt-to-equity)": ("Corporate finance", "How much a company relies on borrowing. Higher leverage means higher risk if earnings fall."),
    "Liquidity ratios (current ratio)": ("Corporate finance", "Current assets / current liabilities: can the company pay its bills due within a year?"),
    "Free cash flow": ("Corporate finance", "Operating cash flow minus capital expenditure: the cash really available to repay debt or pay dividends."),
    "NIM (Net Interest Margin)": ("Corporate finance", "A bank's interest income minus interest paid, as a % of assets. The core measure of lending profitability."),
    "Guidance": ("Corporate finance", "Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording."),
}

# --------------------------------------------------------------------------- #
# Per use case: (what happens in a bank today, who does it, why it's hard, [glossary terms])
# --------------------------------------------------------------------------- #
BUSINESS = {
    "01_credit_risk_assessment": (
        "When someone applies for a personal loan, the bank must decide: will this person pay us back? Credit analysts look at income, existing debts, credit bureau history and the bank's lending policy, then a more senior approver signs off.",
        "Retail credit analysts and credit approvers (Risk department).",
        "Thousands of applications arrive daily. Decisions must be fast, consistent and explainable to the customer and the regulator.",
        ["Credit risk", "DTI (Debt-to-Income)", "LTI (Loan-to-Income)", "EMI", "Credit score / bureau score", "Risk grade"]),
    "02_loan_underwriting_assistant": (
        "Mortgage underwriters check every application against a rulebook: can the borrower afford the payments, is the deposit big enough, is their job stable? They then approve, decline or approve with conditions.",
        "Mortgage underwriters (Retail Lending).",
        "Rules are detailed and easy to misapply under time pressure; every decision must be traceable to a rule.",
        ["Underwriting", "DTI (Debt-to-Income)", "LTV (Loan-to-Value)", "Credit score / bureau score"]),
    "03_sme_credit_memo_writer": (
        "Before lending to a small or mid-sized business, a relationship manager and credit analyst write a 'credit memo': who the business is, how it is performing, whether it can repay, and what protections the bank will take.",
        "Corporate/SME relationship managers and credit analysts.",
        "Writing a memo takes days of spreadsheet work and drafting; analysts spend more time writing than analysing.",
        ["Credit memo", "DSCR (Debt Service Coverage Ratio)", "EBITDA / EBIT", "Leverage (debt-to-equity)", "Covenant", "Collateral"]),
    "04_credit_limit_optimizer": (
        "Card issuers regularly review limits: raise them for good customers who need more room, and reduce them for customers showing signs of stress, to manage risk.",
        "Card portfolio managers (Cards / Unsecured Lending).",
        "Limit changes affect revenue, risk and customer trust. Each one needs a clear reason, especially a decrease.",
        ["Credit limit / utilisation", "Credit score / bureau score", "Credit risk"]),
    "05_collections_strategy_agent": (
        "When customers miss loan payments, the collections team decides who to contact, how (SMS, call, letter), how often, and what to offer (payment plan, settlement).",
        "Collections strategy and operations teams.",
        "Too soft loses money; too aggressive harms customers and breaks conduct rules, especially for customers in hardship.",
        ["Collections", "DPD (Days Past Due)", "Delinquency / NPA / NPL", "Propensity to pay", "Vulnerable customer"]),
    "06_early_warning_signals": (
        "For business loans, banks watch for warning signs (overdraft breaches, bounced cheques, falling sales, rating downgrades) so they can act before the borrower defaults.",
        "Credit monitoring teams and relationship managers.",
        "Signals are spread across many systems; spotting them early is what makes a recovery possible.",
        ["Early Warning Signals (EWS)", "SMA / watch-list", "Credit risk", "Covenant"]),
    "07_mortgage_prequalification_bot": (
        "Before a full mortgage application, customers want a quick answer to 'how much can I borrow?' so they know which homes to look at.",
        "Mortgage advisers, branch staff and digital channels.",
        "Customers expect instant answers at any hour; staff time is better spent on serious applications.",
        ["Pre-qualification", "DTI (Debt-to-Income)", "EMI", "LTV (Loan-to-Value)"]),
    "08_loan_document_extractor": (
        "Loan processors read payslips and bank statements to verify income and existing debts, and re-type the figures into the loan system.",
        "Loan operations / processing teams.",
        "Manual data entry is slow and error-prone, and mismatches between documents can signal fraud.",
        ["Underwriting", "EMI", "DTI (Debt-to-Income)"]),
    "09_aml_transaction_monitoring": (
        "Banks must monitor transactions for money laundering. Rules generate alerts (e.g. repeated cash deposits just under the reporting limit); investigators review each alert and decide whether to report it.",
        "AML transaction monitoring analysts and the MLRO (Compliance / Financial Crime).",
        "Most alerts are false positives, yet missing a real case can bring huge fines. Investigation is slow and manual.",
        ["AML (Anti-Money Laundering)", "Money laundering stages", "Structuring (smurfing)", "CTR (Currency Transaction Report)", "SAR / STR", "MLRO", "False positive"]),
    "10_kyc_onboarding_verifier": (
        "Before opening an account, the bank must verify identity and address documents and check they match the application.",
        "KYC / onboarding operations teams.",
        "Checks are repetitive; small mismatches (spelling, expired IDs) are easy to miss and delay customers.",
        ["KYC (Know Your Customer)", "CDD / EDD"]),
    "11_sanctions_screening_assistant": (
        "Every customer and international payment is screened against sanctions lists. A similar name triggers an alert that an analyst must clear or escalate before money moves.",
        "Sanctions screening analysts (Financial Crime Compliance).",
        "Name matching produces many false positives that delay payments, while a missed true match is a serious legal breach.",
        ["Sanctions screening", "False positive", "PEP"]),
    "12_sar_narrative_generator": (
        "When an investigation concludes activity is suspicious, the bank files a SAR with a written narrative explaining who, what, when, where and why.",
        "AML investigators and the MLRO.",
        "Narratives must be precise, factual and complete; writing them takes hours per case.",
        ["SAR / STR", "MLRO", "Typology", "Money mule", "APP fraud"]),
    "13_card_fraud_explainer": (
        "Card transactions are scored for fraud in real time. Suspicious ones are blocked or held, and the customer is asked to confirm.",
        "Fraud operations analysts.",
        "Blocking genuine spending annoys customers; letting fraud through costs money. Analysts need to see why a transaction was flagged.",
        ["Card fraud / CNP", "MCC", "False positive"]),
    "14_tbml_detector": (
        "Trade finance teams check that goods, prices and shipping routes make commercial sense, because criminals use fake trade invoices to move money across borders.",
        "Trade finance operations and financial crime specialists.",
        "Requires knowing what goods normally cost and how they normally ship; red flags are subtle.",
        ["TBML (Trade-Based Money Laundering)", "Trade finance", "Letter of Credit (LC)"]),
    "15_adverse_media_screening": (
        "During onboarding and periodic reviews, banks search news for negative stories about customers (fraud, corruption, investigations).",
        "KYC / Enhanced Due Diligence analysts.",
        "Searches return many irrelevant hits, including people who just share a name. Reading them all is time-consuming.",
        ["Adverse media", "CDD / EDD", "KYC (Know Your Customer)"]),
    "16_customer_risk_rating": (
        "Each customer gets a money-laundering risk rating based on factors like occupation, countries, products and PEP status. It decides how much checking and how frequent reviews they need.",
        "KYC / AML compliance teams.",
        "Ratings must be consistent and justified in writing for auditors and regulators.",
        ["Customer Risk Rating (CRR)", "PEP", "CDD / EDD", "KYC (Know Your Customer)"]),
    "17_mule_account_detector": (
        "Fraudsters use 'mule' accounts to receive stolen money and pass it on quickly. Banks look for accounts where money comes in from many people and leaves almost immediately.",
        "Fraud and financial crime teams.",
        "Mules are often young people being exploited, so action must stop the fraud and also protect them.",
        ["Money mule", "APP fraud", "Typology"]),
    "18_regulatory_reporting_agent": (
        "Each quarter, banks submit returns to the regulator on capital, liquidity and asset quality, with commentary explaining big movements.",
        "Regulatory reporting team (Finance), signed off by the CFO.",
        "Data comes from many systems; errors or unexplained movements trigger regulator questions or fines.",
        ["Regulatory reporting", "Capital (CET1, Tier 1, Tier 2)", "RWA (Risk-Weighted Assets)", "Capital ratio", "LCR (Liquidity Coverage Ratio)", "Delinquency / NPA / NPL"]),
    "19_basel_capital_calculator": (
        "Banks must hold enough capital against risky assets. Treasury and risk teams constantly ask: what are our ratios, and what happens if we lend more?",
        "Capital management (Treasury / Finance / Risk).",
        "Capital is expensive and limited; every lending decision consumes some, so quick what-if answers matter.",
        ["Basel III", "Capital (CET1, Tier 1, Tier 2)", "RWA (Risk-Weighted Assets)", "Capital ratio"]),
    "20_liquidity_lcr_nsfr_monitor": (
        "Treasury tracks whether the bank has enough liquid assets to survive a 30-day stress (LCR) and stable funding for the next year (NSFR), and reports to ALCO.",
        "Treasury / liquidity risk team, reporting to ALCO.",
        "Liquidity can disappear fast (as in bank runs); positions must be monitored and explained frequently.",
        ["Liquidity", "LCR (Liquidity Coverage Ratio)", "NSFR (Net Stable Funding Ratio)", "HQLA", "ALCO"]),
    "21_regulatory_change_tracker": (
        "Regulators publish new rules constantly. Compliance must work out what each new rule requires, which teams and systems are affected, and what must change by the deadline.",
        "Compliance and regulatory change management teams.",
        "Legal text is dense, and missing one obligation can lead to enforcement action.",
        ["Regulatory circular", "Regulatory reporting"]),
    "22_stress_testing_narrator": (
        "Banks simulate severe recessions to check they would still have enough capital, then explain the results to the board and regulator.",
        "Stress testing / ICAAP teams (Risk), economists, the board risk committee.",
        "Results must be turned into a clear story of what breaks, why, and what management would do.",
        ["Stress testing", "ICAAP", "PD / LGD / EAD", "Capital ratio"]),
    "23_ifrs9_ecl_calculator": (
        "Under IFRS 9, banks set aside provisions for loans they expect to go bad, based on each loan's stage and probability of default.",
        "Credit risk / impairment team and Finance.",
        "Provisions directly hit profit; auditors challenge every staging decision and number.",
        ["IFRS 9", "ECL (Expected Credit Loss)", "PD / LGD / EAD", "IFRS 9 stages", "SICR"]),
    "24_policy_qa_rag": (
        "Bank staff constantly need answers from long internal policy manuals: 'can I approve this?', 'what do I do with this cash deposit?'.",
        "Front-line staff, operations and compliance (as the help desk).",
        "Policies are long and scattered; wrong answers lead to breaches; compliance teams answer the same questions repeatedly.",
        ["KYC (Know Your Customer)", "PEP", "CTR (Currency Transaction Report)", "Structuring (smurfing)"]),
    "25_model_risk_validator": (
        "Banks use statistical models (e.g. credit scores) to make decisions. An independent team must test each model regularly and report whether it still works.",
        "Model validation / Model Risk Management team.",
        "Validation reports are long and technical; findings must be rated and explained to non-specialists.",
        ["Model risk", "Gini / KS / PSI", "PD / LGD / EAD"]),
    "26_wealth_advisor_agent": (
        "Wealth advisers understand a client's goals (education, retirement, a home), assess their risk tolerance, recommend a portfolio and document why it is suitable.",
        "Financial advisers / relationship managers, checked by compliance.",
        "Good advice is personal and time-consuming, so it is usually only available to wealthier clients.",
        ["Wealth management", "Asset allocation", "Risk profile", "Suitability", "SIP"]),
    "27_portfolio_rebalancer": (
        "Markets move, so a client's portfolio drifts away from its agreed mix (e.g. too much in equities after a rally). Advisers rebalance by selling some winners and buying underweight assets, minding taxes.",
        "Portfolio managers and advisers.",
        "Rebalancing too little lets risk creep up; doing it carelessly triggers unnecessary taxes and costs.",
        ["Rebalancing", "Asset allocation", "Capital gains tax"]),
    "28_risk_profiling_agent": (
        "Before giving investment advice, banks must assess a client's risk profile, usually through a questionnaire, and explain the result to the client.",
        "Advisers / RMs.",
        "Answers are often contradictory (e.g. wants high growth but cannot tolerate losses), and these need a conversation.",
        ["Risk profile", "Suitability"]),
    "29_market_news_summarizer": (
        "Every morning, relationship managers need to know what happened in markets and which of their clients are affected, so they can call them proactively.",
        "Relationship managers, investment strategists.",
        "News volume is huge; linking it to each client's holdings by hand is impossible at scale.",
        ["Relationship Manager (RM)", "Asset allocation", "Guidance"]),
    "30_retirement_planner": (
        "Customers ask 'can I retire at 60?'. Advisers estimate the savings needed, project current savings forward and work out the gap.",
        "Financial planners and digital advice tools.",
        "The maths (inflation, returns, years in retirement) is unfamiliar to most customers; clear what-ifs help them act.",
        ["Retirement corpus", "SIP", "Asset allocation"]),
    "31_esg_investment_screener": (
        "More clients want investments that match their values, such as no tobacco or weapons and low carbon. Advisers screen funds and explain the trade-offs.",
        "Investment advisers and ESG / product teams.",
        "ESG data is messy and greenwashing is a regulatory risk.",
        ["ESG", "Asset allocation", "Suitability"]),
    "32_suitability_checker": (
        "Before a product is sold, a check confirms it suits the client's risk profile, knowledge, time horizon and need for cash.",
        "Sales supervisors and compliance / conduct teams.",
        "Mis-selling (especially to elderly or vulnerable customers) leads to compensation and fines.",
        ["Suitability", "Mis-selling", "Vulnerable customer", "Risk profile"]),
    "33_customer_support_agent": (
        "Contact centres handle millions of simple requests: balances, recent transactions, blocking a lost card, branch hours.",
        "Contact centre / customer service.",
        "Simple requests clog queues; customers want 24/7 instant help, done securely.",
        ["Retail banking"]),
    "34_complaint_classifier": (
        "Complaints arrive by email, phone and social media. Each must be categorised, prioritised and routed to the right team within regulatory deadlines.",
        "Complaints handling teams, with conduct/compliance oversight.",
        "Misrouted or late complaints breach rules; complaints from vulnerable customers need urgent attention.",
        ["Customer complaint handling", "Vulnerable customer", "Mis-selling"]),
    "35_personal_finance_coach": (
        "Banks increasingly help customers manage money, analysing spending and suggesting budgets and savings inside the banking app.",
        "Digital banking / customer engagement teams.",
        "Customers want personal, practical advice, not generic tips.",
        ["50/30/20 rule", "Retail banking"]),
    "36_next_best_offer": (
        "Banks try to offer each customer the product they most likely need next (e.g. a credit card for a new salaried customer) at the right time and channel.",
        "Marketing / CRM analytics teams.",
        "Irrelevant offers annoy customers and can be seen as pushy or unfair.",
        ["Cross-sell / Next Best Offer", "Retail banking"]),
    "37_churn_retention_agent": (
        "Banks watch for customers about to leave (salary stops arriving, balances drop, complaints rise) and try to keep the valuable ones.",
        "Customer analytics and retention / customer success teams.",
        "Winning back a customer after they leave is much harder than keeping them.",
        ["Churn / attrition", "Retail banking"]),
    "38_dispute_chargeback_assistant": (
        "When a customer disputes a card payment (item never arrived, cancelled subscription still charged), the bank raises a chargeback through Visa/Mastercard.",
        "Card disputes / chargeback operations.",
        "Each network has strict reason codes, deadlines and evidence rules; mistakes mean the bank loses the dispute.",
        ["Chargeback", "Reason code", "MCC"]),
    "39_multilingual_faq_rag": (
        "Customers ask the same product questions (fees, limits, PIN reset) in many languages.",
        "Customer service and digital channels.",
        "Maintaining FAQs and staff in every language is expensive.",
        ["Retail banking"]),
    "40_call_center_qa": (
        "Quality teams listen to a sample of calls to check agents verified customers securely, handled fraud correctly and treated customers well.",
        "Contact centre quality assurance and team leaders.",
        "Only a tiny fraction of calls can be reviewed manually; security failures can enable fraud.",
        ["Call quality assurance (QA)", "Card fraud / CNP", "Vulnerable customer"]),
    "41_swift_payment_validator": (
        "International payments travel as SWIFT messages. If a field is wrong (bad BIC, invalid IBAN), the payment fails automatic processing and someone must repair it by hand.",
        "Payments operations teams.",
        "Manual repairs are slow and costly, and some repairs need customer confirmation.",
        ["SWIFT / MT103", "STP (Straight-Through Processing)", "BIC / IBAN / IFSC", "Charges code (OUR/SHA/BEN)"]),
    "42_cash_flow_forecaster": (
        "Corporate bankers help business clients forecast cash for the coming weeks to spot shortfalls and arrange funding in time.",
        "Corporate relationship managers and transaction banking / treasury advisers.",
        "Running out of cash, even for a week, can sink a profitable business.",
        ["Cash flow forecasting", "Working capital"]),
    "43_reconciliation_exception_agent": (
        "Operations teams match every entry in the bank's ledger against bank statements daily. Anything that does not match (a 'break') must be investigated.",
        "Reconciliation / operations teams.",
        "Breaks pile up quickly; unresolved ones can hide errors, fraud or losses.",
        ["Reconciliation", "Nostro account"]),
    "44_trade_finance_lc_checker": (
        "Under a Letter of Credit, the bank pays the exporter only if their documents exactly match the LC terms. Checkers examine every document line by line.",
        "Trade finance document checkers and trade operations managers.",
        "Checking is meticulous manual work; missing a discrepancy means paying when the bank should not.",
        ["Letter of Credit (LC)", "UCP 600", "Discrepancy", "Bill of Lading (B/L)", "Incoterms (e.g. CIF)"]),
    "45_fx_hedging_advisor": (
        "Companies that buy or sell abroad face currency risk. Bank FX sales teams help them measure it and lock in rates with forwards or options.",
        "FX sales / treasury advisers for corporate clients.",
        "Clients need clear explanations of risk in their own currency, and advice must be about protection, not speculation.",
        ["FX exposure / hedging", "FX forward"]),
    "46_invoice_cheque_extractor": (
        "Banks and their business clients process piles of invoices and cheques, reading the details and checking them before paying or clearing.",
        "Payments / clearing operations, trade and accounts-payable teams.",
        "Manual keying is slow, and mismatched amounts are a common source of errors and fraud.",
        ["Cheque truncation / OCR", "BIC / IBAN / IFSC", "GSTIN"]),
    "47_financial_statement_analyzer": (
        "Before lending to or investing in a company, analysts study its financial statements to judge profitability, debt and cash generation.",
        "Credit analysts and equity / credit research analysts.",
        "Headline growth can hide weak cash flow or rising debt; spotting this takes careful ratio analysis.",
        ["Financial statements", "EBITDA / EBIT", "Margins", "Leverage (debt-to-equity)", "Liquidity ratios (current ratio)", "Free cash flow"]),
    "48_earnings_call_analyzer": (
        "After quarterly results, management hold an earnings call. Analysts and investors listen for changes in outlook and signs of trouble.",
        "Equity research, investor relations and credit analysts.",
        "Calls are long and the important signals are often subtle changes in wording.",
        ["Guidance", "NIM (Net Interest Margin)", "Delinquency / NPA / NPL"]),
    "49_internal_audit_assistant": (
        "Internal auditors test samples of transactions to check controls worked, e.g. that a different person approved each payment within their authority.",
        "Internal audit.",
        "Testing and report writing are labour-intensive; findings must follow a strict format for the audit committee.",
        ["Internal audit", "Maker-checker"]),
    "50_operational_risk_analyzer": (
        "Every operational loss or near miss (an IT outage, a keying error, a forged signature) is logged, classified and analysed to prevent repeats.",
        "Operational risk teams (Risk department).",
        "Inconsistent classification makes loss data unreliable for reporting and capital calculations.",
        ["Operational risk", "Basel event types"]),
}

# --------------------------------------------------------------------------- #
# How a bank works: departments, mapped to catalog categories
# --------------------------------------------------------------------------- #
AREAS = [
    ("credit", "Lending (Credit)",
     "The bank's main business: it takes deposits and lends them out at a higher interest rate. The difference is its profit. "
     "The skill is lending to people and businesses who will pay back, so credit teams assess, approve, monitor and collect loans."),
    ("fincrime", "Financial Crime Compliance",
     "Banks are legally required to stop criminals using them to launder money, finance terrorism, evade sanctions or commit fraud. "
     "They must know their customers, monitor transactions and report suspicions. Failures lead to multi-billion fines."),
    ("regulatory", "Regulation, Risk & Finance",
     "Because bank failures hurt everyone, regulators require banks to hold enough capital (to absorb losses) and liquidity (to pay what is due), "
     "provision for expected loan losses, validate their models, and report regularly. Risk and Finance teams run this."),
    ("wealth", "Wealth & Investment Management",
     "Fee-earning advice and investment services: understanding clients' goals and risk appetite, building portfolios and making sure "
     "every recommendation is suitable."),
    ("retail", "Retail Banking & Customer Experience",
     "Day-to-day banking for individuals: accounts, cards, loans and support through branches, apps and contact centres. "
     "Here the focus is service, fair treatment of customers and growing the relationship."),
    ("ops", "Treasury, Payments & Operations",
     "The 'plumbing': moving money domestically and internationally, trade finance for importers and exporters, FX, cash management "
     "for companies, and back-office matching and checking that keeps everything accurate."),
    ("enterprise", "Analytics, Research & Audit",
     "Functions that analyse companies (for lending or investing), and internal audit and operational risk, which check that "
     "the bank's own controls work."),
]

# --------------------------------------------------------------------------- #
# Flow diagram labels: (input data, what Python computes or decides, output).
# Use "" when Python does no maths or rules; add "rules_first" when rules run before an extraction.
# Agents and tools are read from app.py.
# --------------------------------------------------------------------------- #
FLOWS = {
    "01_credit_risk_assessment": ("Loan application + lending policy", "DTI · LTI · risk score · policy breaches", "Credit decision memo"),
    "02_loan_underwriting_assistant": ("Loan applications + policy", "", "Underwriting recommendation"),
    "03_sme_credit_memo_writer": ("SME financial statements", "DSCR · current ratio · leverage · margins", "Bank-style credit memo"),
    "04_credit_limit_optimizer": ("Cardholder usage & payments", "Eligibility rules · new limit", "Limit decision + customer explanation"),
    "05_collections_strategy_agent": ("Overdue accounts", "DPD bucket · propensity to pay · segment", "Fair collections strategy"),
    "06_early_warning_signals": ("Borrower account behaviour", "Trigger rules: overdrafts, bounces, downgrades", "Watch-list note per borrower"),
    "07_mortgage_prequalification_bot": ("Customer's income & debts", "", "How much you can borrow + EMI"),
    "08_loan_document_extractor": ("Payslip + bank statement text", "Salary vs. statement credit check", "Validated fields + mismatches"),
    "09_aml_transaction_monitoring": ("Customer profile + transactions", "AML rules: structuring, high-risk countries, CTR", "Close / escalate / file SAR"),
    "10_kyc_onboarding_verifier": ("Onboarding application + ID documents", "", "KYC checklist: pass / fail"),
    "11_sanctions_screening_assistant": ("Payment parties + watchlist", "Fuzzy name matching", "True match / false positive"),
    "12_sar_narrative_generator": ("Investigation case facts", "", "Regulator-ready SAR narrative"),
    "13_card_fraud_explainer": ("Card transactions + spending history", "Fraud score: velocity, geo-jump, MCC, amount", "Fraud explanation + action"),
    "14_tbml_detector": ("Trade invoices + shipping routes", "Unit price vs. benchmark · transhipment hubs", "TBML risk assessment"),
    "15_adverse_media_screening": ("News articles about a customer", "Highest severity → escalate for EDD?", "Per-article verdict + escalation"),
    "16_customer_risk_rating": ("Customer profiles", "Weighted factors → Low / Medium / High", "Risk rating + justification"),
    "17_mule_account_detector": ("Account activity", "Pass-through ratio · account age · counterparties", "Ranked mule suspects + actions"),
    "18_regulatory_reporting_agent": ("Quarterly regulatory return", "Validation rules · QoQ variance", "Submission commentary"),
    "19_basel_capital_calculator": ("Exposures + capital", "", "Capital ratios vs. minimums"),
    "20_liquidity_lcr_nsfr_monitor": ("Liquid assets + cash flows", "LCR · NSFR with haircuts & run-off rates", "ALCO note + actions"),
    "21_regulatory_change_tracker": ("New regulator circular + process list", "", "Impact assessment + gaps"),
    "22_stress_testing_narrator": ("Loan portfolio + scenarios", "PD / LGD shocks · losses · capital impact", "Board stress-test summary"),
    "23_ifrs9_ecl_calculator": ("Loan book", "", "IFRS 9 stages + ECL"),
    "24_policy_qa_rag": ("Bank policy documents", "", "Answer with source references"),
    "25_model_risk_validator": ("Credit model scores + outcomes", "Gini · KS · PSI · calibration", "Model validation report"),
    "26_wealth_advisor_agent": ("Client goals + model portfolios", "Future value · required monthly SIP", "Personalised investment plan"),
    "27_portfolio_rebalancer": ("Holdings + target allocation", "", "Rebalancing trades + reasons"),
    "28_risk_profiling_agent": ("Risk questionnaire answers", "Risk score · profile band", "Risk profile + inconsistencies"),
    "29_market_news_summarizer": ("Market news + client portfolios", "", "RM morning briefing"),
    "30_retirement_planner": ("Customer's age, savings & goal", "", "Retirement plan + gap"),
    "31_esg_investment_screener": ("Funds + client ESG preferences", "Exclusions · ESG score thresholds", "ESG fund shortlist"),
    "32_suitability_checker": ("Client profile + product proposals", "Risk, horizon & concentration rules", "Suitable / not suitable verdict", "rules_first"),
    "33_customer_support_agent": ("Customer's accounts & cards", "", "Answer + action taken"),
    "34_complaint_classifier": ("Customer complaints", "Routing table · SLA from severity", "Category, team & deadline"),
    "35_personal_finance_coach": ("Income + transactions", "Spend by category · 50/30/20 check", "Personal coaching tips"),
    "36_next_best_offer": ("Customers + product catalogue", "Product propensity scores", "Compliant offer messages"),
    "37_churn_retention_agent": ("Customer activity signals", "Churn risk score", "Retention plan + save offers"),
    "38_dispute_chargeback_assistant": ("Card transactions + reason codes", "", "Dispute summary + next steps"),
    "39_multilingual_faq_rag": ("Bank FAQ", "", "Answer in the customer's language"),
    "40_call_center_qa": ("Call transcript + QA checklist", "", "QA score + coaching feedback"),
    "41_swift_payment_validator": ("SWIFT payment message", "BIC / IBAN / amount validation", "Repair suggestions"),
    "42_cash_flow_forecaster": ("Inflows, outflows + known events", "", "13-week cash view + funding gap"),
    "43_reconciliation_exception_agent": ("Ledger + bank statement", "Match by amount, reference & date", "Break resolution plan"),
    "44_trade_finance_lc_checker": ("LC + invoice + bill of lading", "Field-by-field comparison", "Accept / reject presentation"),
    "45_fx_hedging_advisor": ("FX exposures + market rates", "", "Hedging advice"),
    "46_invoice_cheque_extractor": ("OCR text of cheque & invoice", "Words vs. figures · dates · IFSC", "Validated payment data"),
    "47_financial_statement_analyzer": ("Company financial statements", "Ratios · YoY growth", "Research report"),
    "48_earnings_call_analyzer": ("Earnings call transcript", "", "Earnings call note"),
    "49_internal_audit_assistant": ("Payment sample + approval limits", "Control tests: maker-checker, limits, SoD", "Audit report with ratings"),
    "50_operational_risk_analyzer": ("Operational risk incidents", "Aggregate losses by event type", "Incident summary"),
}

# --------------------------------------------------------------------------- #
# What the user asks in the sample conversation (explorer + READMEs), for use cases
# that process a batch of sample data instead of taking a typed question. Use cases
# that print their own Question / Customer / "Q:" / "You:" sections use those instead.
# --------------------------------------------------------------------------- #
ASK = {
    "01_credit_risk_assessment": "New personal loan application from Priya Sharma: 12 lakh for home renovation over 5 years. Should we approve it?",
    "03_sme_credit_memo_writer": "Write the credit memo for GreenLeaf Foods: a 25M working capital line plus a 15M term loan for their new packaging unit.",
    "04_credit_limit_optimizer": "Review cardholders C-201, C-202 and C-203. Who should get a limit change, and how do we explain it to them?",
    "05_collections_strategy_agent": "These four overdue loan accounts need a collections plan. What should we do with each, fairly?",
    "06_early_warning_signals": "Run the early warning scan on our corporate borrowers. Who needs to go on the watch-list?",
    "08_loan_document_extractor": "Here are Rohan Mehta's payslip and bank statement. Extract the details and check they match.",
    "09_aml_transaction_monitoring": "Our monitoring rules flagged Marco Rinaldi, a restaurant owner. Review the alerts: close, escalate or file a SAR?",
    "10_kyc_onboarding_verifier": "Verify the current onboarding application.",
    "11_sanctions_screening_assistant": "Screen today's payment parties against the sanctions watchlist. Are any hits real matches?",
    "12_sar_narrative_generator": "Case INV-2026-0912 on Daniel Okafor is confirmed suspicious. Draft the SAR narrative for the regulator.",
    "13_card_fraud_explainer": "Score today's card transactions for fraud and tell me what action to take on each.",
    "14_tbml_detector": "Check these three trade finance deals for trade-based money laundering red flags.",
    "15_adverse_media_screening": "Screen these news articles for adverse media on Rajiv Malhotra, MD of Horizon Infra Projects.",
    "16_customer_risk_rating": "Rate the AML risk of these customers and justify each rating for the file.",
    "17_mule_account_detector": "Which of these accounts look like money mules, and what should we do about them?",
    "18_regulatory_reporting_agent": "Validate the Q3-2026 capital and liquidity return against Q2 and draft the submission commentary.",
    "20_liquidity_lcr_nsfr_monitor": "What are our LCR and NSFR today? Write the note for ALCO.",
    "21_regulatory_change_tracker": "A new circular on digital lending (2026/14) just came out. What does it mean for our processes?",
    "22_stress_testing_narrator": "Run the stress scenarios on our loan portfolio and write the board summary.",
    "25_model_risk_validator": "Validate our retail credit scorecard: is it still performing well enough to keep using?",
    "26_wealth_advisor_agent": "Arjun and Meera Nair want a plan for their children's education and retirement. What do you recommend?",
    "27_portfolio_rebalancer": "Review my portfolio and rebalance if needed.",
    "28_risk_profiling_agent": "Here are the client's risk questionnaire answers. What is their risk profile, and is anything inconsistent?",
    "29_market_news_summarizer": "Prepare this morning's market briefing for our relationship managers, with talking points per client.",
    "31_esg_investment_screener": "Which funds fit my client's ESG preferences? Shortlist them and explain the trade-offs.",
    "32_suitability_checker": "We plan to offer Mrs. Lata Desai (71, conservative) these three products. Are they suitable?",
    "34_complaint_classifier": "Classify today's customer complaints and route each one to the right team with a deadline.",
    "35_personal_finance_coach": "Here's my spending for last month on a 5,200 take-home pay. How am I doing, and where can I save?",
    "36_next_best_offer": "What should we offer customers R-1, R-2 and R-3 next? Draft the messages.",
    "37_churn_retention_agent": "Which customers are at risk of leaving, and how do we keep them?",
    "40_call_center_qa": "QA this card-dispute call between agent Sam and a customer. What should Sam do better?",
    "41_swift_payment_validator": "This MT103 payment failed straight-through processing. What's wrong and how do we repair it?",
    "42_cash_flow_forecaster": "Give me the 13-week cash outlook and any funding needs.",
    "43_reconciliation_exception_agent": "Reconcile the general ledger against the bank statement and tell me how to clear the breaks.",
    "44_trade_finance_lc_checker": "Check this LC presentation from Shenzhen Lumen Electronics. Can we accept the documents?",
    "45_fx_hedging_advisor": "Analyse our FX exposures and recommend a hedging plan.",
    "46_invoice_cheque_extractor": "Extract the data from this scanned cheque and invoice, and check it is valid.",
    "47_financial_statement_analyzer": "Analyse Northwind Consumer Goods' last two years of financial statements and write a research report.",
    "48_earnings_call_analyzer": "Summarise Meridian Bank's Q3 FY26 earnings call. How confident did management sound, and what are the risks?",
    "49_internal_audit_assistant": "Test this quarter's payment sample against our approval controls and write the audit findings.",
    "50_operational_risk_analyzer": "Classify these operational risk incidents by Basel event type and summarise the losses.",
}
