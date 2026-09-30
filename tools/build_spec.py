#!/usr/bin/env python3
"""Expand a strategy from strategies/catalog.json into a full Astral strategy_build spec.

Usage:  python3 tools/build_spec.py HV-G2 [--size 0.12] > spec.json
Supports the multi-coin families: rsi2, bollinger, meanrev_bb_rsi, zscore.
Paste the output fields (assets, series, signals, orders, rules) into
mcp__astral__astral_strategy_build along with name and bar_size.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(cfg, coins):
    e, x = cfg["entry"], cfg["exit"]
    S, G, O, R = [], [], [], []
    for p in coins:
        s = p + "USD"
        S.append({"alias": f"{p}_A", "expr": f"ATR({s}.high, {s}.low, {s}.close, 14)"})
        S.append({"alias": f"{p}_E", "expr": f"EMA({s}.close, {e['ema']})"})
        fam = cfg["family"]
        conds = [f"{s}.close > {p}_E"]
        outs = []
        if fam in ("rsi2", "meanrev_bb_rsi"):
            S.append({"alias": f"{p}_R", "expr": f"RSI({s}.close, 2)"})
            conds.append(f"{p}_R < {e['rsi2_below']}")
        if fam in ("bollinger", "meanrev_bb_rsi"):
            S.append({"alias": f"{p}_L", "expr": f"BB_LOWER({s}.close, {e['bb_len']}, {e['bb_sd']})"})
            S.append({"alias": f"{p}_M", "expr": f"BB_MIDDLE({s}.close, {e['bb_len']}, 2)"})
            conds.append(f"{s}.close < {p}_L")
        if fam == "zscore":
            S.append({"alias": f"{p}_Z", "expr": f"ZSCORE({s}.close, {e['z_len']})"})
            conds.append(f"{p}_Z < {e['z_below']}")
        S.append({"alias": f"{p}_N", "expr": " and ".join(conds)})
        if "rsi2_above" in x:
            outs.append(f"{p}_R > {x['rsi2_above']}")
        if x.get("bb_mid"):
            outs.append(f"{s}.close >= {p}_M")
        outs.append(f"BARS_SINCE({p}_N) == {x['max_bars']}")
        G += [{"name": f"{p}_IN", "expr": f"{p}_N"}, {"name": f"{p}_OUT", "expr": " or ".join(outs)}]
        O += [{"name": f"B_{p}", "asset": s, "side": "buy", "accumulate": False,
               "sizing_type": "percent_of_equity", "sizing_value": cfg["size"],
               "protection": {"protection": "tp_oco_sl", "evaluation": "on_entry_fill",
                              "stop_loss": {"expr": f"ENTRY_PRICE - {cfg['sl_atr']} * {p}_A"},
                              "take_profit": {"expr": f"ENTRY_PRICE + {cfg['tp_atr']} * {p}_A"}}},
              {"name": f"S_{p}", "asset": s, "side": "sell", "sizing_type": "percent_of_equity", "sizing_value": 1}]
        R += [{"name": f"{p}i", "condition": f"{p}_IN", "actions": [f"B_{p}"]},
              {"name": f"{p}o", "condition": f"{p}_OUT", "actions": [f"S_{p}"]}]
    return {"bar_size": cfg["bar"], "assets": [{"symbol": c + "USD", "type": "crypto"} for c in coins],
            "series": S, "signals": G, "orders": O, "rules": R}


if __name__ == "__main__":
    cat = json.load(open(os.path.join(ROOT, "strategies", "catalog.json")))
    key = sys.argv[1]
    cfg = dict(cat["strategies"][key])
    if "--size" in sys.argv:
        cfg["size"] = float(sys.argv[sys.argv.index("--size") + 1])
    coins = cat["coin_sets"][cfg["coins"]] if isinstance(cfg["coins"], str) else cfg["coins"]
    spec = build(cfg, coins)
    spec["name"] = key
    print(json.dumps(spec, indent=1))
