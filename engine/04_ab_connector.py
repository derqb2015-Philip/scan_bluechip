# ==================================
# TVA - AMIBROKER CONNECTOR
# ==================================

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT))

try:

    import win32com.client

except:

    print()

    print("CHUA CAI PYWIN32")

    print()

    print("pip install pywin32")

    quit()


print()

print("="*50)

print("TVA AMIBROKER CONNECTOR")

print("="*50)

print()

try:

    AB = win32com.client.Dispatch("Broker.Application")

    print("[OK] AmiBroker connected")

    print()

    print("Version :", AB.Version)

    print()

    print("[SUCCESS] Ready")

except Exception as e:

    print()

    print("[ERROR]")

    print(e)

print()