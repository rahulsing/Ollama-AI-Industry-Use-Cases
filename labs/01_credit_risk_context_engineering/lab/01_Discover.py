# Databricks notebook source
# MAGIC %md
# MAGIC # 01 · Discover: which table is which?
# MAGIC
# MAGIC **The problem:** in the baseline, the AI had to guess what each table holds. It can't tell the live snapshot table from a stale backup, or loan data from marketing data.
# MAGIC
# MAGIC **The context step:** build an **entity map** that links every raw table to a business entity (Loan Account, Member, Account Snapshot…), with its grain, data range and status (*use*, *deprecated*, *out of scope*).
# MAGIC
# MAGIC *Credit-risk example:* `t_acct_mth` = "Account Snapshot, one row per account per month-end, use for reporting". `t_acct_mth_bkp` = "deprecated, stopped refreshing Dec 2025".

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · Let AI propose, let a person confirm
# MAGIC AI is good at a first draft of discovery. A data owner confirms it.

# COMMAND ----------

lab.discover_with_ai()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC The AI recognised most tables from their columns. It **can't know** things like "this backup stopped refreshing" or "this table is out of scope". That knowledge sits with people, which is why discovery needs a human confirmation step.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Publish the confirmed entity map

# COMMAND ----------

lab.publish_entity_map()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Every table now carries its business entity, grain, data range and status **in the catalog itself**. Anyone, or any AI, that reads the catalog now gets this knowledge for free.
# MAGIC
# MAGIC > 🔧 *On Databricks:* stored as Unity Catalog table comments and tags.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · AI Scorecard

# COMMAND ----------

lab.run_scorecard("01 + Entity map")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What improved, and what didn't
# MAGIC The AI should now pick the **right table** and avoid the backup. Most answers are probably still wrong, though: it knows *where* the data is but not *what the columns mean*. `DLQ_CD = '78'` is still just a code.
# MAGIC
# MAGIC > 🔑 **Key takeaway:** Discovery tells the AI *where* to look. It doesn't yet tell it *how to read* what it finds.
# MAGIC
# MAGIC ➡️ Next: **02_Standardize**
