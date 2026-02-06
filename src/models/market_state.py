from dataclasses import dataclass

@dataclass
class MarketState:
    price_above_vwap: bool
    price_below_vwap: bool
    price_near_vwap: bool

    higher_lows_present: bool
    lower_highs_present: bool
    overlapping_candles: bool

    displacement_detected: bool
    candles_since_displacement: int

    favorable_liquidity: bool
    unfavorable_liquidity: bool

    volume_expanding: bool
    volume_contracting: bool
    volume_diverging: bool

    risk_reward: float
    entry_at_extreme: bool
    news_volatility: bool
