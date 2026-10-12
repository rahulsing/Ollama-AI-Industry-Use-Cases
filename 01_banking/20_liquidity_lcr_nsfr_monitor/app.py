"""Liquidity LCR / NSFR Monitor — LangChain chain + Ollama.

Simplified Basel III factors for illustration.

Run:  python 01_banking/20_liquidity_lcr_nsfr_monitor/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

HQLA = {"cash_central_bank": (3_200, 1.0), "govt_bonds_L1": (5_400, 1.0), "covered_bonds_L2A": (1_500, 0.85), "corp_bonds_L2B": (800, 0.50)}
OUTFLOWS = {"retail_stable": (20_000, 0.05), "retail_less_stable": (15_000, 0.10), "operational_wholesale": (6_000, 0.25),
            "non_operational_wholesale": (9_000, 0.40), "committed_credit_lines": (12_000, 0.10)}
INFLOWS = {"performing_loans_maturing": (1_600, 0.50), "interbank_maturing": (600, 1.0)}

ASF = {"capital": (5_800, 1.0), "retail_deposits": (28_000, 0.90), "wholesale_funding_lt1y": (11_500, 0.50), "long_term_debt": (4_000, 1.0)}
RSF = {"hqla_l1": (8_600, 0.0), "residential_mortgages": (12_000, 0.65), "corporate_loans_gt1y": (15_000, 0.85),
       "retail_loans": (9_000, 0.85), "other_assets": (2_500, 1.0)}


def weighted(d):  # sum of amount * factor
    return sum(a * f for a, f in d.values())


def compute() -> dict:
    l1 = HQLA["cash_central_bank"][0] + HQLA["govt_bonds_L1"][0]
    l2 = weighted({k: v for k, v in HQLA.items() if "L2" in k})
    hqla = l1 + min(l2, l1 * 40 / 60)  # Level 2 cap: 40% of HQLA
    out, inf = weighted(OUTFLOWS), weighted(INFLOWS)
    net = out - min(inf, 0.75 * out)
    return {"hqla": round(hqla), "gross_outflows": round(out), "capped_inflows": round(min(inf, 0.75 * out)),
            "lcr_pct": round(hqla / net * 100, 1), "asf": round(weighted(ASF)), "rsf": round(weighted(RSF)),
            "nsfr_pct": round(weighted(ASF) / weighted(RSF) * 100, 1), "limits": {"lcr_min": 100, "nsfr_min": 100,
                                                                                    "internal_lcr_trigger": 120,
                                                                                    "internal_nsfr_trigger": 110}}


SYSTEM = (
    "You are the Treasury liquidity risk manager writing for ALCO. Using the metrics, write: headline (RAG status), "
    "LCR and NSFR vs regulatory minimum and internal trigger, top drivers of outflows/RSF, and 3 concrete actions "
    "(e.g. term out wholesale funding, grow stable retail deposits, add Level 1 HQLA). Keep numbers exact and use only "
    "the limits provided - do not invent targets. RAG: Red below regulatory minimum, Amber below internal trigger, else Green."
)


def main():
    banner("20 - Liquidity LCR / NSFR Monitor (LangChain)")
    m = compute()
    section("Metrics", json.dumps(m, indent=2))
    section("ALCO note", run_chain(SYSTEM, "Metrics:\n{m}\n\nInputs:\n{i}", m=json.dumps(m, indent=2),
                                   i=json.dumps({"outflows": OUTFLOWS, "rsf": RSF}, indent=2)))


if __name__ == "__main__":
    main()
