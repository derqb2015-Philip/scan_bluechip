def compute_score(sig):

    score = 0

    # Breakout
    if sig["breakout"]:
        score += 20

    # Reversal
    if sig["reversal"] == "bullish":
        score += 15
    elif sig["reversal"] == "bearish":
        score -= 10

    # Wyckoff
    if sig["wyckoff"]:
        score += 10

    # Minervini
    if sig["minervini"]:
        score += 15

    # RS
    score += min(sig["rs"], 15)

    # Money flow
    if sig["money_flow"]:
        score += 10

    # Support/Resistance breakout zone
    if sig["sr"] == "support_bounce":
        score += 5
    elif sig["sr"] == "resistance_break":
        score += 10

    # Fibonacci
    if sig["fib"]:
        score += 5

    return max(0, min(score, 100))