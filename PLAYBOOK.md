# Astral Strategy Playbook — What Works vs. What Doesn't

**Purpose:** one place to see which strategy ideas worked, which failed, and why, so new strategies can build on proven pieces instead of re-testing dead ends.
**Detailed trade-by-trade history:** `astral-paper-log.md` (this file is the summary).
**Last updated:** 2026-09-30 16:45 UTC

---

## ✅ WORKING — build on these

| Rank | Strategy | Market / timeframe | Core rules | Backtest | Live paper result | Status |
|---|---|---|---|---|---|---|
| 1 | **HV-E / HV-E2** — RSI(2) scalper | 1-min, 10 coins (BTC ETH SOL LINK AVAX DOGE XRP ADA LTC DOT) | Buy when close > EMA50 **and** RSI(2) < 10. Exit when RSI(2) > 70 or after 3 bars. TP +0.6 ATR, SL −1.5 ATR | 5,078 trades, ~7.8/hr, 62% WR, +5.7% (27 days, no costs) | **30 trades, 80% WR, +$177** (~6.6/hr) | LIVE on Paper4 (HV-E2, 18%/coin) |
| 2 | **HV-G / HV-G2** — fast RSI(2) scalper | 1-min, 15 coins (above + BCH UNI ATOM NEAR AAVE) | Buy close > EMA50 **and** RSI(2) < 20. Exit RSI(2) > 60 or after 2 bars. TP +0.5 ATR, SL −1.5 ATR | 8,607 trades, ~33/hr, 60% WR, +1.6% (11 days) | **92 trades each acct, 68–70% WR, +$124 (Paper2), ~29/hr** | LIVE on Paper try 1 + Paper2 (HV-G2, 10%/coin) |
| 3 | **HV-F2** — Bollinger snap-back | 1-min, 10 coins | Buy close < BB lower (20, **1.5 sd**) while close > EMA100. Exit at BB mid or 5 bars. TP +0.5 ATR, SL −2 ATR | 4,170 trades, ~6.4/hr, 66% WR, +5.4% | **13 trades, 85% WR, +$62** — but only ~3/hr live | RETIRED for low volume → HV-F3 (15 coins) on Paper5 |
| 4 | **HV-D / HV-A** — 5-min mean reversion | 5-min, SOL LINK AVAX DOGE | Buy close > EMA200 & close < BB lower (20,2) & RSI(2) < 10. Exit BB mid or 12 bars. TP +1 ATR, SL −1.5 ATR | 856 trades, 67% WR, +13.8%, DD −1.9% (4.5 mo) | **3 trades, 100% WR, +$257** | LIVE on Paper3 (low volume, <1/hr) |
| 5 | **1h MeanRev v2** (low-volume, real-cost winner) | 1-hour, SOL (also LINK) | Buy close > EMA200 & close < BB lower (20,2) & RSI(2) < 5. Exit BB mid or 24 bars. SL −2.5 ATR | SOL: 129 trades, 65.9% WR, **+18.6% AFTER 0.1% costs**; LINK +17.1% | Not live (parked) | Only design that stays profitable with realistic exchange fees |

### The winning recipe (use as the starting template)
1. **Mean reversion, not trend-following.** Buy sharp short-term dips *inside* an uptrend.
2. **Uptrend filter:** close above an EMA (EMA50 on 1-min, EMA200 on 5-min/1-h).
3. **Oversold trigger:** RSI(2) < 10–20, or close below Bollinger lower band.
4. **Quick exit:** RSI(2) bounce (> 60–70), Bollinger middle, or a 2–5 bar time stop.
5. **Asymmetric bracket for high win rate:** small take-profit (0.5–1 ATR), wider stop (1.5–2.5 ATR).
6. **Volume comes from coin count:** 10–15 coins at 1-min = 5–30+ trades/hr. Size per coin ≈ 90% ÷ max concurrent positions.

---

## ❌ NOT WORKING — don't repeat these

| Strategy | What it was | Result | Why it failed / lesson |
|---|---|---|---|
| **HV-C** trend pullback | 5-min SOL+LINK, EMA9>21>50, buy dip to EMA21 | 1,990 trades, 58% WR, **−20% even with zero costs** | Trend-following on short timeframes gets chopped up by noise |
| **Breakout A/B/C/D** (original 15-min plan) | 1h trend + 15-min volume breakout + RSI, 2R target, retest variants | 33–46% WR, −3% to −42% after costs | Breakouts win too rarely; 2R targets → low hit rate; costs dominate |
| **4h EMA50 filter** on breakout C | Added higher-timeframe trend filter | Not better out-of-sample; cut trades to ~5 per 8 months | Extra filters just remove trades; RSI filter was redundant |
| **LINK momentum breakout** 5-min & 15-min | Donchian 20-bar high + volume + EMA trend | 34–36% WR; −21% to −26% after costs | Momentum breakouts = low win rate |
| **v4 "bounce confirmation"** | Wait for up-candle after oversold signal | 64.7% WR but −17.7%, DD −44% | Buying *after* the bounce gives away the edge |
| **1-min mean reversion, 1 coin (SOL)** | Early 1-min test | 13% WR, −5% in a month | Too few signals + costs ≈ ATR on 1 coin |
| **BTC / ETH / AVAX / DOGE / XRP 1-hour v2** | Same 1h rules on other coins | 53–59% WR, flat to −20% after costs | Only works on higher-volatility SOL/LINK when costs are real |
| **HV-F (Bollinger 2.0 sd)** | 1-min, 10 coins | 65% WR but only ~2.3 trades/hr | Band too strict → too few trades (1.5 sd fixed it) |
| **v5 quick TP (1h)** | TP +0.75 ATR | 71–73% WR but ~1/3 the profit of v2 | Higher hit rate ≠ more money; exits winners too early |
| **15-min/30-min mean reversion** (real costs) | SOL MR at 15m, 30m | 54–59% WR, −6% to −16% after costs | Costs still too big vs. move size below 1h |
| **Cost-aware filters on 1m/5m** (from hmmm-zip review, 2026-09-30) | HV-G2 + ATR%>0.25% floor; HV-D + "BB-mid ≥0.6% / ≥1% away" edge floor, no TP | 1m: 24% WR −30% (baseline −79%). 5m edge≥1%: +2.2% May–Sep **but −6.8% on Jan–May holdout** | Filters cut losses a lot but no 1m/5m variant survives 0.2% round-trip costs out-of-sample. **Always check an untouched earlier period before deploying.** |

---

## ⚠️ Key facts about Astral Paper (affects every result)
- **Zero fees and zero slippage.** Fills happen exactly at the candle close / TP price. Paper P&L therefore matches the *no-cost* backtests and **overstates what a real exchange would give** (≈0.1–0.2% per round trip would erase most 1-min/5-min edges).
- Astral strategies are **long-only**, **percent-of-equity sizing only**, **no multi-timeframe** (approximate higher timeframes with longer EMAs), fills on signal-bar close.
- **Backtest limits:** 40,000 bars per run; 15-coin 1-min backtests **time out after 27 days** → use ≤10-day windows. Max 2 concurrent backtests.
- **Avoid BCHUSD and ATOMUSD on 1-min**: its feed times out (sparse bars) → a deployment can sit in warm-up forever (HV-F3 made 0 trades in 7h) and it periodically pauses HV-G2. ATOM did the same on 2026-09-30 13:36 (all ATOM strategies frozen 75+ min). One thin coin freezes the WHOLE multi-coin strategy — keep coin lists to liquid names. Check `runtime_health`/`source_failed_symbols` in deployments_list when a strategy is silent.
- Undeploying does **not** close open positions — swap strategies only when the account is flat.

---

## 📍 Currently live (2026-09-30)

| Account | Saved ID | Strategy | Size/coin |
|---|---|---|---|
| Paper try 1 ($10k) | 5948 | HV-G4 1m RSI2 13 coins | 12.5% |
| Paper2 ($100k) | 5949 | HV-G4 1m RSI2 13 coins | 12.5% |
| Paper3 ($100k) | 5952 | HV-D2 5m MR 4 coins | 29.7% |
| Paper4 ($100k) | 5950 | HV-E3 1m RSI2 10 coins | 22.5% |
| Paper5 ($100k) | 5951 | HV-F6 1m Bollinger 1.5sd 13 coins | 8.1% |

Sizes raised x1.25 on 2026-09-30 ~16:45 UTC (user request). Total exposure can now exceed 100% of equity when many coins signal at once — extra orders may be rejected for insufficient cash; watch for that.

**Where the paper trades "execute":** nowhere real. Astral Paper is an internal simulator: fills are at the close of the signal candle (or the TP/SL price) using Astral's *consolidated* USD crypto price feed (`crypto_market_scope: consolidated`, venue "SMART"), with zero fees/slippage. No exchange receives orders. Going live would route through a connected broker account (none connected yet).

**Replacement rule:** after 15+ closed live trades, replace a strategy if win rate < 55%, P&L < −3%, or (1-min strategies) < 5 trades/hour. Record the result in the tables above.
