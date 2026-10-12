# 🏦 Banking: 50 AI Use Cases

**Retail, corporate and investment banking.** 50 AI agents for credit, AML, regulatory reporting, wealth, customer service, treasury and audit.

[⬅ All industries](../README.md) · [New to banking?](#-new-to-banking) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-50-success)
![CrewAI](https://img.shields.io/badge/CrewAI-22-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-28-1C3C3C)

```bash
# from the repo root, with Ollama running
python 01_banking/01_credit_risk_assessment/app.py
```

---

## 🎓 New to banking?

**How a bank makes money:** it pays savers a low interest rate on deposits and lends that money to people and
businesses at a higher rate. The difference (the *net interest margin*) is its main income. It also earns *fees* from
payments, cards, wealth advice, trade finance and FX.

**What makes it hard:**
1. **Risk is the job.** Profit disappears if borrowers don't repay (*credit risk*), if the bank runs out of cash (*liquidity risk*), or if processes, people or systems fail (*operational risk*).
2. **Heavily regulated.** Banks hold other people's money and are central to the economy, so regulators set rules on capital, liquidity, fighting financial crime and treating customers fairly. Much of a bank's work (and many use cases here) exists to meet these rules.

Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[Banking Primer & glossary](PRIMER.md)** (109 terms).

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

## 📚 Use Cases

### 🏦 Credit & Lending

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 01 | **Credit Risk Assessment Agent** | Scores a retail loan applicant and writes a credit decision memo with risk grade and conditions. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_credit_risk_assessment/) |
| 02 | **Loan Underwriting Assistant** | Underwriter copilot that checks DTI, LTV and policy rules through tools before recommending a decision. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_loan_underwriting_assistant/) |
| 03 | **SME Credit Memo Writer** | Turns SME financials into a bank-style credit memo (business profile, ratios, risks, mitigants). | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_sme_credit_memo_writer/) |
| 04 | **Credit Card Limit Optimizer** | Recommends credit-limit increases or decreases per card holder with an explainable reason. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_credit_limit_optimizer/) |
| 05 | **Collections & Recovery Strategist** | Segments delinquent accounts and designs a compliant, empathetic collection strategy per segment. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_collections_strategy_agent/) |
| 06 | **Early Warning Signals (EWS) Monitor** | Detects early signs of stress in a corporate loan book and drafts watch-list commentary. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_early_warning_signals/) |
| 07 | **Mortgage Pre-Qualification Bot** | Conversational assistant that estimates how much a customer can borrow and the monthly EMI. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_mortgage_prequalification_bot/) |
| 08 | **Loan Document Extractor** | Extracts structured fields from payslips and bank statements for loan processing. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_loan_document_extractor/) |

### 🕵️ Financial Crime & Compliance

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 09 | **AML Transaction Monitoring Agent** | Detects structuring, rapid movement and high-risk-geography patterns and triages the alert. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_aml_transaction_monitoring/) |
| 10 | **KYC Onboarding Verifier** | Checks customer onboarding data for completeness, document validity and consistency. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_kyc_onboarding_verifier/) |
| 11 | **Sanctions Screening Assistant** | Reduces false positives in name screening by adjudicating fuzzy matches with secondary identifiers. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](11_sanctions_screening_assistant/) |
| 12 | **SAR Narrative Generator** | Drafts a Suspicious Activity Report narrative (who, what, when, where, why) from case facts. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](12_sar_narrative_generator/) |
| 13 | **Card Fraud Detection Explainer** | Scores card transactions for fraud and explains each alert for analysts and customers. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](13_card_fraud_explainer/) |
| 14 | **Trade-Based Money Laundering Detector** | Flags over/under-invoicing and suspicious trade routes in trade finance transactions. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](14_tbml_detector/) |
| 15 | **Adverse Media Screening** | Classifies news articles about a customer for financial-crime relevance and severity. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](15_adverse_media_screening/) |
| 16 | **Customer Risk Rating (CRR)** | Computes a customer ML/TF risk rating and justifies it for periodic KYC review. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](16_customer_risk_rating/) |
| 17 | **Money Mule Account Detector** | Identifies likely mule accounts from pass-through behaviour and new-account signals. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](17_mule_account_detector/) |

### 📜 Regulatory & Risk Reporting

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 18 | **Regulatory Reporting Agent** | Validates a regulatory return, explains period-on-period movements and drafts the submission commentary. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](18_regulatory_reporting_agent/) |
| 19 | **Basel III Capital Calculator Assistant** | Answers capital-adequacy questions by computing RWA, CET1, Tier 1 and total capital ratios. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](19_basel_capital_calculator/) |
| 20 | **Liquidity LCR / NSFR Monitor** | Calculates LCR and NSFR and produces an ALCO liquidity commentary. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](20_liquidity_lcr_nsfr_monitor/) |
| 21 | **Regulatory Change Impact Analyzer** | Reads a new regulatory circular and maps obligations to impacted business units and controls. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](21_regulatory_change_tracker/) |
| 22 | **Stress Testing Scenario Narrator** | Applies macro stress scenarios to a portfolio and writes the stress-test narrative for the board. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](22_stress_testing_narrator/) |
| 23 | **IFRS 9 ECL Calculator & Explainer** | Stages loans (1/2/3) and calculates expected credit loss, then explains drivers. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](23_ifrs9_ecl_calculator/) |
| 24 | **Bank Policy & Procedure Q&A (RAG)** | Answers staff questions from internal credit, KYC and operations policies with citations. | LangChain | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](24_policy_qa_rag/) |
| 25 | **Model Risk Validation Assistant** | Reviews a credit model's performance metrics and drafts an SR 11-7 style validation report. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](25_model_risk_validator/) |

### 📈 Wealth & Investment Management

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 26 | **AI Wealth Advisor** | Builds a goals-based investment plan for a client with suitability checks. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](26_wealth_advisor_agent/) |
| 27 | **Portfolio Rebalancing Agent** | Detects drift from target allocation and proposes tax-aware rebalancing trades. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](27_portfolio_rebalancer/) |
| 28 | **Investor Risk Profiling Agent** | Scores a risk questionnaire and explains the resulting risk profile to the client. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](28_risk_profiling_agent/) |
| 29 | **Market News Briefing for RMs** | Summarises market news and maps it to client holdings for relationship managers. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](29_market_news_summarizer/) |
| 30 | **Retirement Planning Assistant** | Projects a retirement corpus, gap and required monthly savings. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](30_retirement_planner/) |
| 31 | **ESG Investment Screener** | Screens a fund universe against ESG preferences and exclusions. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](31_esg_investment_screener/) |
| 32 | **Suitability & Mis-selling Checker** | Checks whether a recommended product is suitable for a client's profile before sale. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](32_suitability_checker/) |

### 🙋 Retail Banking & Customer Experience

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 33 | **Banking Customer Support Agent** | Answers balance, transaction and card questions and can block a lost card. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](33_customer_support_agent/) |
| 34 | **Complaint Classifier & Router** | Classifies complaints by product, issue, severity and regulatory reportability and routes them. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](34_complaint_classifier/) |
| 35 | **Personal Finance Coach** | Analyses spending and gives personalised saving tips and a budget. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](35_personal_finance_coach/) |
| 36 | **Next Best Offer / Cross-sell** | Recommends the next best product for each customer with a personalised message. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](36_next_best_offer/) |
| 37 | **Customer Churn Retention Agent** | Identifies customers likely to leave and designs retention actions. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](37_churn_retention_agent/) |
| 38 | **Dispute & Chargeback Assistant** | Guides a card dispute, determines the reason code and drafts the chargeback case. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](38_dispute_chargeback_assistant/) |
| 39 | **Multilingual Banking FAQ (RAG)** | Answers product FAQs in the customer's language (e.g. Hindi, Spanish, French). | LangChain | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](39_multilingual_faq_rag/) |
| 40 | **Call Center QA Analyzer** | Scores call transcripts for compliance, empathy and resolution and coaches the agent. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](40_call_center_qa/) |

### 💱 Treasury, Payments & Operations

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 41 | **SWIFT Payment Repair Assistant** | Validates MT103 payment messages and suggests repairs for failed STP. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](41_swift_payment_validator/) |
| 42 | **Corporate Cash Flow Forecaster** | Forecasts a corporate client's 13-week cash position and highlights funding gaps. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](42_cash_flow_forecaster/) |
| 43 | **Reconciliation Exception Agent** | Matches ledger vs. bank statement entries and investigates the breaks. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](43_reconciliation_exception_agent/) |
| 44 | **Letter of Credit Document Checker** | Checks LC presentation documents for discrepancies against UCP 600 terms. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](44_trade_finance_lc_checker/) |
| 45 | **FX Hedging Advisor** | Measures a corporate's FX exposure and suggests a hedging approach. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](45_fx_hedging_advisor/) |
| 46 | **Invoice & Cheque Data Extractor** | Extracts fields from invoices and cheques (OCR text) and validates them. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](46_invoice_cheque_extractor/) |

### 🏢 Enterprise Analytics & Audit

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 47 | **Financial Statement Analyzer** | Analyses a company's income statement and balance sheet and writes an equity-style summary. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](47_financial_statement_analyzer/) |
| 48 | **Earnings Call Analyzer** | Extracts guidance, sentiment and risks from an earnings call transcript. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](48_earnings_call_analyzer/) |
| 49 | **Internal Audit Assistant** | Tests a sample of transactions against controls and drafts audit findings. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](49_internal_audit_assistant/) |
| 50 | **Operational Risk Incident Analyzer** | Classifies operational-loss incidents into Basel event types and suggests root cause and controls. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](50_operational_risk_analyzer/) |

## 🧩 By Framework

### ![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) CrewAI (22)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 01 | Credit Risk Assessment Agent | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_credit_risk_assessment/) |
| 03 | SME Credit Memo Writer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_sme_credit_memo_writer/) |
| 05 | Collections & Recovery Strategist | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_collections_strategy_agent/) |
| 09 | AML Transaction Monitoring Agent | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_aml_transaction_monitoring/) |
| 12 | SAR Narrative Generator | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](12_sar_narrative_generator/) |
| 14 | Trade-Based Money Laundering Detector | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](14_tbml_detector/) |
| 17 | Money Mule Account Detector | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](17_mule_account_detector/) |
| 18 | Regulatory Reporting Agent | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](18_regulatory_reporting_agent/) |
| 21 | Regulatory Change Impact Analyzer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](21_regulatory_change_tracker/) |
| 22 | Stress Testing Scenario Narrator | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](22_stress_testing_narrator/) |
| 25 | Model Risk Validation Assistant | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](25_model_risk_validator/) |
| 26 | AI Wealth Advisor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](26_wealth_advisor_agent/) |
| 29 | Market News Briefing for RMs | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](29_market_news_summarizer/) |
| 31 | ESG Investment Screener | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](31_esg_investment_screener/) |
| 36 | Next Best Offer / Cross-sell | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](36_next_best_offer/) |
| 37 | Customer Churn Retention Agent | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](37_churn_retention_agent/) |
| 40 | Call Center QA Analyzer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](40_call_center_qa/) |
| 43 | Reconciliation Exception Agent | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](43_reconciliation_exception_agent/) |
| 44 | Letter of Credit Document Checker | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](44_trade_finance_lc_checker/) |
| 47 | Financial Statement Analyzer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](47_financial_statement_analyzer/) |
| 48 | Earnings Call Analyzer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](48_earnings_call_analyzer/) |
| 49 | Internal Audit Assistant | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](49_internal_audit_assistant/) |

### ![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) LangChain (28)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 02 | Loan Underwriting Assistant | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_loan_underwriting_assistant/) |
| 04 | Credit Card Limit Optimizer | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_credit_limit_optimizer/) |
| 06 | Early Warning Signals (EWS) Monitor | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_early_warning_signals/) |
| 07 | Mortgage Pre-Qualification Bot | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_mortgage_prequalification_bot/) |
| 08 | Loan Document Extractor | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_loan_document_extractor/) |
| 10 | KYC Onboarding Verifier | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_kyc_onboarding_verifier/) |
| 11 | Sanctions Screening Assistant | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](11_sanctions_screening_assistant/) |
| 13 | Card Fraud Detection Explainer | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](13_card_fraud_explainer/) |
| 15 | Adverse Media Screening | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](15_adverse_media_screening/) |
| 16 | Customer Risk Rating (CRR) | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](16_customer_risk_rating/) |
| 19 | Basel III Capital Calculator Assistant | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](19_basel_capital_calculator/) |
| 20 | Liquidity LCR / NSFR Monitor | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](20_liquidity_lcr_nsfr_monitor/) |
| 23 | IFRS 9 ECL Calculator & Explainer | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](23_ifrs9_ecl_calculator/) |
| 24 | Bank Policy & Procedure Q&A (RAG) | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](24_policy_qa_rag/) |
| 27 | Portfolio Rebalancing Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](27_portfolio_rebalancer/) |
| 28 | Investor Risk Profiling Agent | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](28_risk_profiling_agent/) |
| 30 | Retirement Planning Assistant | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](30_retirement_planner/) |
| 32 | Suitability & Mis-selling Checker | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](32_suitability_checker/) |
| 33 | Banking Customer Support Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](33_customer_support_agent/) |
| 34 | Complaint Classifier & Router | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](34_complaint_classifier/) |
| 35 | Personal Finance Coach | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](35_personal_finance_coach/) |
| 38 | Dispute & Chargeback Assistant | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](38_dispute_chargeback_assistant/) |
| 39 | Multilingual Banking FAQ (RAG) | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](39_multilingual_faq_rag/) |
| 41 | SWIFT Payment Repair Assistant | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](41_swift_payment_validator/) |
| 42 | Corporate Cash Flow Forecaster | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](42_cash_flow_forecaster/) |
| 45 | FX Hedging Advisor | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](45_fx_hedging_advisor/) |
| 46 | Invoice & Cheque Data Extractor | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](46_invoice_cheque_extractor/) |
| 50 | Operational Risk Incident Analyzer | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](50_operational_risk_analyzer/) |

---

[⬅ Back to all industries](../README.md)
