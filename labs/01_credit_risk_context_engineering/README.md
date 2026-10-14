# Context Engineering for Credit Risk: Hands-on Lab

[← All labs](../README.md) · [← Ollama AI Industry Use Cases](../../README.md)

> **Note:** unlike the rest of this repo, this lab does **not** use Ollama. It runs on Databricks Free Edition and calls the hosted pay-per-token models that the workspace provides.

**Same model, better context → smarter AI.**

This lab shows *why* an AI assistant gets credit-risk questions wrong on raw data, and how building a **context and semantic layer**, one step at a time, makes it accurate and safe. It follows the six stages of the *Context Engineering Studio · Credit Risk* design.

It is **not** a Databricks tutorial. Databricks Free Edition is just where the lab runs.

## The story
In module 00, an AI that sees only the raw tables is asked 5 questions. It fails. Each module then adds one layer of context, and the same 5 questions are asked again:

| Module | Context step | Fixes |
|---|---|---|
| 00 Baseline | none | — (expect about 0–1 out of 5) |
| 01 Discover | Entity map: which table is which, which to avoid | wrong or stale table |
| 02 Standardize | Glossary, PII classification, quality rules | misread codes, PII leaks |
| 03 Attach documents | Policies and metric definitions | generic answers instead of *our* policy |
| 04 Semantic layer | Certified metrics + ontology | improvised, inconsistent formulas |
| 05 Enrich & publish | AI-drafted, steward-approved vocabulary | "bad loans", "West" not understood |
| 06 Grounded agent | Guardrails | credit-decision opinions → 5 out of 5 |

The model and the prompt never change. Only the context does.

**Don't want to run it?** 👉 **[See the walkthrough with screenshots](docs/WALKTHROUGH.md)** from a real run: 0.5 → 0.5 → 1.5 → 2.5 → 4.5 → 4.5 → **5 / 5**. The full notebooks with outputs are in `rendered/` (open in a browser) and in the workspace folder `credit-risk-context-lab/With outputs (read-only)`.

![Score after each step](docs/screenshots/06_05.png)

## Setup (5 minutes)
1. Sign up for **Databricks Free Edition**: <https://www.databricks.com/learn/free-edition>
2. In the workspace, go to **Workspace → Create → Git folder** and paste this repository's URL. This clones the whole repo, so open `labs/01_credit_risk_context_engineering/lab/` inside it. Alternatively, import just the `lab/` folder as files.
3. Open `lab/00_Baseline_AI_Without_Context` and click **Run all**. Then run 01 → 06 in order.

Total time is about 60–90 minutes. Each scorecard run takes 1–2 minutes because it makes about 6 AI calls.

**Important on Free Edition:**
- Run the modules **one at a time, in order**. Each module checks that the previous one has finished.
- Attach each notebook to **Serverless**, not the SQL warehouse.
- Free Edition allows very little serverless compute at once, so close other running notebooks or SQL warehouses first.

## What's in the repo
```
lab/
  00_Baseline_AI_Without_Context … 06_Grounded_Agent, 99_Cleanup   the notebooks (run in order)
  _setup.py           loaded by every notebook
  lab_utils.py        all logic (learners don't need to read it)
  datagen.py          synthetic data with built-in "traps"
  context/            the context assets: entity map, glossary, ontology, metrics, synonyms, guardrails, docs
docs/WALKTHROUGH.md   step-by-step results with screenshots (no run needed)
rendered/             all notebooks with outputs, as HTML (open in a browser or import into Databricks)
output/               raw HTML exports from the reference run
tools/
  finalize_exports.py turns output/ exports into rendered/ (applies the current notes, clears stale errors)
  run_and_capture.py  runs the whole lab as one job and exports the results (needs Jobs enabled on the account)
```

## Notes for the instructor
- **Data is synthetic.** It has 12,000 accounts and monthly snapshots from Jan 2024 to Sep 2026. Traps are built in on purpose:
  - Metro 2 delinquency codes
  - charged-off balances that look outstanding
  - a stale backup table
  - an Auto vintage (2025-04) that only shows up as worst when vintages are compared at equal age
- **Model:** the lab picks the first available pay-per-token chat model, preferring Claude, then GPT-OSS, then Llama. To force a specific one, run `lab.use_model("<endpoint-name>")` after `%run ./_setup`.
- **Results vary a little between runs.** LLM answers aren't fully deterministic. Scores generally rise step by step, but a question can occasionally pass early or flip. Treat that as a teaching moment: steps 04 and 06 exist to make answers *consistent*, not just correct once.
- **To see exactly what the AI receives,** run `lab.show_context("your question")`.
- If the account can't create a new catalog, the lab uses the `workspace` catalog with `crl_*` schemas instead.
- **Local check, no Databricks needed:** `cd lab && python lab_utils.py` validates the context files, the data traps and the grader.
