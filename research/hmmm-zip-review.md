# Review: hmmm-main.zip + "Complete Trading Handoff" (2026-09-30)

## What the zip actually is
A Python **market-making** framework (`src/v17mm_hardened`: Coinbase / Binance.US spot maker, perp ladders) plus a Go **Polymarket** bot (`sideprojects/polyharvest`) and a sports/weather pricer. It is **not** a candle/indicator strategy library. There are no RSI/EMA/Bollinger strategies in it.
- Maker logic: post-only bid/ask ladders around mid, spread floor = max(min spread, vol, fee x mult, 2 x required edge); inventory target = base 12% + signal x 15pp + trend x 8pp - vol penalty (bounds 0-45%).
- "Signals": order-book imbalance "phase space", Aizawa attractor modulation, TCN tape model (untrained if no weights -> random), Binance provider defaults to **neutral (zero) signal**.
- Evidence of profit: none reproducible. Author notes show ADA markouts **-5.9 to -7.7 bps** (adverse selection); polyharvest **-$42.53 over 137 markets**.

## Astral compatibility
| Idea from zip / handoff | Implementable in Astral? | Verdict |
|---|---|---|
| Spot market making (post-only quotes, inventory) | No - Astral fills at bar close, no limit-order ladders, no order-book data | Skip |
| Order-flow imbalance / phase-space / Aizawa / neural tape | No - needs L2 book/tick data; unvalidated | Skip |
| Polymarket NO-bid harvesting / sports pricer | No - different market | Skip |
| **Fee-aware edge floor** (only trade if expected move > costs + buffer) | Yes - entry filter, e.g. `(BB_MIDDLE - close)/close > 0.003` or `ATR/close > k` | **Test first** - targets our #1 problem (costs kill 1m edges) |
| **Volatility gating** (vol penalty on exposure) | Yes - ATR% band filter | Test |
| Trend-tilted inventory (buy more in uptrend) | Already doing it (close > EMA filter) | Confirms recipe |
| Risk halts: -1.5% daily loss stop, pause 6h after 3 losses, review at 6% DD | Not in strategy rules; yes via monitoring cron (undeploy) | Add to monitor |
| Correct markouts / honest P&L measurement | Partly - post-trade 1/5/15-bar returns from trade CSV + candles | Nice-to-have for summarize_trades.py |
| Chronological dev / validation / untouched holdout, trial register | Yes (catalog.json already = trial register) | Adopt |
| Handoff T0 breakout-retest (Appendix B), variants A-D | Mostly (risk-% sizing -> approximate with % equity; hourly filter -> EMA36/84 on 15m) | **Already tested A/B/C on SOL: 33-46% WR, -3% to -42%.** Only untested piece: variant D partial+trail, and BTC. Low priority; 2R targets structurally give <50% WR |

## Bottom line
Nothing in the zip is a ready-to-run strategy for Astral. The useful parts are **risk/cost discipline**, which matches what our own backtests found. Next experiments: (1) cost-edge floor on HV-G2/E2/F3 backtested at 5+5 bps, (2) ATR% volatility filter, (3) risk halts in the monitor, (4) optional T0-D on BTC/SOL 15m for completeness.
