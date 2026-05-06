from vnstock import register_user
register_user(api_key='vnstock_585e95e6d7c5e379910fa8f6be9fecae')
import streamlit as st
import pandas as pd
import numpy as np
from vnstock import Vnstock
import time

st.set_page_config(layout="wide")

# ===== DANH SÁCH MÃ =====
STOCKS =  [
    "VCB","BID","CTG","TCB","MBB","VPB","ACB","STB","SHB",
    "HPG","HSG","NKG","FPT","MWG","PNJ","REE","GMD","VHC",
    "VNM","SAB","MSN","SSI","VND","HCM","GAS","PLX","POW",
    "BVH","VIC","VHM","VRE","DXG","DIG","KBC","PDR","NVL",
    "DPM","DCM","ANV","PVS","PVD","KDH","HDG","HDC","CSV",
    "CMG","BWE","SZC","TCH","IDC","VPI","BCM","CTR","CII",
    "HAG","HNG","NLG","KSB","GEX","VGC","MSB","OCB","TPB"
    ]
# ===== INDICATORS =====
def calc(df):

    df = df.sort_values("time")

    # MA
    df['ma20'] = df['close'].rolling(20).mean()

    # MACD
    exp1 = df['close'].ewm(span=12).mean()
    exp2 = df['close'].ewm(span=26).mean()
    df['macd'] = exp1 - exp2
    df['signal'] = df['macd'].ewm(span=9).mean()

    # RSI
    delta = df['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))

    # Bollinger
    df['std'] = df['close'].rolling(20).std()
    df['upper'] = df['ma20'] + 2*df['std']
    df['lower'] = df['ma20'] - 2*df['std']

    # Volume
    df['vol_ma20'] = df['volume'].rolling(20).mean()

    return df

# ===== CHẤM ĐIỂM =====
def score(df):

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    s = 0

    # MACD
    if prev['macd'] < prev['signal'] and latest['macd'] > latest['signal']:
        s += 20

    # RSI
    if 45 < latest['rsi'] < 60 and latest['rsi'] > prev['rsi']:
        s += 15

    # Trend
    if latest['close'] > latest['ma20']:
        s += 15

    # BB squeeze
    width = (latest['upper'] - latest['lower']) / latest['ma20']
    if width < 0.1:
        s += 10

    # Volume
    if latest['volume'] > latest['vol_ma20'] * 1.5:
        s += 20

    # Breakout
    if latest['close'] > df['close'].rolling(20).max().iloc[-2]:
        s += 20

    return s

# ===== MAIN =====
st.title("🔥 AI STOCK SCANNER VN – PRO")

if st.button("🚀 QUÉT TOÀN THỊ TRƯỜNG"):

    results = []

    progress = st.progress(0)

    for i, stock in enumerate(STOCKS[:300]):

        try:
            df = stock_historical_data(stock, "2024-01-01")
            if len(df) < 30:
                continue

            df = calc(df)

            sc = score(df)

            if sc >= 70:
                price = df.iloc[-1]['close']

                results.append({
                    "Mã": stock,
                    "Giá": round(price,2),
                    "Điểm": sc,
                    "TP": round(price*1.05,2),
                    "SL": round(price*0.97,2)
                })

        except:
            continue

        progress.progress((i+1)/300)

    if results:
        df_out = pd.DataFrame(results).sort_values(by="Điểm", ascending=False)
        st.dataframe(df_out, use_container_width=True)
    else:
        st.warning("Không có kèo ngon hôm nay.")

# ===== AUTO REFRESH =====
time.sleep(60)
st.rerun()
