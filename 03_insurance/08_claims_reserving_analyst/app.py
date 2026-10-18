"""Claims Reserving Analyst — LangChain chain + Ollama.

Python runs the chain-ladder method on a paid claims triangle: development factors, ultimate claims and the
reserve still needed for each accident year, compared with the reserves on the books; the LLM writes the
reserving memo.

Run:  python 03_insurance/08_claims_reserving_analyst/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

# Motor book. Cumulative claims paid by the end of each development year (year 1 = the accident year itself)
PAID = {
    2021: [2_000_000, 3_560_000, 4_450_000, 4_810_000, 4_905_000],
    2022: [2_150_000, 3_890_000, 4_900_000, 5_290_000],
    2023: [2_380_000, 4_330_000, 5_400_000],
    2024: [2_800_000, 5_180_000],
    2025: [3_250_000],
}
EARNED_PREMIUM = {2021: 6_900_000, 2022: 7_200_000, 2023: 7_600_000, 2024: 8_100_000, 2025: 8_700_000}
BOOKED_RESERVE = {2021: 0, 2022: 105_000, 2023: 600_000, 2024: 1_750_000, 2025: 4_300_000}  # held today for future payments
TARGET_LOSS_RATIO = 0.75
TAIL_FACTOR = 1.0     # assume claims are fully paid after 5 years


def chain_ladder() -> tuple[list[dict], list[dict], dict]:
    years = sorted(PAID)
    n = len(PAID[years[0]])
    # Volume-weighted age-to-age factors: total paid at dev j+1 / total paid at dev j, over years that have both
    factors = []
    for j in range(n - 1):
        rows = [PAID[y] for y in years if len(PAID[y]) > j + 1]
        factors.append(sum(r[j + 1] for r in rows) / sum(r[j] for r in rows))
    to_ultimate = [TAIL_FACTOR] * n           # cumulative factor from dev j to ultimate
    for j in range(n - 2, -1, -1):
        to_ultimate[j] = to_ultimate[j + 1] * factors[j]
    dev = [{"from_year": j + 1, "to_year": j + 2, "age_to_age_factor": round(f, 3),
            "factor_to_ultimate": round(to_ultimate[j], 3)} for j, f in enumerate(factors)]

    rows = []
    for y in years:
        paid = PAID[y][-1]
        ultimate = paid * to_ultimate[len(PAID[y]) - 1]
        needed = ultimate - paid
        gap = needed - BOOKED_RESERVE[y]
        loss_ratio = ultimate / EARNED_PREMIUM[y]
        rows.append({"accident_year": y, "years_developed": len(PAID[y]), "paid_to_date": paid,
                     "ultimate_claims": round(ultimate), "reserve_needed": round(needed),
                     "reserve_booked": BOOKED_RESERVE[y], "shortfall": round(gap) if gap > 0 else 0,
                     "surplus": round(-gap) if gap < 0 else 0, "ultimate_loss_ratio": f"{loss_ratio:.1%}",
                     "loss_ratio_above_target": loss_ratio > TARGET_LOSS_RATIO})
    needed = sum(r["reserve_needed"] for r in rows)
    booked = sum(r["reserve_booked"] for r in rows)
    totals = {"reserve_needed": needed, "reserve_booked": booked,
              "net_reserve_increase_needed": needed - booked if needed > booked else 0,
              "years_with_shortfall": [r["accident_year"] for r in rows if r["shortfall"]],
              "target_loss_ratio": f"{TARGET_LOSS_RATIO:.0%}",
              "most_uncertain_year": f"{years[-1]} (only {len(PAID[years[-1]])} year of payments, so its estimate "
                                     f"rests most on the development factors)"}
    return dev, rows, totals


SYSTEM = (
    "You are an actuary writing a reserving memo for the reserving committee. Use ONLY the figures given; never "
    "recalculate or round them differently. Cover: (1) the overall position: reserve needed vs booked and the net "
    "increase needed; (2) each accident year with a shortfall or surplus, and the loss ratios above target; "
    "(3) what the trend suggests (e.g. rising claims costs in recent years); (4) caveats: chain-ladder assumes past "
    "payment patterns repeat, and the most recent year is the least certain, so suggest a cross-check with the "
    "Bornhuetter-Ferguson method. End with a recommendation. Under 350 words."
)


def main():
    banner("Insurance 08 - Claims Reserving Analyst (LangChain chain)")
    dev, rows, totals = chain_ladder()
    section("Development factors", json.dumps(dev, indent=2))
    section("Reserves by accident year", json.dumps({"accident_years": rows, "total": totals}, indent=2))
    section("Reserving memo", run_chain(SYSTEM, "Development factors:\n{d}\n\nReserves:\n{r}",
                                        d=json.dumps(dev, indent=2),
                                        r=json.dumps({"accident_years": rows, "total": totals}, indent=2)))


if __name__ == "__main__":
    main()
