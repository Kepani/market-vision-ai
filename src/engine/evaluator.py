def evaluate_bias(state):
    if state.price_above_vwap and state.higher_lows_present:
        return "bullish"
    if state.price_below_vwap and state.lower_highs_present:
        return "bearish"
    return "neutral"


def evaluate_displacement(state, rules):
    return state.displacement_detected


def evaluate_liquidity(state):
    if state.unfavorable_liquidity:
        return "unfavorable"
    if state.favorable_liquidity:
        return "favorable"
    return "unknown"
