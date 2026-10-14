# Databricks notebook source
# Shared setup, run at the top of every module with %run. Nothing to change here.
import importlib
import subprocess
import sys

try:
    import yaml  # noqa: F401
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pyyaml"])

import datagen
import lab_utils as lab

importlib.reload(datagen)
importlib.reload(lab)
print(f"✅ Lab helpers loaded · AI model: {lab.pick_model()}")
lab.check_order()   # stops here if the previous module hasn't been run yet
