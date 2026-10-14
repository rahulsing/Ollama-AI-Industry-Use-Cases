# Databricks notebook source
# MAGIC %md
# MAGIC # 04 · Semantic layer: one certified way to calculate each number
# MAGIC
# MAGIC **The problem:** even with definitions and documents, the AI **re-invents every formula** in its own SQL: joins, filters, code lists, denominators. One small slip gives a wrong number. Two people asking the same question can get two different answers.
# MAGIC
# MAGIC Vintage analysis (Q3) shows this most clearly. Older vintages always *look* worse because they've had more time to default. The fair comparison is at the **same age** (12 months on book), and that is easy to get wrong.
# MAGIC
# MAGIC **The context step:** build a **semantic layer**:
# MAGIC - a conformed view in business terms (`product`, `division`, `vintage`, `months_on_book`…)
# MAGIC - **certified metrics** defined once: 30+ DPD rate, 60+ DPD balance, net charge-off rate, cumulative charge-off rate by vintage
# MAGIC - an **ontology**: the business entities and how they relate (Member → holds → Loan Account → observed in → Snapshot…)

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · Publish the semantic layer

# COMMAND ----------

lab.publish_semantic_layer()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Each metric now has **one owner, one definition and one formula**, stored centrally. The AI no longer has to work out *how* to calculate delinquency. It only has to pick the metric and the filters.
# MAGIC
# MAGIC The layer also publishes its **allowed values** (`product = 'Auto'`, `division = 'West'`…). We learned this the hard way: in our first test run the metric views existed, but the AI filtered them with raw source codes (`product IN ('V31','V32')`, `division = 'R01'`). Every answer came back **empty**, and the score went *down*. A semantic layer that renames values must also say what the new values are.
# MAGIC
# MAGIC > 🔧 *On Databricks:* a view plus two **Unity Catalog Metric Views** (metrics defined in YAML, queried with `MEASURE()`).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Use a certified metric

# COMMAND ----------

lab.try_metric_view()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC A few lines of SQL return the official delinquency rate for every product. The complicated logic (which codes, which accounts, which balance) lives inside the metric. That's what makes answers consistent for dashboards, analysts and AI alike.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · AI Scorecard

# COMMAND ----------

lab.run_scorecard("04 + Semantic layer")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What improved, and what didn't
# MAGIC - **Q1** and **Q3** should now be right, and stay right on every run, because the AI selects a certified metric instead of improvising.
# MAGIC - **Q4** may still miss: "bad loans" is how the credit committee talks. It isn't a metric name.
# MAGIC
# MAGIC > 🔑 **Key takeaway:** The semantic layer turns "the AI writes a formula" into "the AI picks the official metric". That's the difference between plausible and correct.
# MAGIC
# MAGIC ➡️ Next: **05_Enrich_and_Publish**
