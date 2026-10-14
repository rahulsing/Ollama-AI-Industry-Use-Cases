"""Build read-only "with outputs" notebooks from Databricks HTML exports.

Takes output/<module>.html (exported after a real run), updates the markdown cells from the
current lab/<module>.py source (same outputs, corrected narrative), clears stale error flags,
and writes rendered/<module>.html.

    python tools/finalize_exports.py
"""
import base64
import copy
import json
import re
import urllib.parse
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC, EXP, OUT = ROOT / "lab", ROOT / "output", ROOT / "rendered"
PAT = re.compile(r"(__DATABRICKS_NOTEBOOK_MODEL = ')([^']+)(')")


def source_cells(py):
    cells = []
    for raw in py.read_text(encoding="utf-8").split("# COMMAND ----------"):
        lines = [l for l in raw.strip().splitlines() if l != "# Databricks notebook source"]
        if not lines:
            continue
        if lines[0].startswith("# MAGIC"):
            text = "\n".join(re.sub(r"^# MAGIC ?", "", l) for l in lines)
        else:
            text = "\n".join(lines)
        cells.append(text.strip())
    return cells


def key(text):
    """First meaningful line, used to match cells between source and export."""
    for l in text.splitlines():
        l = l.strip()
        if l and l != "%md":
            return l
    return ""


def finalize(name):
    html = (EXP / f"{name}.html").read_text(encoding="utf-8")
    m = PAT.search(html)
    model = json.loads(urllib.parse.unquote(base64.b64decode(m.group(2)).decode("utf-8")))
    cmds = sorted(model["commands"], key=lambda c: float(c["position"]))
    src = source_cells(SRC / f"{name}.py")
    md_template = next(c for c in cmds if c["command"].lstrip().startswith("%md"))

    by_key = {key(c["command"]): c for c in cmds}
    changed = inserted = 0
    for i, cell in enumerate(src):
        if not cell.startswith("%md"):
            continue
        k = key(cell)
        if k in by_key:
            c = by_key[k]
            if c["command"].strip() != cell:
                c["command"] = cell
                changed += 1
            continue
        # new markdown cell: insert after the cell that precedes it in the source
        prev = by_key.get(key(src[i - 1])) if i else None
        if prev is None:
            print(f"  ! could not place new cell '{k[:50]}'")
            continue
        later = [float(c["position"]) for c in cmds if float(c["position"]) > float(prev["position"])]
        new = copy.deepcopy(md_template)
        new.update(command=cell, guid=str(uuid.uuid4()), origId=0, results=None,
                   position=str((float(prev["position"]) + min(later + [float(prev["position"]) + 2])) / 2))
        cmds.append(new)
        by_key[k] = new
        inserted += 1

    for c in cmds:                      # stale error flags from an earlier attempt
        if c.get("results") is not None or c["command"].startswith("%run"):
            for f in ("error", "errorSummary", "errorTraceType", "errorDetails", "baseErrorDetails"):
                c[f] = None
            c["state"] = "finished"

    model["commands"] = sorted(cmds, key=lambda c: float(c["position"]))
    enc = base64.b64encode(urllib.parse.quote(json.dumps(model), safe="~()*!.'").encode()).decode()
    OUT.mkdir(exist_ok=True)
    (OUT / f"{name}.html").write_text(html[:m.start(2)] + enc + html[m.end(2):], encoding="utf-8")
    print(f"{name}: {changed} markdown cells updated, {inserted} inserted")


if __name__ == "__main__":
    for f in sorted(EXP.glob("*.html")):
        finalize(f.stem)
