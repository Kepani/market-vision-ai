1. Purpose

This model defines when entries are allowed, discouraged, or invalid based on price displacement, liquidity behavior, and momentum.
The system is advisory only and never executes trades.

2. Market Assumptions

Intraday trading (1m–5m primary timeframe)

Liquid instruments (SPY, QQQ, ES, NQ, large-cap equities)

Chart contains:

Candlesticks

VWAP with bands

Volume histogram

3. Bias Determination

Bias must be established before any entry logic runs.

3.1 Bullish Bias

Bias is bullish if:

Price is above VWAP

Higher lows are present

No recent strong bearish displacement candle

3.2 Bearish Bias

Bias is bearish if:

Price is below VWAP

Lower highs are present

No recent strong bullish displacement candle

3.3 No Trade Bias

Bias is neutral if:

Price is chopping around VWAP

Overlapping candles dominate

Volume is declining or inconsistent

If bias = neutral → NO TRADES

4. Displacement Definition

A displacement candle is required to signal intent.

A candle qualifies as displacement if:

Candle body ≥ 1.5× average body size of last 10 candles

Candle closes near its high (bullish) or low (bearish)

Volume is above recent average

Displacement alone is not an entry.

5. Liquidity Conditions

Entries require liquidity alignment.

5.1 Favorable Liquidity

Clear liquidity resting above highs (shorts) or below lows (longs)

Recent stop run or liquidity sweep supports direction

5.2 Unfavorable Liquidity

No visible liquidity in trade direction

Entry would occur into opposing liquidity

If liquidity is unfavorable → ENTRY DISCOURAGED

6. Entry Conditions

An entry is allowed only if ALL are true:

Bias is defined (bullish or bearish)

A valid displacement candle occurred

Price retraces toward:

VWAP

VWAP band

Displacement origin

Entry is not at candle extreme

7. Late Entry Rules

An entry is invalid (late) if:

Entry occurs ≥ 2 candles after displacement

Entry occurs at or near session high/low

Risk-to-reward < predefined minimum (2:1 default)

8. Volume Confirmation

Volume should:

Expand during displacement

Contract during pullback

Re-expand on continuation

If volume diverges → ENTRY DISCOURAGED

9. Hard No-Trade Conditions

The system must explicitly warn if:

Choppy overlapping candles

Low volume session

News volatility spike

Entry violates bias

10. System Feedback States

The AI outputs one of:

VALID ENTRY

WAIT

LATE

DISCOURAGED

NO TRADE

Each output must include a short reason.

11. Non-Goals

No prediction

No execution

No profit guarantees

12. Philosophy

The system exists to prevent bad trades, not find more trades.