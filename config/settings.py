# ==================================
# TVA SETTINGS
# ==================================

from pathlib import Path

# ===== CẦN THAY ĐỔI =====

TVA_PATH = r"D:\TVA"

AMIBROKER_PATH = r"C:\Program Files (x86)\AmiBroker"

DATABASE_NAME = "CP68"

# ⚠️ TẠM THỜI GIỮ NGUYÊN
DATABASE_PATH = r"C:\Program Files (x86)\AmiBroker\MetaStock"

# =======================

# Folder TVA

DATA_FOLDER = Path(TVA_PATH) / "data"

DATABASE_FOLDER = Path(TVA_PATH) / "database"

REPORT_FOLDER = Path(TVA_PATH) / "reports"

LOG_FOLDER = Path(TVA_PATH) / "logs"

BACKUP_FOLDER = Path(TVA_PATH) / "backup"

# File SQLite

SQLITE_DB = DATABASE_FOLDER / "market.db"

# Scheduler

UPDATE_INTERVAL = 120

START_TIME = "09:00"

STOP_TIME = "15:05"

# Market

EXCHANGES = [

    "HOSE",

    "HNX",

    "UPCOM"

]