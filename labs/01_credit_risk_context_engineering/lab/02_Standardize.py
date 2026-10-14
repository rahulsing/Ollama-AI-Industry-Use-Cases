# Databricks notebook source
# MAGIC %md
# MAGIC # 02 · Standardize: give every column a business meaning
# MAGIC
# MAGIC **The problem:** the AI found the right table, but it still guesses what the columns mean:
# MAGIC - `DLQ_CD` holds Metro 2 codes (`71` = 30–59 days late), not a number of days.
# MAGIC - `CUR_BAL` on charged-off rows is money already written off. It must not count as outstanding.
# MAGIC - `R01` means West. Nothing in the data says so.
# MAGIC - `MBR_NM` and `SSN_L4` are personal data, and nothing marks them as private.
# MAGIC
# MAGIC **The context step:** bind the **business glossary** to the columns (definition and term), **classify** sensitive data, and enforce a **data-quality contract** so the data keeps meaning what the glossary says.

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · Check the data-quality contract
# MAGIC Definitions only help if the data respects them. These rules come from the data product's quality contract.

# COMMAND ----------

lab.check_quality()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Each rule turns a definition into something testable. For example, "a delinquency code must be one of the known Metro 2 codes". With zero violations, the data is safe to describe.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Publish the glossary and classifications (about 1 minute)

# COMMAND ----------

lab.publish_glossary()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Every column now explains itself: what it means, the glossary term it maps to, its industry (FIBO) alignment, and its sensitivity class (`PII`, `Restricted`, `Internal`). The quality rules are now **enforced**, so bad data is rejected at load time.
# MAGIC
# MAGIC > 🔧 *On Databricks:* column comments, column tags and `CHECK` constraints in Unity Catalog.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · AI Scorecard

# COMMAND ----------

lab.run_scorecard("02 + Glossary")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What improved, and what didn't
# MAGIC - **Q1** should improve: the AI now knows which codes mean 30+ days late and that charged-off balances must be excluded.
# MAGIC - **Q5** should be partly safer: names and SSNs are now marked as PII.
# MAGIC - **Q2** (our charge-off policy) still fails. That knowledge isn't in any table. It lives in a policy document.
# MAGIC
# MAGIC > 🔑 **Key takeaway:** A glossary turns columns into business language, and classification tells the AI what it must protect.
# MAGIC
# MAGIC ➡️ Next: **03_Attach_Documents**
