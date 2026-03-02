import streamlit as st
import pandas as pd
import numpy as np
from vnstock import *

st.set_page_config(layout="wide")

STOCKS = [
"VCB","BID","CTG","TCB","MBB",
"VIC","VHM","VRE",
"HPG","HSG","DPM","DCM","PLC",
"FPT","MWG",
"GAS","PLX","OIL","PVS","PVT","PVD","BSR",
"SSI","VND",
"VPB","ACB",
"SAB","MSN","MML","MCH","MSR",
"BVH","POW",
"STB","TPB",
"PNJ","VJC",
"GVR","DGC",
"KDH","BCM",
"VJC","HAH","CEO","NLG"
]

def calculate_indicators(df):

    df = df.sort_values("time")

    exp1 = df['close'].ewm(span=12, adjust=False).mean()
    exp2 = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = exp1 - exp2
    df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()

    df['ma20'] = df['close'].rolling(20).mean()
    df['std'] = df['close'].rolling(20).std()
    df['upper'] = df['ma20'] + 2*df['std']
    df['lower'] = df['ma20'] - 2*df['std']

    low_min = df['low'].rolling(14).min()
    high_max = df['high'].rolling(14).max()
    df['%K'] = 100 * ((df['close'] - low_min) / (high_max - low_min))
    df['%D'] = df['%K'].rolling(3).mean()

    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))

    return df


def check_signal(df):

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    buy = (
        prev['macd'] < prev['signal'] and
        latest['macd'] > latest['signal'] and
        latest['close'] <= latest['lower'] * 1.02 and
        latest['%K'] < 30 and
        latest['%K'] > latest['%D'] and
        latest['rsi'] < 35 and
        latest['rsi'] > prev['rsi']
    )

    sell = (
        prev['macd'] > prev['signal'] and
        latest['macd'] < latest['signal'] and
        latest['close'] >= latest['upper'] * 0.98 and
        latest['%K'] > 60 and
        latest['%K'] < latest['%D'] and
        latest['rsi'] > 55 and
        latest['rsi'] < prev['rsi']
    )

    if buy:
        return "BUY"
    elif sell:
        return "SELL"
    else:
        return None


st.title("📊 BLUECHIP SCANNER VN")

if st.button("🔍 QUÉT THỊ TRƯỜNG BLUECHIP_VN"):

    results = []

    for stock in STOCKS:
        try:
            df = stock_historical_data(
                symbol=stock,
                start_date="2025-01-01"
            )

            df = calculate_indicators(df)

            if len(df) < 30:
                continue

            signal = check_signal(df)

            if signal:
                price = df.iloc[-1]['close']
                results.append({
                    "Mã": stock,
                    "Giá": round(price,2),
                    "Tín hiệu": signal
                })

        except:
            continue

    if results:
        df_result = pd.DataFrame(results)
        st.dataframe(df_result, use_container_width=True)
    else:

        st.warning("Không có tín hiệu hôm nay.")




