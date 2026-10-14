"""Synthetic credit-risk data for the lab (pure Python, deterministic).

The raw tables are deliberately "source-system shaped": cryptic names, coded
values, a stale backup table and a noise table. That is the starting point an
AI would face without any context engineering.

Built-in traps (each one is fixed by a later context step):
  * DLQ_CD holds Metro 2 status codes, not days past due.
  * CUR_BAL on charged-off rows (STAT_CD='CO') is the written-off balance, not outstanding.
  * The official delinquency rate is balance-weighted, not a count of accounts.
  * t_acct_mth_bkp is a stale copy that stops at 2025-12.
  * Division codes (R01/R02) mean nothing until the glossary says R01 = West.
  * Vintage 2025-04 Auto defaults early. It is only visible when vintages are
    compared at equal months on book (MOB 12), not on a to-date basis.
"""
import random
from datetime import date

N_ACCOUNTS = 12000
N_MONTHS = 33                       # 2024-01 .. 2026-09
SEED = 20261013
SPIKE_VINTAGE = 15                  # month index of 2025-04
BKP_LAST = 23                       # backup table stops at 2025-12

PRODUCTS = {                        # code: (group, description, loan/line, share)
    "C10": ("Cards", "CLASSIC REV", "R", .33),
    "U20": ("Personal Loan", "SIG UNSEC", "L", .22),
    "V31": ("Auto", "NEW VEH", "L", .18),
    "V32": ("Auto", "USED VEH", "L", .27),
}
CHANNELS = {"Cards": {"BR": .45, "DG": .55}, "Personal Loan": {"DG": .7, "TP": .3},
            "Auto": {"BR": .3, "DG": .45, "DL": .25}}
BASE_PD = {"Cards": .09, "Personal Loan": .07, "Auto": .045}
CO_DPD = {"Cards": 150, "Personal Loan": 120, "Auto": 90}     # internal charge-off policy
RECOVERY = {"Cards": .12, "Personal Loan": .18, "Auto": .45}
TERM = {"U20": 48, "V31": 72, "V32": 60}
DLQ_CODE = {0: "11", 30: "71", 60: "78", 90: "80", 120: "82", 150: "83"}

FIRST = ["Alex", "Sam", "Jordan", "Taylor", "Casey", "Riley", "Morgan", "Jamie", "Avery", "Quinn",
         "Drew", "Parker", "Reese", "Rowan", "Skyler", "Emerson", "Hayden", "Kendall", "Logan", "Sage"]
LAST = ["Rivera", "Chen", "Patel", "Okafor", "Nguyen", "Smith", "Garcia", "Kowalski", "Haddad", "Silva",
        "Brown", "Kim", "Novak", "Mensah", "Larsen", "Costa", "Ito", "Murphy", "Rossi", "Weber"]


def month_end(i):
    y, m = 2024 + i // 12, i % 12 + 1
    nxt = date(y + (m == 12), m % 12 + 1, 1)
    return date.fromordinal(nxt.toordinal() - 1)


def month_label(i):
    return f"{2024 + i // 12}-{i % 12 + 1:02d}"


def _pick(r, weights):
    x, acc = r.random(), 0.0
    for k, w in weights.items():
        acc += w
        if x < acc:
            return k
    return k


def _fico_mult(score):
    return 3.0 if score < 620 else 1.8 if score < 660 else 1.0 if score < 720 else .45


def generate(n_accounts=N_ACCOUNTS, seed=SEED):
    """Return dict of table name -> list of row dicts."""
    r = random.Random(seed)
    prod_w = {k: v[3] for k, v in PRODUCTS.items()}
    accts, members, snaps = [], [], []

    for i in range(n_accounts):
        acct_id, mbr_id = f"A{1000000 + i}", f"M{500000 + i}"
        prd = _pick(r, prod_w)
        grp = PRODUCTS[prd][0]
        div = "R01" if r.random() < .55 else "R02"
        ch = _pick(r, CHANNELS[grp])
        fico = int(min(830, max(540, r.gauss(700, 55))))
        o = min(N_MONTHS - 1, int(r.random() ** .85 * N_MONTHS))     # slightly more recent volume
        if grp == "Cards":
            amt = r.choice([2000, 3000, 5000, 7500, 10000, 15000])
        elif grp == "Personal Loan":
            amt = round(r.uniform(3000, 25000), -2)
        else:
            amt = round(r.uniform(12000, 55000), -2)

        # lifetime default propensity and timing
        pd_ = BASE_PD[grp] * _fico_mult(fico) * (1.15 if ch in ("DL", "TP") else 1.0)
        early = False
        if grp == "Auto" and o < 6:
            pd_ *= 1.6                                   # 2024-H1: looser box, slow-burn losses
        if grp == "Auto" and o == SPIKE_VINTAGE:
            pd_ *= 1.3                                   # 2025-04: early payment defaults
            early = True
        defaulter = r.random() < pd_
        start = (2 + r.gammavariate(1.5, 2.5)) if early else (3 + r.gammavariate(2.2, 6))
        start = int(start)
        if defaulter:
            amt = round(amt * 1.6, -2)                   # stretched borrowers take larger loans

        accts.append(dict(ACCT_ID=acct_id, MBR_ID=mbr_id, PRD_CD=prd, DIV_CD=div, CH_CD=ch,
                          OPN_DT=month_end(o).replace(day=1 + r.randrange(27)), ORIG_AMT=float(amt),
                          ORIG_SCR=fico, ORIG_RT=round(r.uniform(.05, .09) + (720 - fico) / 4000
                                                       + (.12 if grp == "Cards" else 0), 4),
                          TRM_MO=TERM.get(prd, 0)))
        members.append(dict(MBR_ID=mbr_id, MBR_NM=f"{r.choice(FIRST)} {r.choice(LAST)}",
                            SSN_L4=f"{r.randrange(10000):04d}", ZIP_CD=f"{r.randrange(80000, 99999)}"))

        status, dpd, bal, co_bal, co_mob, util = "OP", 0, amt, 0.0, None, r.uniform(.3, .7)
        for mob in range(N_MONTHS - o):
            t = o + mob
            co_amt = rcv_amt = 0.0
            if status == "OP":
                if grp != "Cards" and r.random() < .008 and mob > 2 and dpd == 0:
                    status, bal = "CL", 0.0
                elif defaulter and mob >= start:
                    if dpd >= CO_DPD[grp]:
                        status, co_bal, co_mob, co_amt = "CO", round(bal, 2), mob, round(bal, 2)
                    else:
                        dpd += 30
                        bal = round(bal * 1.02, 2)               # unpaid interest and fees accrue
                else:
                    dpd = 30 if (dpd == 0 and mob > 1 and r.random() < .012) else 0
                    if grp == "Cards":
                        util = min(.95, max(.05, util + r.uniform(-.08, .08)))
                        bal = round(amt * util, 2)
                    else:
                        bal = round(amt * max(0.0, 1 - mob / TERM[prd]), 2)
                    if bal <= 0:
                        status = "CL"
            elif status == "CO" and 1 <= mob - co_mob <= 6:
                rcv_amt = round(co_bal * RECOVERY[grp] / 6, 2)

            code = {"OP": DLQ_CODE.get(dpd, "83"), "CL": "13", "CO": "97"}[status]
            snaps.append(dict(ACCT_ID=acct_id, SNAP_DT=month_end(t),
                              CUR_BAL=co_bal if status == "CO" else (0.0 if status == "CL" else bal),
                              DLQ_CD=code, STAT_CD=status, CO_AMT=co_amt, RCV_AMT=rcv_amt))

    prd_rows = [dict(PRD_CD=k, PRD_DSC=v[1], LN_LN_FLG=v[2]) for k, v in PRODUCTS.items()]
    org_rows = [dict(DIV_CD="R01", ORG_NM="REGION 01"), dict(DIV_CD="R02", ORG_NM="REGION 02")]
    bkp = [s for s in snaps if s["SNAP_DT"] <= month_end(BKP_LAST)]
    cmp_rows = [dict(CMP_ID=f"CMP{r.randrange(10, 40)}", MBR_ID=m["MBR_ID"], RESP_FLG=r.choice("YN"))
                for m in members[::4]]
    return {"t_acct": accts, "t_mbr": members, "t_acct_mth": snaps, "t_acct_mth_bkp": bkp,
            "t_prd": prd_rows, "t_org": org_rows, "t_cmp_resp": cmp_rows}


# ---------------------------------------------------------------------------
# Ground truth (pure Python, used by self-check; the lab recomputes it in SQL)
# ---------------------------------------------------------------------------
def truths(data):
    acct = {a["ACCT_ID"]: a for a in data["t_acct"]}
    last = month_end(N_MONTHS - 1)
    late30, late60 = {"71", "78", "80", "82", "83"}, {"78", "80", "82", "83"}
    num = den = cnt_num = cnt_den = naive_num = naive_den = bad_west = 0.0
    for s in data["t_acct_mth"]:
        if s["SNAP_DT"] != last:
            continue
        a = acct[s["ACCT_ID"]]
        if PRODUCTS[a["PRD_CD"]][0] == "Auto":
            naive_den += s["CUR_BAL"]
            naive_num += s["CUR_BAL"] if s["DLQ_CD"] in late30 | {"97"} else 0
            if s["STAT_CD"] == "OP":
                den += s["CUR_BAL"]; cnt_den += 1
                if s["DLQ_CD"] in late30:
                    num += s["CUR_BAL"]; cnt_num += 1
        if a["DIV_CD"] == "R01" and s["STAT_CD"] == "OP" and s["DLQ_CD"] in late60:
            bad_west += s["CUR_BAL"]

    # vintage: cumulative charge-off rate at MOB 12 vs naive to-date
    co_12, co_all, orig = {}, {}, {}
    for s in data["t_acct_mth"]:
        a = acct[s["ACCT_ID"]]
        if PRODUCTS[a["PRD_CD"]][0] != "Auto" or not s["CO_AMT"]:
            continue
        o = (a["OPN_DT"].year - 2024) * 12 + a["OPN_DT"].month - 1
        t = (s["SNAP_DT"].year - 2024) * 12 + s["SNAP_DT"].month - 1
        co_all[o] = co_all.get(o, 0) + s["CO_AMT"]
        if t - o <= 12:
            co_12[o] = co_12.get(o, 0) + s["CO_AMT"]
    for a in data["t_acct"]:
        if PRODUCTS[a["PRD_CD"]][0] == "Auto":
            o = (a["OPN_DT"].year - 2024) * 12 + a["OPN_DT"].month - 1
            orig[o] = orig.get(o, 0) + a["ORIG_AMT"]
    mob12 = {o: co_12.get(o, 0) / orig[o] for o in orig if o <= N_MONTHS - 1 - 12}
    todate = {o: co_all.get(o, 0) / orig[o] for o in orig}
    worst12 = max(mob12, key=mob12.get)
    worst_td = max(todate, key=todate.get)
    return {
        "q1_dpd30_auto": num / den,
        "q1_wrong_count_based": cnt_num / cnt_den,
        "q1_wrong_incl_chargeoffs": naive_num / naive_den,
        "q3_worst_vintage_mob12": month_label(worst12),
        "q3_wrong_worst_todate": month_label(worst_td),
        "q3_mob12_rates": {month_label(o): round(v, 4) for o, v in sorted(mob12.items())},
        "q4_bad_loans_west": bad_west,
    }


if __name__ == "__main__":
    d = generate()
    print({k: len(v) for k, v in d.items()})
    t = truths(d)
    for k, v in t.items():
        print(k, v)
