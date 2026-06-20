import pandas as pd

def rank_stocks(results):

    df = pd.DataFrame(results)

    df = df.sort_values("score", ascending=False)

    df["rank"] = range(1, len(df) + 1)

    return df