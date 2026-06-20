import numpy as np

def simulate_tplus(df):

    close = df["close"].values

    def calc(n):
        if len(close) <= n:
            return None
        return float((close[n] - close[0]) / close[0] * 100)

    return {
        "tplus3": calc(3),
        "tplus5": calc(5),
        "tplus10": calc(10)
    }