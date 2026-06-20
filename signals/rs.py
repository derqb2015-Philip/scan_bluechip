def calc_relative_strength(stock_df, index_df):
    if len(stock_df) < 20 or len(index_df) < 20:
        return 0

    stock_ret = stock_df["close"].pct_change().sum()
    index_ret = index_df["close"].pct_change().sum()

    rs = (stock_ret - index_ret) * 100

    return round(max(0, rs), 2)