# Lab walkthrough: what happens at each step (no need to run anything)

All screenshots come from a real run on Databricks Free Edition. The model was `databricks-gpt-oss-120b`, and the data is synthetic.

**The idea:** we ask an AI the same 5 credit-risk questions after every step. The model and the prompt never change. Only the **context** we build changes.

![Score after each step](screenshots/06_05.png)

| Step | Score | What changed |
|---|---|---|
| 00 Baseline | 0.5 / 5 | Raw tables only. The AI gives up, guesses, or leaks SSNs. |
| 01 Discover | 0.5 / 5 | Finds the right tables, but still can't read the codes. |
| 02 Standardize | 1.5 / 5 | Glossary added: **delinquency rate now exactly right** |
| 03 Documents | 2.5 / 5 | Policy added: **states our charge-off rules** |
| 04 Semantic layer | 4.5 / 5 | Certified metrics added: **vintage and "bad loans" right** |
| 05 Enrich & publish | 4.5 / 5 | Approved vocabulary: business phrasing now handled reliably |
| 06 Guardrails | **5 / 5** | Scope rules: **no PII, no credit decisions** |

---

## How the lab works
```
 question ──► [guardrail check] ──► model + SYSTEM PROMPT + CONTEXT ──► SQL or answer ──► grader ──► ✅ ⚠️ ❌
                                                   ▲
                       build_context() reads ONLY what has been published:
                       catalog descriptions & tags · documents · metric views · vocabulary · rules
```
- **One fixed prompt, one fixed model.** Every module asks the same 5 questions with the same system prompt. The only thing that grows is the **CONTEXT** section, which is assembled automatically from what has been published so far.
- **Context lives in the catalog, not in the notebook.**
  - Table and column descriptions and sensitivity tags are stored in Unity Catalog.
  - Everything else (documents, metrics, vocabulary, rules) goes into a small **context registry** table, with a `draft` or `published` status.
  - The AI only ever sees `published` items.
- **Honest grading.** The correct answers are computed directly from the data. The grader also computes the typical *wrong* answers: counting accounts instead of balances, including charge-offs, comparing vintages to date, and so on. So when the AI is wrong, the scorecard says *why*.
- **Realistic data with built-in traps.** The lab uses 12,000 synthetic loan accounts with 33 months of snapshots, designed to look like a core-banking extract. It has coded columns, a stale backup table, a marketing table mixed in, member names and SSNs, and charged-off balances that look like they're still outstanding.

---

## 00 · Baseline: AI without context
The AI sees only raw source tables, with cryptic columns and coded values:

![Raw tables](screenshots/00_02.png)

Asked the 5 questions, it **gives up** on the delinquency rate, doesn't know our charge-off policy, ranks vintages by dollar losses, reports $95.9M of "bad loans" (roughly the whole book), and **returns member names and SSNs**:

![Baseline scorecard](screenshots/00_04.png)

> **How we built it**
> - Generated the synthetic source tables (`t_acct`, `t_acct_mth`, `t_mbr`, `t_prd`, `t_org`, plus a stale `t_acct_mth_bkp` and an unrelated `t_cmp_resp`), loaded into `credit_risk_lab.raw`.
> - Created two lab tables: `context.registry`, which holds every context asset, and `context.scorecard`, which records every graded answer.
> - Ran the first scorecard with **no context**: only table names, column names and two sample rows per table.

---

## 01 · Discover: which table is which?
The AI proposes what each table holds, and a data owner confirms. Only a person knows that the backup table stopped refreshing, or that the campaign table is out of scope:

![AI discovery vs confirmed map](screenshots/01_01.png)

The score doesn't move yet. The AI now finds the right table, but returns **0.0%**, because it still can't read `DLQ_CD` codes:

![Scorecard 01](screenshots/01_03.png)

> **How we built it**
> - **AI-assisted discovery:** the model received each table's columns, sample rows and date range, and guessed its business entity, with a confidence score.
> - **Human confirmation:** the confirmed map (`context/entity_map.yaml`) records each table's entity, grain and status (*use / deprecated / out of scope*).
> - **Published to the catalog** as a table description and tags, with the data range profiled automatically:
>   ```sql
>   COMMENT ON TABLE raw.t_acct_mth_bkp IS '[Account Snapshot (backup copy)] DEPRECATED stale backup ...
>     Status: DEPRECATED. Data range: 2024-01-31 to 2025-12-31.';
>   ALTER TABLE raw.t_acct_mth_bkp SET TAGS ('business_entity' = 'Account Snapshot (backup copy)', 'lab_status' = 'deprecated');
>   ```

---

## 02 · Standardize: give every column a business meaning
Glossary definitions, sensitivity classes and quality rules are written into the catalog:

![Glossary published](screenshots/02_02.png)

**Q1 is now exactly right (1.59%).** Q3 falls into a classic trap: it compares vintages *to date*, and older vintages always look worse. Q5 still leaks SSNs even though they're tagged PII. A label informs. It doesn't enforce.

![Scorecard 02](screenshots/02_03.png)

> **How we built it**
> - **Business glossary bound to columns** (`context/glossary.yaml`). Each of the 26 columns got a term, a definition, a sensitivity class (`PII`, `Restricted`, `Internal`) and, where one exists, an industry (FIBO) alignment:
>   ```sql
>   ALTER TABLE raw.t_acct_mth ALTER COLUMN DLQ_CD COMMENT 'Delinquency Status: Metro 2 account status code.
>     11 = current, 71 = 30-59 DPD, 78 = 60-89 DPD ... 30+ DPD = codes 71,78,80,82,83.';
>   ALTER TABLE raw.t_mbr ALTER COLUMN SSN_L4 SET TAGS ('glossary_term' = 'SSN Last Four', 'classification' = 'PII');
>   ```
> - **Data-quality contract:** 4 rules were checked first (0 violations), then enforced so bad data can't be loaded:
>   ```sql
>   ALTER TABLE raw.t_acct_mth ADD CONSTRAINT valid_delinquency_code
>     CHECK (DLQ_CD IN ('11','71','78','80','82','83','97','13'));
>   ```
> - The key fix for Q1 was the `CUR_BAL` definition, which warns that charged-off balances are no longer outstanding and must be excluded.

---

## 03 · Attach documents: knowledge that isn't in the data
Policies and definitions are stored, split into sections and retrieved for each question. Asked about charge-offs, the AI now answers with **our** policy (90/120/150 days) instead of the textbook one:

![Policy answer](screenshots/03_02.png)

![Scorecard 03](screenshots/03_03.png)

> **How we built it**
> - Wrote three reference documents (`context/docs/`): the **charge-off & recovery policy**, the **metric definitions** (for example, delinquency is balance-weighted and vintages are compared at equal age) and the **Metro 2 status-code crosswalk**.
> - Stored them in a governed Unity Catalog **Volume**: `/Volumes/credit_risk_lab/context/docs/`.
> - **Split** them by section into 10 chunks and published them to the registry.
> - **Retrieval:** for each question, the most relevant chunks are added to the context. The lab uses a simple keyword match. At scale you would use `ai_parse_document` for PDFs and a Vector Search index.

---

## 04 · Semantic layer: one certified way to calculate each number
Metrics are defined once, with an owner, a formula and the **allowed values** the AI must use:

![Semantic layer](screenshots/04_01.png)

> **A lesson from our test run:** in the first attempt, the metric views existed but their allowed values weren't published. The AI filtered with raw codes (`product IN ('V31','V32')`), every answer came back empty, and the score *dropped*. Publishing the values fixed it.

The AI now picks the certified metric instead of improvising. **Vintage 2025-04** is correctly identified as the worst at 12 months on book, and bad loans in the West are exactly **$628,433**:

![Scorecard 04](screenshots/04_03.png)

> **How we built it**
> - **Conformed view** `gold.loan_snapshot`: decodes codes into business values (`V31/V32` → `'Auto'`, `R01` → `'West'`) and derives `vintage`, `months_on_book`, `outstanding_balance` (open accounts only), `dpd30_balance`, `dpd60_balance` and `cum_charge_off_amount`.
> - **Two certified Metric Views**, `semantic.portfolio_performance` and `semantic.vintage_performance`, are defined in YAML (`context/metrics/`):
>   ```yaml
>   measures:
>     - name: dpd30_rate
>       expr: SUM(dpd30_balance) / SUM(outstanding_balance)
>     - name: dpd60_balance
>       expr: SUM(dpd60_balance)
>   ```
>   Every measure has an owner and a definition (`metric_catalog.yaml`). An example definition: *"compare vintages only at the same months_on_book; standard = 12."*
> - **Allowed values and rules** were published with the metrics: `product: 'Auto','Cards','Personal Loan'`, `division: 'East','West'`, the latest `snapshot_date`, and "default to the latest month".
> - **Ontology** (`context/ontology.yaml`): 10 business entities and 9 relationships (Member → holds → Loan Account → observed in → Snapshot …), aligned to FIBO where a match exists.
> - The AI now writes queries like `SELECT MEASURE(dpd30_rate) FROM semantic.portfolio_performance WHERE product = 'Auto' ...` instead of re-deriving the formula.

---

## 05 · Enrich & publish: speak the business's language
The AI drafts synonyms, and the steward adds institutional meaning ("bad loans" = 60+ days past due, excluding charge-offs):

![Drafts](screenshots/05_01.png)

Same question, before and after approval. "Problem-loan book in the western region" goes from a **wrong guess ($2.0M, using 30+ days)** to the **certified $628,433**:

| Before approval | After approval |
|---|---|
| ![before](screenshots/05_02.png) | ![after](screenshots/05_04.png) |

> **How we built it**
> - **AI drafting:** the model proposed 4 everyday phrases for each certified metric (24 drafts). They are fast but generic.
> - **Steward curation** (`context/synonyms.yaml`): added the institution's own vocabulary that no model could guess. "Bad loans / bad book / problem loans" = 60+ DPD balance excluding charge-offs, "West / western region / R01" = `division = 'West'`, and "performing worst" = highest loss rate at 12 months on book.
> - **Publish gate:** every AI draft and steward entry went into the registry as **`draft`**, which the AI can't see. Steward approval switched them to **`published`** and tagged the metric views `certified = true` with a named steward.
> - The before and after test above shows that the gate matters: the same question was answered wrongly while the vocabulary was a draft, and correctly once it was published.

---

## 06 · Grounded agent: answer well, and know where to stop
Scope rules are checked *before* a question reaches the model:

![PII refused](screenshots/06_02.png)
![Decision refused](screenshots/06_03.png)

![Final scorecard](screenshots/06_04.png)

> **How we built it**
> - **Scope rules** (`context/guardrails.yaml`) taken from the governance policy: no credit decisions, no member-level personal data, no predictions before model-risk review. Each rule has a **title**, a **reason** and a **pattern**:
>   ```yaml
>   - id: pii
>     title: Member-level personal data is blocked
>     pattern: '\b(ssn|social security|member names?|names? (of|and)|list (the )?(members|customers|borrowers))'
>     why: Only aggregate, certified metrics are served. Columns classified PII are never returned.
>   ```
> - **Two layers of enforcement:**
>   1. A **pre-check** blocks matching questions before they reach the model, and returns the reason and the policy.
>   2. The same rules are added to the model's context ("never return PII columns", "prefer certified metric views").
> - This is why Q5 finally passed. Tagging columns as PII in step 02 *described* the risk, but only an enforced rule *prevented* it.

### Before vs. after
![Before vs after](screenshots/06_06.png)

> 🔑 **The model never changed. Every improvement came from context that was built, reviewed and published.**

---

## What we built, in one table

| Step | Context asset | Stored as (Databricks) | Source file |
|---|---|---|---|
| 01 | Entity map | Table comments + tags | `context/entity_map.yaml` |
| 02 | Glossary, classifications, quality rules | Column comments, column tags, `CHECK` constraints | `context/glossary.yaml` |
| 03 | Reference documents | UC Volume + chunks in the registry | `context/docs/*.md` |
| 04 | Semantic layer + ontology | View + 2 Metric Views + registry | `context/metrics/*.yaml`, `context/ontology.yaml` |
| 05 | Business vocabulary | Registry (draft → published) + `certified` tag | `context/synonyms.yaml` |
| 06 | Guardrails | Registry + pre-check before the model | `context/guardrails.yaml` |

### Where to see the full notebooks with outputs
- **In Databricks:** `/Users/<you>/credit-risk-context-lab/With outputs (read-only)/`
- **In this repo:** `rendered/*.html`, which opens in any browser.
