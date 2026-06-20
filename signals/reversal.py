def detect_reversal(df):
    if len(df) < 3:
        return None

    close = df["close"]

    # simple slope check
    if close.iloc[-3] > close.iloc[-2] > close.iloc[-1]:
        return "bearish"

    if close.iloc[-3] < close.iloc[-2] < close.iloc[-1]:
        return "bullish"

    return None