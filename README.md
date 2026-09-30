# Astral Crypto Strategy Lab

Research and paper trading of high-volume, high-win-rate crypto strategies on [Astral](https://astral.ai) (via the Astral MCP tools in Claude Code).

**Goal:** find strategies that trade frequently (5–10+ trades/hour per account), win more than 55% of trades, and grow the paper accounts.

## Start here
| File | What it is |
|---|---|
| **[PLAYBOOK.md](PLAYBOOK.md)** | ✅ What works vs ❌ what doesn't, the winning recipe, and which strategy runs on which account. **Read this before building anything new.** |
| [strategies/catalog.json](strategies/catalog.json) | Every strategy tested: exact parameters, backtest and live results, status (live / working / retired / failed) |
| `strategies/*.spec.json` | Full Astral strategy specs for the live strategies (ready to paste into `astral_strategy_build`) |
| [logs/paper-trading-log.md](logs/paper-trading-log.md) | Chronological log: deployments, swaps, check-ins, fills, lessons |
| [tools/build_spec.py](tools/build_spec.py) | Rebuild any catalog strategy into a full spec: `python3 tools/build_spec.py HV-G2 --size 0.12` |
| [tools/summarize_trades.py](tools/summarize_trades.py) | Summarize an Astral trade-history CSV: trades, win rate, P&L, trades/hour per strategy |

## Current live paper accounts
| Account | Strategy | Timeframe / coins | Size per coin |
|---|---|---|---|
| Paper try 1 ($10k) | HV-G2 RSI(2) fast scalper | 1-min, 15 coins | 10% |
| Paper2 ($100k) | HV-G2 RSI(2) fast scalper | 1-min, 15 coins | 10% |
| Paper3 ($100k) | HV-D mean reversion | 5-min, 4 coins | 23.75% |
| Paper4 ($100k) | HV-E2 RSI(2) scalper | 1-min, 10 coins | 18% |
| Paper5 ($100k) | HV-F3 Bollinger snap-back | 1-min, 15 coins | 6.5% |

## Important caveat
Astral Paper fills with **zero fees and zero slippage**. Paper profits on 1-min/5-min strategies are therefore optimistic — with realistic exchange costs (~0.1–0.2% per round trip) most short-timeframe edges disappear. The only design that stayed profitable *after* costs in backtests is the 1-hour SOL/LINK mean reversion ("MR1h-v2" in the catalog).

## Workflow
1. New idea → start from the winning recipe in `PLAYBOOK.md`.
2. Backtest in Astral (1-min, ≤10-day window for 15 coins to avoid timeouts).
3. Deploy to a paper account only when the account is flat.
4. After 15+ live trades: keep if win rate ≥ 55%, P&L ≥ −3%, and ≥ 5 trades/hr (1-min); otherwise replace.
5. Record the result in `PLAYBOOK.md` + `strategies/catalog.json`.
