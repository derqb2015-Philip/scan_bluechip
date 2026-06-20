import streamlit as st
import pandas as pd
import os

# =====================
# CONFIG
# =====================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "output",
    "scan_result.csv"
)

st.set_page_config(
    page_title="TVA Dashboard",
    layout="wide"
)

st.title("🚀 TVA Scanner Dashboard")

# =====================
# CHECK FILE
# =====================

if not os.path.exists(DATA_PATH):

    st.error("❌ Chưa tìm thấy output/scan_result.csv")

    st.info("""
1. Chạy run_scan.py trước

python run_scan.py

2. Sau đó chạy lại Dashboard

streamlit run dashboard/app.py
""")

    st.stop()

# =====================
# LOAD DATA
# =====================

df = pd.read_csv(DATA_PATH)

# =====================
# METRICS
# =====================

col1, col2, col3 = st.columns(3)

col1.metric("Tổng số mã", len(df))

col2.metric("Điểm cao nhất", int(df["score"].max()))

col3.metric("Điểm trung bình", round(df["score"].mean(), 1))

st.divider()

# =====================
# TOP 20
# =====================

st.subheader("🏆 Top 20")

top20 = df.sort_values(
    "score",
    ascending=False
).head(20)

st.dataframe(
    top20,
    use_container_width=True
)

# =====================
# FILTER
# =====================

st.subheader("🔍 Filter")

search = st.text_input("Nhập mã cổ phiếu")

if search:

    result = df[
        df["symbol"].str.contains(
            search.upper(),
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

# =====================
# SCORE CHART
# =====================

st.subheader("📊 Score Distribution")

st.bar_chart(df["score"])