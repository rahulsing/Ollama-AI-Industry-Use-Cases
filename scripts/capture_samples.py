"""Run every use case against the local Ollama model and save its real output.

Writes NN_industry/NN_slug/sample_output.txt, which build_docs.py shows in each README
and in the interactive explorer as "Sample response".

Run:  python scripts/capture_samples.py               # all use cases
      python scripts/capture_samples.py 01_banking/13  # only matching paths
      python scripts/capture_samples.py --missing      # only those without a sample yet
"""

import os
import re
import subprocess
import sys
import time

from domains import ROOT, load_domains

ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_missing = "--missing" in sys.argv
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"}
    failed = []
    for d in load_domains():
        for u in d.use_cases:
            rel = f"{d.folder}/{u[0]}"
            out = d.path / u[0] / "sample_output.txt"
            if (args and not any(a in rel for a in args)) or (only_missing and out.exists()):
                continue
            start = time.time()
            proc = subprocess.run([sys.executable, str(d.path / u[0] / "app.py")], cwd=ROOT, env=env,
                                  capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1800)
            took = time.time() - start
            if proc.returncode != 0:
                failed.append(rel)
                print(f"FAIL {rel} ({took:.0f}s)\n{proc.stderr[-1500:]}", flush=True)
                continue
            text = ANSI.sub("", proc.stdout).strip() + "\n"
            out.write_text(text, encoding="utf-8", newline="\n")
            print(f"ok   {rel} ({took:.0f}s, {len(text)} chars)", flush=True)
    if failed:
        sys.exit(f"{len(failed)} failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
