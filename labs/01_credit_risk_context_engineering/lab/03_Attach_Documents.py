# Databricks notebook source
# MAGIC %md
# MAGIC # 03 · Attach documents: knowledge that isn't in the data
# MAGIC
# MAGIC **The problem:** asked "when do we charge off a loan?", the AI answers with the **generic industry rule** (120/180 days). Our credit union is stricter: Auto at 90 days, Personal Loans at 120, Cards at 150. That's written in a policy document, not in any table.
# MAGIC
# MAGIC **The context step:** attach the reference documents (charge-off policy, metric definitions, Metro 2 code crosswalk) to the data. Store them in a governed place, split them into sections, and let the AI retrieve the relevant section for each question.

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1 · Store and index the documents

# COMMAND ----------

lab.publish_documents()

# COMMAND ----------

# MAGIC %md
# MAGIC ### What just happened
# MAGIC Three documents were copied to a governed document store and split into sections. When a question comes in, the most relevant sections are retrieved and handed to the AI. This is the "retrieval" in *retrieval-augmented generation (RAG)*.
# MAGIC
# MAGIC > 🔧 *On Databricks:* files in a Unity Catalog Volume. For large document sets, use `ai_parse_document` for PDFs and a Vector Search index for retrieval.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 · Ask the policy question again

# COMMAND ----------

lab.ask("When do we charge off a loan? Explain our charge-off policy for each product.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 · AI Scorecard

# COMMAND ----------

lab.run_scorecard("03 + Documents")

# COMMAND ----------

# MAGIC %md
# MAGIC ### What improved, and what didn't
# MAGIC - **Q2** should now state *our* policy, not the textbook one.
# MAGIC - The metric definitions document also tells the AI that delinquency is **balance-weighted** and that vintages must be compared **at equal age**.
# MAGIC - Even so, the AI still writes its *own* SQL for every number, and results can vary between runs and between users. Q3 is hard to get right this way.
# MAGIC
# MAGIC > 🔑 **Key takeaway:** Documents give the AI the institution's own rules. Without them, it falls back on generic knowledge.
# MAGIC
# MAGIC ➡️ Next: **04_Semantic_Layer**
