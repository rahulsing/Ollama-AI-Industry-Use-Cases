"""Run the lab end-to-end in a Databricks workspace and capture every notebook WITH outputs.

Usage (uses the DEFAULT profile in ~/.databrickscfg):
    python tools/run_and_capture.py [--profile NAME] [--skip-run RUN_ID]

What it does
  1. Uploads lab/ to /Users/<you>/credit-risk-context-lab (overwrites).
  2. Submits one serverless job: 00 -> 01 -> ... -> 06, one task per module.
  3. Exports each finished task as HTML (code + outputs) to rendered/<module>.html.
  4. Imports those HTML files into /Users/<you>/credit-risk-context-lab/rendered/, which gives
     read-only notebooks with saved outputs that anyone can open without running anything.
"""
import argparse
import base64
import io
import sys
import time
from pathlib import Path

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs, workspace

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
OUT = ROOT / "rendered"
MODULES = ["00_Baseline_AI_Without_Context", "01_Discover", "02_Standardize", "03_Attach_Documents",
           "04_Semantic_Layer", "05_Enrich_and_Publish", "06_Grounded_Agent"]


def upload(w, dest):
    w.workspace.mkdirs(dest)
    for f in LAB.rglob("*"):
        if f.is_dir() or "__pycache__" in f.parts:
            continue
        rel = f.relative_to(LAB).as_posix()
        target = f"{dest}/{rel}"
        w.workspace.mkdirs(target.rsplit("/", 1)[0])
        text = f.read_text(encoding="utf-8")
        if f.suffix == ".py" and text.startswith("# Databricks notebook source"):
            w.workspace.import_(target[:-3], content=base64.b64encode(text.encode()).decode(),
                                format=workspace.ImportFormat.SOURCE, language=workspace.Language.PYTHON,
                                overwrite=True)
        else:
            w.workspace.upload(target, io.BytesIO(f.read_bytes()), format=workspace.ImportFormat.AUTO,
                               overwrite=True)
    print(f"uploaded lab to {dest}")


def submit(w, dest):
    tasks = []
    for i, m in enumerate(MODULES):
        tasks.append(jobs.SubmitTask(
            task_key=f"m{m[:2]}", notebook_task=jobs.NotebookTask(notebook_path=f"{dest}/{m}",
                                                                  source=jobs.Source.WORKSPACE),
            depends_on=[jobs.TaskDependency(task_key=f"m{MODULES[i - 1][:2]}")] if i else None,
            timeout_seconds=1800))
    run = w.jobs.submit(run_name="credit-risk-context-lab: full run", tasks=tasks).response.run_id
    print(f"submitted run {run}: {w.config.host}/jobs/runs/{run}")
    return run


def wait(w, run_id):
    while True:
        r = w.jobs.get_run(run_id)
        states = {t.task_key: (t.state.life_cycle_state.value, t.state.result_state.value if t.state.result_state else "")
                  for t in r.tasks}
        print(time.strftime("%H:%M:%S"), states, flush=True)
        if r.state.life_cycle_state.value in ("TERMINATED", "INTERNAL_ERROR", "SKIPPED"):
            return r
        time.sleep(30)


def capture(w, run, dest):
    OUT.mkdir(exist_ok=True)
    w.workspace.mkdirs(f"{dest}/rendered")
    for t in run.tasks:
        m = next(x for x in MODULES if t.task_key == f"m{x[:2]}")
        if not t.run_id or t.state.result_state is None:
            print(f"skip {m}: no output")
            continue
        views = w.jobs.export_run(t.run_id, views_to_export=jobs.ViewsToExport.CODE).views
        html = views[0].content
        (OUT / f"{m}.html").write_text(html, encoding="utf-8")
        w.workspace.import_(f"{dest}/rendered/{m}", content=base64.b64encode(html.encode()).decode(),
                            format=workspace.ImportFormat.HTML, overwrite=True)
        print(f"captured {m}: {t.state.result_state.value} -> rendered/{m}.html")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default=None)
    ap.add_argument("--skip-run", type=int, help="capture an existing run instead of starting a new one")
    a = ap.parse_args()
    w = WorkspaceClient(profile=a.profile)
    dest = f"/Users/{w.current_user.me().user_name}/credit-risk-context-lab"
    if a.skip_run:
        run = w.jobs.get_run(a.skip_run)
    else:
        upload(w, dest)
        run = wait(w, submit(w, dest))
    capture(w, run, dest)
    failed = [t.task_key for t in run.tasks if t.state.result_state and t.state.result_state.value != "SUCCESS"]
    print("FAILED tasks:", failed) if failed else print("all modules succeeded")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
