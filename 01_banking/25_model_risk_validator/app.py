"""Model Risk Validation Assistant — CrewAI + Ollama.

Computes Gini, KS, PSI and calibration in pure Python, then agents draft an
SR 11-7 style validation report.

Run:  python 01_banking/25_model_risk_validator/app.py
"""

import json
import math
import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

random.seed(7)


def synthetic(n: int, shift: float = 0.0):
    """(score, default_flag) pairs: higher score = higher predicted PD."""
    rows = []
    for _ in range(n):
        latent = random.gauss(0, 1) + shift
        pd = 1 / (1 + math.exp(-(latent * 1.2 - 3)))
        rows.append((pd, 1 if random.random() < pd * 1.15 else 0))
    return rows


def auc(rows):
    pos = [s for s, y in rows if y]
    neg = [s for s, y in rows if not y]
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg[:2000])
    return wins / (len(pos) * len(neg[:2000]))


def ks(rows):
    rows = sorted(rows)
    P = sum(y for _, y in rows); N = len(rows) - P
    cp = cn = best = 0
    for _, y in rows:
        cp += y; cn += 1 - y
        best = max(best, abs(cp / P - cn / N))
    return best


def psi(dev, cur, bins=10):
    edges = sorted(s for s, _ in dev)
    cuts = [edges[int(len(edges) * i / bins)] for i in range(1, bins)]
    def dist(rows):
        c = [0] * bins
        for s, _ in rows:
            c[sum(s > x for x in cuts)] += 1
        return [max(v / len(rows), 1e-4) for v in c]
    a, b = dist(dev), dist(cur)
    return sum((y - x) * math.log(y / x) for x, y in zip(a, b))


def main():
    banner("25 - Model Risk Validation Assistant (CrewAI)")
    dev, oot = synthetic(3000), synthetic(3000, shift=0.35)
    a_dev, a_oot = auc(dev), auc(oot)
    metrics = {
        "model": "Retail PD Scorecard v3 (logistic regression)",
        "gini_development": round(2 * a_dev - 1, 3), "gini_out_of_time": round(2 * a_oot - 1, 3),
        "ks_out_of_time": round(ks(oot), 3), "psi_dev_vs_oot": round(psi(dev, oot), 3),
        "avg_predicted_pd_oot": round(sum(s for s, _ in oot) / len(oot), 4),
        "observed_default_rate_oot": round(sum(y for _, y in oot) / len(oot), 4),
        "thresholds": {"gini_min": 0.40, "psi_amber": 0.10, "psi_red": 0.25, "calibration_tolerance_rel": 0.10},
    }
    section("Validation metrics", json.dumps(metrics, indent=2))

    # RAG status is a threshold rule, so Python decides it
    th = metrics["thresholds"]
    calib_gap = abs(metrics["avg_predicted_pd_oot"] / metrics["observed_default_rate_oot"] - 1)
    rag = {
        "discrimination (Gini OOT)": "GREEN" if metrics["gini_out_of_time"] >= th["gini_min"] else "RED",
        "stability (PSI)": "RED" if metrics["psi_dev_vs_oot"] >= th["psi_red"]
        else "AMBER" if metrics["psi_dev_vs_oot"] >= th["psi_amber"] else "GREEN",
        "calibration (predicted vs observed PD)": f"{'GREEN' if calib_gap <= th['calibration_tolerance_rel'] else 'AMBER'} "
                                                  f"(relative gap {calib_gap:.0%})",
    }
    section("Test results (RAG)", json.dumps(rag, indent=2))

    validator = make_agent("Model Validator", "Assess discrimination, stability and calibration against thresholds",
                           "Independent model validation quant; you are objective and evidence-based.")
    mrm = make_agent("Head of Model Risk Management", "Rate findings and conclude the validation",
                     "You own the model risk framework (SR 11-7 / SS1/23) and decide model use conditions.")
    t1 = make_task("Metrics:\n{metrics}\n\nFinal RAG status per test (do not change):\n{rag}\n\n"
                   "Explain what each result means and likely causes of any AMBER/RED result.",
                   "Test-by-test explanation.", validator)
    t2 = make_task("Write the validation report summary.\n\nExact metrics (quote these; never invent numbers):\n{metrics}\n\n"
                   "Final RAG status per test (do not change):\n{rag}",
                   "Sections: Scope, Summary of tests (table), Findings with severity (High/Medium/Low) and remediation "
                   "for every AMBER/RED test, Overall rating (Fit for use / Fit with conditions / Not fit), "
                   "Monitoring recommendations.", mrm, context=[t1])
    section("Validation report", run_crew([validator, mrm], [t1, t2],
                                          {"metrics": json.dumps(metrics, indent=2), "rag": json.dumps(rag, indent=2)}))


if __name__ == "__main__":
    main()
