import pandas as pd
from core.scorer import compute_score
from core.tplus_simulator import simulate_tplus

from signals.breakout import detect_breakout
from signals.reversal import detect_reversal
from signals.wyckoff import detect_wyckoff
from signals.minervini import detect_minervini
from signals.rs import calc_relative_strength
from signals.money_flow import detect_money_flow
from signals.support_resistance import detect_sr
from signals.fibonacci import detect_fib_zone


def analyze_stock(df: pd.DataFrame, index_df: pd.DataFrame, symbol: str):

    result = {}

    # ===== SIGNALS =====
    result["breakout"] = detect_breakout(df)
    result["reversal"] = detect_reversal(df)
    result["wyckoff"] = detect_wyckoff(df)
    result["minervini"] = detect_minervini(df)
    result["rs"] = calc_relative_strength(df, index_df)
    result["money_flow"] = detect_money_flow(df)
    result["sr"] = detect_sr(df)
    result["fib"] = detect_fib_zone(df)

    # ===== SCORING =====
    score = compute_score(result)

    # ===== T+ SIMULATION =====
    tplus = simulate_tplus(df)

    return {
        "symbol": symbol,
        "score": score,
        "signals": result,
        "tplus": tplus
    }