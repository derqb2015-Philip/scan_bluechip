import os
import pandas as pd

from engine.tva_engine import analyze_stock
from core.ranker import rank_stocks

# =========================
# CONFIG
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SYMBOL_FILE = os.path.join(BASE_DIR, "data", "symbols.csv")
DATA_DIR = os.path.join(BASE_DIR, "data", "price_data")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "scan_result.csv")

INDEX_FILE = os.path.join(DATA_DIR, "VNINDEX.csv")


# =========================
# LOAD SYMBOLS
# =========================

def load_symbols():
    df = pd.read_csv(SYMBOL_FILE)
    return df["symbol"].dropna().unique().tolist()


# =========================
# LOAD PRICE DATA
# =========================

def load_price(symbol):
    path = os.path.join(DATA_DIR, f"{symbol}.csv")

    if not os.path.exists(path):
        return None

    df = pd.read_csv(path)

    required_cols = ["open", "high", "low", "close", "volume"]
    for c in required_cols:
        if c not in df.columns:
            return None

    return df


# =========================
# MAIN SCAN ENGINE
# =========================

def run_scan():

    symbols = load_symbols()

    index_df = load_price("VNINDEX")

    results = []

    print(f"🚀 Scanning {len(symbols)} symbols...")

    for sym in symbols:

        df = load_price(sym)

        if df is None or len(df) < 50:
            continue

        try:
            result = analyze_stock(df, index_df, sym)

            results.append({
                "symbol": sym,
                "score": result["score"],
                "signals": str(result["signals"]),
                "tplus3": result["tplus"]["tplus3"],
                "tplus5": result["tplus"]["tplus5"],
                "tplus10": result["tplus"]["tplus10"],
            })

        except Exception as e:
            print(f"❌ Error {sym}: {e}")

    # =========================
    # RANKING
    # =========================

    df_result = pd.DataFrame(results)

    if df_result.empty:
        print("❌ No data processed")
        return

    df_result = df_result.sort_values("score", ascending=False)

    df_result["rank"] = range(1, len(df_result) + 1)

    # =========================
    # EXPORT
    # =========================

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    df_result.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Scan completed: {OUTPUT_FILE}")
    print(df_result.head(10))


# =========================
# RUN
# =========================

if __name__ == "__main__":
    run_scan()