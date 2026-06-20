def detect_sr(df):
    if len(df) < 20:
        return None

    close = df["close"]

    resistance = close[-20:].max()
    support = close[-20:].min()

    last = close.iloc[-1]

    if last >= resistance * 0.99:
        return "resistance_break"

    if last <= support * 1.01:
        return "support_bounce"

    return None