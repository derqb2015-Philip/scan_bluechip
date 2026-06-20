# ==================================
# TVA SYSTEM CHECK
# ==================================

import sys
from pathlib import Path
import platform

# ===== THÊM ROOT PATH =====

ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT))

# ==========================

from config.settings import *

print()

print("=" * 50)

print("TVA SYSTEM CHECK")

print("=" * 50)

print()

print("Python :", platform.python_version())

print()

print("TVA :", Path(TVA_PATH).exists())

print("AmiBroker :", Path(AMIBROKER_PATH).exists())

print("Database :", Path(DATABASE_PATH).exists())

print("SQLite :", SQLITE_DB.exists())

print()

print("=" * 50)

if Path(AMIBROKER_PATH).exists():

    print("SYSTEM READY")

else:

    print("CHECK AMIBROKER PATH")

print("=" * 50)

print()