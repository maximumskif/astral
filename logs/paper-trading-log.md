# Astral paper trading log

Targets: Paper try 1 $10k → $13k · Paper2 $100k → $120k · Paper3 $100k → $120k

| Account | Saved strategy | Rules | Backtest (2023–26, net of 5+5 bps) |
|---|---|---|---|
| Paper try 1 (PAPER-4B36) | 5906 SOL+LINK 1h v2 combo | 47.5%/coin | 243 trades, 63.0% WR, +36.4%, DD −13.5% |
| Paper2 (PAPER-38E4) | 5907 SOL 1h v2 full size | 95%/trade | 129 trades, 65.9% WR, +35.6%, DD −22.4% |
| Paper3 (PAPER-AE0E) | 5908 LINK 1h v2 full size | 95%/trade | 114 trades, 59.6% WR, +32.1%, DD −18.1% |

Kill/review rule: after 20+ live trades, if win rate < 50% or drawdown worse than backtest max DD, pause and re-test.

## Head-to-head research (1h, 95% sizing, 5+5 bps, 2023-01 → 2026-09)

| Variant | Coin | Trades | Win rate | Net | Max DD | Note |
|---|---|---|---|---|---|---|
| v2 (live) | SOL | 129 | 65.9% | +35.6% | −22.4% | best return |
| v5 quick TP +0.75 ATR | SOL | 134 | 73.1% | +16.4% | −11.4% | 2025–26 only: 69.2% WR, +1.5% |
| v4 bounce confirm | SOL | 119 | 64.7% | −17.7% | −44.4% | rejected |
| v2 (live) | LINK | 114 | 59.6% | +32.1% | −18.1% | |
| v5 quick TP | LINK | 118 | 71.2% | +11.9% | −11.8% | |

Verdict: v5 = higher hit rate (~71–73%) but roughly 1/3 the return; v2 stays live given $ targets.

## 2026-09-29 ~23:30 UTC — switched all 3 accounts to HIGH-VOLUME experiments (user request)

| Account | Saved | Experiment | Logic |
|---|---|---|---|
| Paper try 1 ($10k) | 5909 | HV-A 5m mean reversion SOL+LINK | close>EMA200 & <BB lower & RSI2<10; TP +1 ATR / SL −1.5 ATR / 12 bars |
| Paper2 ($100k) | 5910 | HV-B 5m Z-score scalper SOL/LINK/ETH/BTC | Z(20)<−2 & close>EMA100; TP +0.5 ATR / SL −2 ATR / 6 bars |
| Paper3 ($100k) | 5911 | HV-C 5m trend pullback SOL+LINK | EMA9>21>50, dip to EMA21 then bullish close, RSI14>45; TP +0.75 / SL −1.5 ATR / 12 bars |

1h v2 strategies (5906/5907/5908) parked as the proven low-volume fallback.
Learning rule: after 15+ closed trades, live WR < 55% or equity < 97% → replace with next variant.

## Check-ins

| Time (UTC) | Try1 equity | Paper2 equity | Paper3 equity | New fills since last | Notes |
|---|---|---|---|---|---|
| 2026-09-29 23:05 | $10,000 | $100,000 | $100,000 | 0 | Deployed 22:49; SOL & LINK in uptrend (above 200h EMA) |
| 2026-09-29 23:45 | $10,000 (5909 HV-A) | $100,000 (5910 HV-B) | $100,000 (5912 HV-D, replaced HV-C) | 0 | All active, no errors; HV-C (5911) failed backtest (58% WR, −20%) → replaced by HV-D (67% WR, +13.8%). HV-E/HV-F 1m 10-coin for Paper4/5 backtesting |

## 2026-09-29 ~23:55 UTC — Paper4 & Paper5 added (target 5–10 trades/hour/account)

| Account | Saved | Strategy | Backtest (1m, Sep 2–28 2026, no costs) |
|---|---|---|---|
| Paper4 (PAPER-D654) | 5913 | HV-E 1m RSI2 scalper, 10 coins (BTC ETH SOL LINK AVAX DOGE XRP ADA LTC DOT): close>EMA50 & RSI2<10; exit RSI2>70 or 3 bars; TP +0.6 / SL −1.5 ATR; 9.5%/coin | 5,078 trades (~7.8/hr), 62.0% WR, +5.7%, DD −1.1% ✅ |
| Paper5 (PAPER-687C) | 5914 | HV-F 1m Bollinger snap-back, same 10 coins: close<BB_L(20,2) & close>EMA100; exit BB mid or 5 bars; TP +0.5 / SL −2 ATR | 1,487 trades (~2.3/hr), 65.0% WR, +1.8%, DD −1.0% (volume below target → testing looser variant) |
| Paper3 | 5912 | HV-D 5m MR 4 coins (replaced failed HV-C) | 856 trades, 67.2% WR, +13.8%, DD −1.9% |

Lesson: HV-C 5m trend pullback = 1,990 trades but 58% WR, −20% even gross → trend-following at 5m fails; mean reversion wins.
- 2026-09-30 ~00:10 UTC: Paper5 swapped HV-F (5914, 2.3 trades/hr) → HV-F2 (5915, BB lower 1.5sd): bt 4,170 trades (~6.4/hr), 66.0% WR, +5.4%, DD −1.8%. Lesson: loosening band 2→1.5sd nearly tripled volume with no win-rate loss.
| 2026-09-30 00:08 | $10,000 (5909) | $100,000 (5910) | $100,000 (5912) | 0 | Paper4 5913 $100k, Paper5 5915 $100k; all 5 active/healthy/ready_to_trade, 0 fills, 0 positions. Watch: HV-E expected ~7.8/hr but 0 fills after ~30 min — if still 0 next check, investigate live signal evaluation |
| 2026-09-30 00:38 | $10,000 (5909, 0 fills) | $100,000 (5910, 0 fills) | ~$100,163 (5912: 2 round trips, 2/2 wins, +$75.08 & +$87.88) | 5 | FIRST FILLS. HV-D AVAX: buy 11.388 (=23:40 5m close) → TP sell 11.424; buy 11.360 (=00:15 close) → TP sell 11.402. Fees = 0 (notional exactly 23.75% of equity), slippage = 0 (fills at candle close / TP price). Paper4 HV-E: 1 open DOT buy @1.194 ($9,500). Paper5: 0. HV-E running well under 7.8/hr so far (1 fill in ~55 min) — recheck after a few hours |
| 2026-09-30 01:07 | $10,000 (5909, 0) | $100,000 (5910, 0) | ~$100,163 (5912, 2/2 W) | 4 | Paper4 HV-E: 2 round trips DOT, 2/2 wins (+$16.23, +$6.36) → ~$100,023. Paper5: 0. Live total 4/4 wins. HV-E ~1.6 trades/hr so far (below 7.8 bt). HV-G 15-coin backtest re-running on 10-day window (27-day run timed out) |
- 2026-09-30 ~01:10 UTC: HV-G (1m RSI2<20 & close>EMA50, exit RSI2>60 or 2 bars, TP +0.5/SL −1.5 ATR, 15 coins incl BCH UNI ATOM NEAR AAVE, 6.5%/coin) bt Sep 18–28: 8,607 trades (~33/hr), 60.2% WR, +1.6%, DD −1.2%. Deployed to Paper try 1 (5917) and Paper2 (5918), replacing 5m HV-A/HV-B (<1 trade/hr). Note: 15-coin 1m 27-day backtest times out at 300s → use ≤10-day windows. Lesson: loosening RSI2 10→20 + 2-bar exit + 15 coins = ~4x volume, WR 62→60%.
| 2026-09-30 01:51 | try1 HV-G: 39 trades, 74% WR, +$5.59, ~52/hr | Paper2 HV-G: 40 trades, 72% WR, +$47.75, ~55/hr | Paper3 HV-D: 2, 100%, +$162.96 | 101 closed total | Paper4 HV-E: 12, 58% WR, −$2.92, ~5.6/hr · Paper5 HV-F2: 8, 88% WR, +$71.58, ~4.1/hr. All targets met except Paper5 volume slightly <5/hr (too early) |
| 2026-09-30 02:20 | 5912 n=2 WR=100% pnl=$162.96 0.7/hr;5913 n=19 WR=74% pnl=$55.29 7.2/hr;5915 n=11 WR=82% pnl=$57.22 4.5/hr;5917 n=64 WR=73% pnl=$13.99 51.2/hr;5918 n=64 WR=72% pnl=$131.35 51.9/hr; | | | | auto check-in |
| 2026-09-30 03:50 | 5912 n=3 WR=100% pnl=$257.29 0.7/hr;5913 n=27 WR=78% pnl=$137.65 6.5/hr;5915 n=13 WR=85% pnl=$61.99 3.3/hr;5917 n=84 WR=68% pnl=$8.98 30.6/hr;5918 n=84 WR=67% pnl=$79.95 30.8/hr; | | | | auto check-in |
- 2026-09-30 ~04:15 UTC: Paper5 HV-F2 (5915) retired for volume (live 13 trades, 85% WR, +$62, but 3.3/hr < 5). Replaced by HV-F3 (5925: same Bollinger 1.5sd logic on 15 coins, 6.5%/coin): bt Sep 18–28 2,519 trades (~9.5/hr), 66.7% WR, ~flat (+0.02%). Lesson: HV-F2 had the best live win rate; adding coins fixes volume but per-trade edge is thin.
| 2026-09-30 04:16 | 5912 n=3 WR=100% pnl=$257.29 0.7/hr;5913 n=30 WR=80% pnl=$177.17 6.6/hr;5915 n=13 WR=85% pnl=$61.99 3.0/hr;5917 n=92 WR=70% pnl=$13.44 29.1/hr;5918 n=92 WR=68% pnl=$124.31 29.2/hr; | auto check-in |
- 2026-09-30 ~04:20 UTC: SIZE INCREASE (user request). Measured live peak concurrency: HV-G 9 positions, HV-E 5. Rebuilt & redeployed: HV-G2 10%/coin (was 6.5%) on Paper try 1 (5927) & Paper2 (5928); HV-E2 18%/coin (was 9.5%) on Paper4 (5926). Peak capital use ~90%. Same entry/exit logic. Still at old size: HV-D 23.75% (Paper3, 5912), HV-F3 6.5% (Paper5, 5925).
| 2026-09-30T08:51Z | 5927 n145 67% +$32 32/hr; 5928 n148 68% +$367 33/hr; 5926 n31 58% -$59 6.9/hr; 5912 n3 +$257; 5925 HV-F3 stuck warming up 5h (0 trades) -> redeployed. Cost-filter backtests: none survive holdout, nothing deployed | auto check-in |
| 2026-09-30T09:20Z | 5927 n183 73% +$63 37/hr; 5928 n186 73% +$679 37/hr; 5926 n33 61% -$20 6.6/hr; 5912 n3 +$257; 5925 HV-F3 0 trades yet (redeployed 08:51, 110-bar warmup) | auto check-in |
| 2026-09-30T09:50Z | 5927 n218 72% +$77 40/hr; 5928 n222 73% +$816 40/hr; 5926 n43 65% +$61 7.8/hr; 5912 n3 +$257; 5925 still 0 trades (warmup ~110 bars after 08:51 redeploy) | auto check-in |
| 2026-09-30T10:20Z | 5927 n252 73% +$90 42/hr; 5928 n251 73% +$902 42/hr; 5926 n52 63% +$44 8.7/hr; 5912 n3 +$257; 5925 0 trades (warmup) | auto check-in |
| 2026-09-30T10:52Z | 5927 n275 74% +$102 42/hr; 5928 n273 75% +$1,058 42/hr; 5926 n58 67% +$129 8.9/hr; 5912 n3 +$257. HV-F3 never traded: BCHUSD feed timeouts block warmup -> retired; deployed HV-F4 (14 coins, no BCH, saved 5935) on Paper5 | swap |
| 2026-09-30T11:20Z | 5927 n291 73% +$98 42/hr; 5928 n286 74% +$990 41/hr; 5926 n61 67% +$170 8.7/hr; 5912 n3 +$257; 5935 HV-F4 trading: n8 50% -$18 17/hr | auto check-in |
| 2026-09-30T11:50Z | 5927 n305 72% +$103 41/hr; 5928 n298 74% +$1,070 40/hr; 5926 n63 68% +$201 8.4/hr; 5912 n3 +$257; 5935 n10 60% +$5 10.5/hr | auto check-in |
| 2026-09-30T12:20Z | 5927 n333 71% +$97 42/hr; 5928 n331 73% +$1,095 41/hr; 5926 n71 70% +$297 8.9/hr; 5912 n3 +$257; 5935 HV-F4 n21 76% +$64 14/hr | auto check-in |
| 2026-09-30T14:20Z | 5927 n394 71% +$118; 5928 n399 72% +$1,346; 5926 n85 73% +$486; 5935 n52 83% +$149; 5912 +$257. ALL 1m strategies silent since ~13:36: ATOMUSD feed timeout -> HV-G2 x2 + HV-F4 degraded (auto-recovery pending); HV-E2 healthy but no fills. Watching; if still blocked next check, rebuild on thick-coin set c10 | auto check-in (issue) |
| 2026-09-30T14:53Z | ATOM feed stall persisted 80 min -> swapped (all accounts flat): Paper try 1 5927->5937 HV-G3, Paper2 5928->5938 HV-G3, Paper5 5935->5939 HV-F5 (13 coins, no BCH/ATOM). Final HV-G2: 399 tr 72% +$1,346 (P2), 394 tr 71% +$118 (try1); HV-F4 52 tr 83% +$149 | swap |
| 2026-09-30T15:20Z | HV-G3 (5937/5938) trading after swap: 2 tr each since 15:05; HV-F5 5939 warming up (110 bars, ~16:50); HV-E2 5926 n85 73% +$486, no fills since 13:31 (market dipping below EMA filters, SOL 121->119); HV-D 5912 n4 75% +$38 (one SOL loss), holding DOGE | auto check-in |
| 2026-09-30T15:50Z | HV-G3 5937 n21 95% +$17, 5938 n21 95% +$168 (24/hr); HV-E2 5926 resumed n88 74% +$561; HV-D 5912 n5 80% +$55; HV-F5 5939 warming up | auto check-in |
| 2026-09-30T16:20Z | HV-G3 5937 n56 89% +$37, 5938 n54 87% +$376 (~40/hr); HV-E2 5926 n100 77% +$753; HV-D 5912 n5 80% +$55; HV-F5 5939 live, first trade +$10 | auto check-in |
| 2026-09-30T16:44Z | User: +25% position size. All accounts flat -> swapped: try1 5937->5948 HV-G4 12.5%, P2 5938->5949 HV-G4 12.5%, P4 5926->5950 HV-E3 22.5%, P5 5939->5951 HV-F6 8.125%, P3 5912->5952 HV-D2 29.7% | swap |
| 2026-09-30T16:50Z | 1.25x sizes live: HV-G4 5948 n3 +$2, 5949 n3 +$25; HV-E3 5950 n1 +$29; HV-F6 5951 / HV-D2 5952 warming up | auto check-in |
| 2026-09-30T17:15Z | A/B started: Paper2 5949 HV-G4 -> 5953 HV-G5 (fast-exit, 11 coins). HV-G4 5949 final (1.25x): see th.csv | swap |
| 2026-09-30T17:44Z | quiet market since ~17:15 (few signals). see summ | auto check-in |
| 2026-09-30T18:15Z | very quiet market 17:15-18:15 (G4 +3 tr, G5 +1, F6 0 since 17:27; feeds OK since G4 on same coins traded 17:53) | auto check-in |
| 2026-09-30T18:45Z | still quiet; F6 no trades since 17:27 but G4 trading same coins (feeds OK, EMA100 filter blocking in dip) | auto check-in |
| 2026-09-30T19:15Z | quiet evening market, see summ (G4/F6/G5 few trades) | auto check-in |
| 2026-09-30T19:45Z | activity picking up; see summ | auto check-in |
| 2026-09-30T20:14Z | quiet; see summ | auto check-in |
| 2026-09-30T20:44Z | activity up; see summ | auto check-in |
| 2026-09-30T20:58Z | BREAK: user pausing. All 5 strategies left running on Astral. A/B G5 37tr 54% vs G4 70tr 70%. | note |
