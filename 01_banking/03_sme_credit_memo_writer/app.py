"""SME Credit Memo Writer — CrewAI + Ollama.

Run:  python 01_banking/03_sme_credit_memo_writer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

BORROWER = {
    "name": "GreenLeaf Foods Pvt Ltd",
    "industry": "Packaged food manufacturing",
    "years_in_business": 9,
    "facility_requested": "Working capital line 25,000,000 + term loan 15,000,000 for new packaging unit",
    "collateral": "Factory land & building (valued 60,000,000), stock and receivables hypothecation",
}

FINANCIALS = {  # in thousands
    "FY2024": {"revenue": 210_000, "ebitda": 25_200, "net_profit": 9_800, "interest": 5_100, "principal_repaid": 6_000,
               "current_assets": 78_000, "current_liabilities": 52_000, "total_debt": 64_000, "equity": 58_000},
    "FY2025": {"revenue": 246_000, "ebitda": 28_300, "net_profit": 11_200, "interest": 5_900, "principal_repaid": 7_000,
               "current_assets": 92_000, "current_liabilities": 66_000, "total_debt": 71_000, "equity": 69_000},
}


def ratios(f: dict) -> dict:
    out = {}
    for year, d in f.items():
        out[year] = {
            "ebitda_margin_pct": round(d["ebitda"] / d["revenue"] * 100, 1),
            "net_margin_pct": round(d["net_profit"] / d["revenue"] * 100, 1),
            "dscr": round(d["ebitda"] / (d["interest"] + d["principal_repaid"]), 2),
            "current_ratio": round(d["current_assets"] / d["current_liabilities"], 2),
            "debt_to_equity": round(d["total_debt"] / d["equity"], 2),
            "debt_to_ebitda": round(d["total_debt"] / d["ebitda"], 2),
        }
    y0, y1 = list(f)
    out["revenue_growth_pct"] = round((f[y1]["revenue"] / f[y0]["revenue"] - 1) * 100, 1)
    return out


def main():
    banner("03 - SME Credit Memo Writer (CrewAI)")
    r = ratios(FINANCIALS)
    section("Computed ratios", json.dumps(r, indent=2))

    analyst = make_agent("SME Financial Analyst", "Interpret the borrower's financial performance and trends",
                         "Corporate banking analyst who focuses on cash-flow repayment capacity.")
    writer = make_agent("Credit Memo Writer", "Write a concise, bank-standard credit memo",
                        "You write credit papers for the credit committee. Structured, factual, no fluff.")

    t1 = make_task(
        "Borrower:\n{borrower}\n\nFinancials (thousands):\n{financials}\n\nRatios:\n{ratios}\n\n"
        "Assess profitability, liquidity, leverage and repayment capacity. Note trends and red flags.",
        "Analytical notes under Profitability, Liquidity, Leverage, Repayment Capacity, Red Flags.",
        analyst,
    )
    t2 = make_task(
        "Write the credit memo using the analysis.\n\nBorrower:\n{borrower}\n\n"
        "Exact ratios (quote these; never invent numbers):\n{ratios}",
        "Credit memo with sections: 1. Borrower Overview 2. Facility Request 3. Financial Analysis "
        "(with key ratios) 4. Key Risks & Mitigants 5. Covenants 6. Recommendation.",
        writer,
        context=[t1],
    )
    memo = run_crew([analyst, writer], [t1, t2], {
        "borrower": json.dumps(BORROWER, indent=2),
        "financials": json.dumps(FINANCIALS, indent=2),
        "ratios": json.dumps(r, indent=2),
    })
    section("Credit memo", memo)


if __name__ == "__main__":
    main()
