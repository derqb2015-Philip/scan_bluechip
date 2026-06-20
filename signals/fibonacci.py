def detect_fib_zone(df):
    if len(df) < 30:
        return False

    high = df["close"][-30:].max()
    low = df["close"][-30:].min()
    price = df["close"].iloc[-1]

    fib_382 = high - (high - low) * 0.382
    fib_50 = high - (high - low) * 0.5
    fib_618 = high - (high - low) * 0.618

    return abs(price - fib_382) / high < 0.02 or \
           abs(price - fib_50) / high < 0.02 or \
           abs(price - fib_618) / high < 0.02