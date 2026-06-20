import numpy as np

def detect_breakout(df):
    close = df["close"]
    volume = df["volume"]

    if len(close) < 20:
        return False

    highest_20 = close[-20:].max()
    avg_vol = volume[-20:].mean()

    is_breakout = close.iloc[-1] > highest_20 and volume.iloc[-1] > 1.5 * avg_vol

    return bool(is_breakout)