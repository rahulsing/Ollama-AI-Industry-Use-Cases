# Databricks notebook source
# MAGIC %md
# MAGIC # 99 · Cleanup
# MAGIC Removes every table, view, volume and schema created by the lab. Run **00** again to start over.

# COMMAND ----------

# MAGIC %run ./_setup

# COMMAND ----------

lab.cleanup()
