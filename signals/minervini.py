def detect_minervini(df):
    if len(df) < 50:
        return False

    close = df["close"]

    ma20 = close.rolling(20).mean()
    ma50 = close.rolling(50).mean()

    trend_up = ma20.iloc[-1] > ma50.iloc[-1]
    price_above_ma = close.iloc[-1] > ma20.iloc[-1]

    return bool(trend_up and price_above_ma)