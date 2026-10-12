"""Financial Statement Analyzer — CrewAI + Ollama.

Run:  python 01_banking/47_financial_statement_analyzer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

COMPANY = "Northwind Consumer Goods plc (fictional)"
FS = {  # millions
    "2024": {"revenue": 4_820, "cogs": 2_990, "opex": 1_160, "depreciation": 140, "interest": 85, "tax": 115, "net_income": 330,
             "cash": 410, "receivables": 690, "inventory": 820, "total_assets": 5_400, "current_liabilities": 1_350,
             "total_debt": 1_600, "equity": 2_450, "cfo": 520, "capex": 260},
    "2025": {"revenue": 5_150, "cogs": 3_310, "opex": 1_200, "depreciation": 150, "interest": 110, "tax": 98, "net_income": 282,
             "cash": 280, "receivables": 860, "inventory": 1_010, "total_assets": 5_900, "current_liabilities": 1_610,
             "total_debt": 1_980, "equity": 2_560, "cfo": 340, "capex": 300},
}


def analyse(fs: dict) -> dict:
    out = {}
    for y, d in fs.items():
        ebit = d["revenue"] - d["cogs"] - d["opex"] - d["depreciation"]
        out[y] = {"gross_margin_pct": round((d["revenue"] - d["cogs"]) / d["revenue"] * 100, 1),
                  "ebit_margin_pct": round(ebit / d["revenue"] * 100, 1), "net_margin_pct": round(d["net_income"] / d["revenue"] * 100, 1),
                  "roe_pct": round(d["net_income"] / d["equity"] * 100, 1), "interest_cover": round(ebit / d["interest"], 1),
                  "current_ratio": round((d["cash"] + d["receivables"] + d["inventory"]) / d["current_liabilities"], 2),
                  "debt_to_equity": round(d["total_debt"] / d["equity"], 2),
                  "dso_days": round(d["receivables"] / d["revenue"] * 365), "dio_days": round(d["inventory"] / d["cogs"] * 365),
                  "free_cash_flow": d["cfo"] - d["capex"], "operating_cash_flow_to_net_income_pct": round(d["cfo"] / d["net_income"] * 100)}
    out["yoy_growth_pct"] = {k: round((fs["2025"][k] / fs["2024"][k] - 1) * 100, 1) for k in ("revenue", "net_income", "total_debt", "inventory", "receivables")}
    return out


def main():
    banner("47 - Financial Statement Analyzer (CrewAI)")
    a = analyse(FS)
    section("Ratios", json.dumps(a, indent=2))
    analyst = make_agent("Financial Analyst", "Interpret ratios and trends, spotting quality-of-earnings issues",
                         "CFA charterholder who looks beyond headline growth to margins, working capital and cash.")
    writer = make_agent("Research Report Writer", "Write a clear, balanced company analysis",
                        "You write concise research notes for credit and equity committees.")
    t1 = make_task("Company: {company}\n\nStatements:\n{fs}\n\nRatios:\n{ratios}\n\nAnalyse profitability, efficiency, liquidity, "
                   "leverage and cash flow quality. Flag concerns.", "Analytical notes.", analyst)
    t2 = make_task("Write the report on {company}.\n\nExact ratios (quote these; never invent numbers):\n{ratios}", "Sections: Summary (3 bullets), Performance, Balance sheet & liquidity, Cash flow, "
                   "Key risks / red flags, Questions for management, Overall view (Positive / Neutral / Negative).",
                   writer, context=[t1])
    section("Report", run_crew([analyst, writer], [t1, t2], {"company": COMPANY, "fs": json.dumps(FS, indent=2), "ratios": json.dumps(a, indent=2)}))


if __name__ == "__main__":
    main()
