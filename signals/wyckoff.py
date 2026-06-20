def detect_wyckoff(df):
    if len(df) < 30:
        return False

    vol = df["volume"]
    price = df["close"]

    avg_vol = vol[-20:].mean()
    range_size = price[-20:].max() - price[-20:].min()

    # accumulation-like condition
    low_vol = vol[-10:].mean() < avg_vol * 0.8
    breakout = price.iloc[-1] > price[-20:].max()

    return low_vol and breakout