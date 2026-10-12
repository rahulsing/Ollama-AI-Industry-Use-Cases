"""Trade-Based Money Laundering Detector — CrewAI + Ollama.

Run:  python 01_banking/14_tbml_detector/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

BENCHMARK_UNIT_PRICE = {"Cotton T-shirts": 3.2, "Used laptops": 180.0, "Frozen shrimp (kg)": 9.5}  # USD
TRANSHIPMENT_HUBS = {"AE", "HK", "PA"}

TRADES = [
    {"lc": "LC-301", "goods": "Cotton T-shirts", "qty": 20000, "invoice_value": 66000, "origin": "BD", "via": None, "dest": "DE",
     "applicant": "Nordmode GmbH", "beneficiary": "Dhaka Knit Ltd"},
    {"lc": "LC-302", "goods": "Used laptops", "qty": 500, "invoice_value": 412000, "origin": "CN", "via": "AE", "dest": "NG",
     "applicant": "Lagos Tech Hub", "beneficiary": "Gulf Star Trading FZE"},
    {"lc": "LC-303", "goods": "Frozen shrimp (kg)", "qty": 40000, "invoice_value": 98000, "origin": "VN", "via": "PA", "dest": "US",
     "applicant": "Coastline Foods", "beneficiary": "Saigon Seafood Co"},
]


def analyse(t: dict) -> dict:
    unit = t["invoice_value"] / t["qty"]
    bench = BENCHMARK_UNIT_PRICE[t["goods"]]
    dev = (unit / bench - 1) * 100
    flags = []
    if dev > 50: flags.append(f"Over-invoicing: unit price {unit:.2f} vs benchmark {bench} (+{dev:.0f}%)")
    if dev < -40: flags.append(f"Under-invoicing: unit price {unit:.2f} vs benchmark {bench} ({dev:.0f}%)")
    if t["via"] in TRANSHIPMENT_HUBS: flags.append(f"Transhipment via {t['via']} not required for route")
    if "FZE" in t["beneficiary"] and t["origin"] != "AE": flags.append("Beneficiary free-zone entity, not the manufacturer")
    return {"lc": t["lc"], "unit_price": round(unit, 2), "deviation_pct": round(dev), "flags": flags}


def main():
    banner("14 - Trade-Based Money Laundering Detector (CrewAI)")
    results = [analyse(t) for t in TRADES]
    section("Pricing & route analysis", json.dumps(results, indent=2))

    trade_analyst = make_agent("Trade Finance Analyst", "Assess commercial plausibility of each trade",
                               "Trade operations expert who knows typical goods, pricing and shipping routes.")
    tbml = make_agent("TBML Specialist", "Identify trade-based money laundering risks and recommend actions",
                      "Financial-crime specialist following FATF/Wolfsberg TBML red-flag guidance.")
    t1 = make_task("Trades:\n{trades}\n\nAnalysis:\n{analysis}\n\nComment on the commercial rationale of each trade.",
                   "Per-LC commercial assessment.", trade_analyst)
    t2 = make_task("Rate each LC LOW / MEDIUM / HIGH TBML risk and recommend actions "
                   "(e.g. request price justification, verify shipment via vessel tracking, EDD on beneficiary).",
                   "Per-LC risk rating, red flags and recommended actions.", tbml, context=[t1])
    section("TBML assessment", run_crew([trade_analyst, tbml], [t1, t2],
                                        {"trades": json.dumps(TRADES, indent=2), "analysis": json.dumps(results, indent=2)}))


if __name__ == "__main__":
    main()
