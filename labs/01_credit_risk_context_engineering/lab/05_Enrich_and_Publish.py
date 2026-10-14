# Databricks notebook source
# MAGIC %md
# MAGIC # 05 · Enrich & publish: speak the business's language, with a human in the loop
# MAGIC
# MAGIC **The problem:** people don't say "dpd60_balance". They say *"bad loans"*, *"the bad book"*, *"problem loans"*. Each institution uses these phrases in its own way. Here, "bad loans" means **60+ days past due, excluding charge-offs**. Without that, the AI guesses: 30+? charge-offs? both?
# MAGIC
# MAGIC **The context step:**
# MAGIC 1. **AI drafts** enrichments: synonyms and plain-language phrases for each certified metric.
# MAGIC 2. A **data steward reviews** them and adds the institution's own vocabulary.
# MAGIC 3. Only **approved** items are **published** to the AI. Drafts stay invisible.

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · AI drafts, steward adds

# COMMAND ----------

lab.draft_enrichments()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC The AI produced sensible but **generic** synonyms quickly. The steward's list holds what only the institution knows. Everything is still a **draft**: the AI can't see any of it yet.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Test a business phrase while the vocabulary is still a draft
# MAGIC "Problem-loan book" and "western region" aren't metric names. Watch how the AI copes.

# COMMAND ----------

lab.ask("How big is our problem-loan book in the western region right now?")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · Steward approval: publish
# MAGIC Change to `approve=False` to see what happens when nothing is approved.

# COMMAND ----------

lab.approve_and_publish(approve=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC The approved vocabulary is now published, and the metric views are tagged **certified**, with a named steward. This publish gate is what makes the context *trustworthy*: an unreviewed AI suggestion never becomes something the AI treats as truth.
# MAGIC
# MAGIC > 🔧 *On Databricks:* the approval status lives in a Delta table, and the certification is a Unity Catalog tag on the metric views.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4 · Same question, after publishing

# COMMAND ----------

lab.ask("How big is our problem-loan book in the western region right now?")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC With the approved vocabulary published, the AI maps "problem-loan book" to the 60+ DPD balance and "western region" to `division = 'West'`, and answers with the certified figure. The answer should match Q4 in the scorecard.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5 · AI Scorecard

# COMMAND ----------

lab.run_scorecard("05 + Enriched & published")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What improved, and what didn't
# MAGIC - **Q4** may already have passed in module 04, where the AI linked "bad loans" to the metric named *Seriously Delinquent Balance*. That was an inference, and the next phrasing might not be so lucky. Approved vocabulary makes it **reliable** for every phrase the business uses, as the problem-loan test above showed.
# MAGIC - **Q5** is still unsafe: asked for member names and SSNs, the AI returns them, even though those columns have been tagged **PII** since module 02. A label informs. It doesn't enforce.
# MAGIC
# MAGIC > 🔑 **Key takeaway:** AI can speed up building context, but a person must approve it before it's published.
# MAGIC
# MAGIC ➡️ Next: **06_Grounded_Agent**
