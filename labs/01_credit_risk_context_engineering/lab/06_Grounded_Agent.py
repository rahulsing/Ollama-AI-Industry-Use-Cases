# Databricks notebook source
# MAGIC %md
# MAGIC # 06 · Grounded agent: answer well, and know where to stop
# MAGIC
# MAGIC **The problem:** the AI is now accurate, but it still doesn't know its **limits**:
# MAGIC - Asked for "names and SSNs of members 60+ days late", it **returns them**, even though those columns have been tagged PII since module 02. Tags *describe* data. They don't *stop* anything.
# MAGIC - On credit decisions ("should we approve this loan?") it relies on its own judgement: sometimes it declines, sometimes it offers an opinion. Credit decisions belong to underwriters, and they need model-risk and fair-lending review.
# MAGIC
# MAGIC **The context step:** publish **scope rules (guardrails)** from the governance policy:
# MAGIC - 🛑 no credit decisions (approve, decline, price)
# MAGIC - 🛑 no member-level personal data
# MAGIC - 🛑 no predictions until a model has been reviewed
# MAGIC
# MAGIC Questions are checked against these rules *before* they reach the model, and the rules are also part of the context the model reads.

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · Publish the guardrails

# COMMAND ----------

lab.publish_guardrails()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Try the requests that leaked before

# COMMAND ----------

lab.ask("List the names and SSNs of members who are 60+ days past due.")

# COMMAND ----------

lab.ask("A member with a 640 FICO wants a $30,000 auto loan through a dealer. Should we approve it?")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Both requests were stopped *before* reaching the model, each with the **reason and the policy** it breaks. Refusing clearly and explaining why is part of being trustworthy, just as much as giving correct numbers.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · Final AI Scorecard

# COMMAND ----------

lab.run_scorecard("06 + Guardrails")

# COMMAND ----------

lab.show_progress()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4 · Before vs. after

# COMMAND ----------

lab.before_and_after()

# COMMAND ----------

# MAGIC %md
# MAGIC ## What you built
# MAGIC
# MAGIC | Step | Context asset | Without it, the AI… | 🔧 On Databricks |
# MAGIC |---|---|---|---|
# MAGIC | 01 Discover | Entity map | uses the wrong or stale table | table comments + tags |
# MAGIC | 02 Standardize | Glossary, classification, quality rules | misreads codes, leaks PII | column comments, tags, constraints |
# MAGIC | 03 Documents | Policies and definitions | answers with generic rules | Volume (+ Vector Search at scale) |
# MAGIC | 04 Semantic layer | Certified metrics + ontology | invents its own formulas | Metric Views |
# MAGIC | 05 Enrich & publish | Approved business vocabulary | misunderstands business language | approval table + certified tag |
# MAGIC | 06 Guardrails | Scope rules | oversteps into decisions | rules checked before the model |
# MAGIC
# MAGIC > 🔑 **The lesson:** the model never changed. Every improvement came from **context we built, reviewed and published**. Context engineering is what turns a fluent AI into a trustworthy one.
# MAGIC
# MAGIC ---
# MAGIC ### Try your own question
# MAGIC Ideas: *"What is the net charge-off rate by product?"*, *"Which channel has the highest 60+ DPD rate?"*, *"Compare West and East delinquency."*

# COMMAND ----------

lab.ask("Which channel has the highest 60+ day delinquency rate for Auto loans?")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Look closely: context is never "finished"
# MAGIC In our test run, the AI used the right metric and the right business values, but it **forgot to filter `snapshot_date`**. It averaged the 60+ rate over all 33 months instead of reporting the current month. Nothing in the context said "rates are point-in-time; default to the latest month".
# MAGIC
# MAGIC That's how context engineering works in practice: you watch real questions, find the gap, and publish one more rule. This lab now publishes that rule with the metric views in step 04.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Optional: the same context powers other tools
# MAGIC Everything you published lives in the catalog, not inside this notebook. Any tool that reads it benefits. For example, create a **Genie space** on `semantic.portfolio_performance` and `semantic.vintage_performance`, then ask the scorecard questions there. You get the same definitions and the same numbers.
# MAGIC
# MAGIC When you're done, run **99_Cleanup** to remove the lab objects.
