def detect_money_flow(df):
    if len(df) < 20:
        return False

    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    money_flow = typical_price * df["volume"]

    flow_up = money_flow[-5:].mean() > money_flow[-20:].mean()

    return bool(flow_up)