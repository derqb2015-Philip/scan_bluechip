# ==================================
# TVA - 01_data_collector.py
# Version 1.0
# ==================================

from pathlib import Path
import sqlite3
from datetime import datetime

# ==================================
# ===== CẦN THAY ĐỔI =====

TVA_PATH = r"D:\TVA"

# ==================================


def create_folders():

    folders = [
        "config",
        "data",
        "database",
        "engine",
        "scheduler",
        "reports",
        "web",
        "mobile",
        "logs",
        "backup"
    ]

    for folder in folders:

        path = Path(TVA_PATH) / folder

        path.mkdir(parents=True, exist_ok=True)

        print(f"[OK] {path}")


def create_database():

    db_file = Path(TVA_PATH) / "database" / "market.db"

    conn = sqlite3.connect(db_file)

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS market_data (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        ticker TEXT,

        date TEXT,

        open REAL,

        high REAL,

        low REAL,

        close REAL,

        volume INTEGER,

        exchange TEXT,

        updated_at TEXT

    )

    """)

    conn.commit()

    conn.close()

    print(f"[OK] Database created : {db_file}")


def create_log():

    logfile = Path(TVA_PATH) / "logs" / "system.log"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(logfile, "a", encoding="utf-8") as f:

        f.write(f"{now} : TVA initialized\n")

    print("[OK] Log initialized")


def main():

    print()

    print("=" * 40)

    print("TVA INITIALIZATION")

    print("=" * 40)

    create_folders()

    create_database()

    create_log()

    print()

    print("[SUCCESS] TVA ready")

    print()


if __name__ == "__main__":

    main()