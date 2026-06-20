# ==================================
# TVA CORE ENGINE
# ==================================

import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT))

from config.settings import *


def create_export_folder():

    export_path = DATA_FOLDER / "export"

    export_path.mkdir(parents=True, exist_ok=True)

    return export_path


def create_watch_folder():

    watch_path = DATA_FOLDER / "watch"

    watch_path.mkdir(parents=True, exist_ok=True)

    return watch_path


def create_runtime_folder():

    runtime_path = DATA_FOLDER / "runtime"

    runtime_path.mkdir(parents=True, exist_ok=True)

    return runtime_path


def write_log(message):

    logfile = LOG_FOLDER / "system.log"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(logfile, "a", encoding="utf-8") as f:

        f.write(f"{now} : {message}\n")


def system_initialize():

    print()

    print("="*50)

    print("TVA CORE ENGINE")

    print("="*50)

    print()

    create_export_folder()

    create_watch_folder()

    create_runtime_folder()

    write_log("TVA Core initialized")

    print("[OK] Export folder")

    print("[OK] Watch folder")

    print("[OK] Runtime folder")

    print()

    print("[SUCCESS] TVA Core ready")

    print()


if __name__ == "__main__":

    system_initialize()