"""Store Shrink & Loss Prevention Analyzer — CrewAI + Ollama.

Python splits each store's shrink into known loss (waste, damage) and unknown loss (theft, errors), compares it
to the benchmark and flags unusual till activity; agents find the likely causes and write the action plan.

Run:  python 02_retail/08_shrink_loss_analyzer/app.py
"""

import json
import statistics
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# Last quarter. known = recorded waste and damage; unknown = gap found by stock counts (theft, admin errors)
STORES = [
    {"store": "S-01 Downtown", "sales": 2_400_000, "known": {"expired fresh": 9_000, "damaged": 5_000},
     "unknown": {"health & beauty": 6_000, "electronics accessories": 4_000, "grocery": 3_500, "other": 2_500}},
    {"store": "S-02 Riverside", "sales": 1_800_000, "known": {"expired fresh": 8_000, "damaged": 4_500},
     "unknown": {"health & beauty": 4_000, "electronics accessories": 2_500, "grocery": 2_500, "other": 2_000}},
    {"store": "S-03 Airport Mall", "sales": 2_100_000, "known": {"expired fresh": 9_500, "damaged": 5_500},
     "unknown": {"health & beauty": 18_500, "electronics accessories": 12_000, "grocery": 4_000, "other": 6_500}},
    {"store": "S-04 Lakeside", "sales": 1_500_000, "known": {"expired fresh": 24_000, "damaged": 7_000},
     "unknown": {"health & beauty": 2_000, "electronics accessories": 1_500, "grocery": 1_500, "other": 1_000}},
]
# Till exceptions per cashier ID: refunds without a receipt and voids after the total was shown
TILLS = [
    ("S-01 Downtown", "C-101", 6100, 7, 10), ("S-01 Downtown", "C-102", 5900, 8, 9),
    ("S-02 Riverside", "C-201", 4700, 5, 6), ("S-02 Riverside", "C-202", 4500, 4, 8),
    ("S-03 Airport Mall", "C-311", 5200, 6, 9), ("S-03 Airport Mall", "C-312", 4800, 41, 38),
    ("S-03 Airport Mall", "C-313", 5100, 5, 7),
    ("S-04 Lakeside", "C-401", 3900, 3, 5), ("S-04 Lakeside", "C-402", 4100, 4, 6),
]
BENCHMARK = 0.015      # total shrink above 1.5% of sales needs action
TILL_FLAG = 3          # exception rate above 3x the chain median gets reviewed


def store_facts(s: dict) -> dict:
    known, unknown = sum(s["known"].values()), sum(s["unknown"].values())
    total_pct = (known + unknown) / s["sales"]
    main = "unknown loss (theft or admin errors)" if unknown > known else "known loss (waste and damage)"
    excess = max(round(known + unknown - BENCHMARK * s["sales"]), 0)
    return {"store": s["store"], "shrink_pct": round(total_pct * 100, 2), "known_loss": known, "unknown_loss": unknown,
            "status": "ABOVE BENCHMARK" if excess else "OK", "main_driver": main,
            "loss_reduction_needed_per_quarter": excess,
            "target": f"cut losses by {excess:,} a quarter to get back to {BENCHMARK:.1%} of sales" if excess
                      else "stay at or below the benchmark",
            "top_loss_lines": dict(sorted({**s["known"], **s["unknown"]}.items(), key=lambda kv: -kv[1])[:2])}


def till_flags() -> list[dict]:
    rates = [(st, cid, refunds / tx * 1000, voids / tx * 1000) for st, cid, tx, refunds, voids in TILLS]
    med_refund = statistics.median(r[2] for r in rates)
    med_void = statistics.median(r[3] for r in rates)
    return [{"store": st, "cashier_id": cid, "no_receipt_refunds_per_1000": round(rf, 1),
             "post_total_voids_per_1000": round(vd, 1), "chain_median_refunds": round(med_refund, 1),
             "chain_median_voids": round(med_void, 1)}
            for st, cid, rf, vd in rates if rf > TILL_FLAG * med_refund or vd > TILL_FLAG * med_void]


def main():
    banner("Retail 08 - Store Shrink & Loss Prevention Analyzer (CrewAI)")
    facts = {"benchmark_shrink_pct": BENCHMARK * 100, "stores": [store_facts(s) for s in STORES],
             "till_exceptions_to_review": till_flags(),
             "note": "Till flags are a reason to review CCTV and till logs, not proof of wrongdoing."}
    section("Shrink facts", json.dumps(facts, indent=2))

    analyst = make_agent("Loss Prevention Analyst", "Find the most likely cause of excess shrink at each store",
                         "Retail loss prevention analyst. You separate theft, admin errors and waste, and you never "
                         "accuse an individual: unusual till activity only triggers a review.")
    manager = make_agent("Regional Operations Manager", "Turn the findings into a practical 30-day action plan",
                         "You run these stores and balance loss prevention with customer experience and staff morale.")
    t1 = make_task("Shrink facts (exact figures):\n{facts}\n\nFor each ABOVE BENCHMARK store, explain the main driver "
                   "and the likely causes for its top loss lines. Mention the till exceptions as items to review.",
                   "Findings per store.", analyst)
    t2 = make_task("Shrink facts (exact figures; quote these, never recalculate):\n{facts}\n\n"
                   "Write the 30-day action plan for the stores above benchmark.",
                   "Plan: per store, 3-4 actions (e.g. protective packaging or tagging for high-theft lines, fresh "
                   "ordering and rotation fixes, till-log review), each with an owner role and fitting that store's "
                   "main driver. End each store's section with 'Target:' followed by its target field quoted exactly. "
                   "Do not give each action its own money target.",
                   manager, context=[t1])
    section("Action plan", run_crew([analyst, manager], [t1, t2], {"facts": json.dumps(facts, indent=2)}))


if __name__ == "__main__":
    main()
