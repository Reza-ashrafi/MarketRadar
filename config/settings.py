import os

PROJECT_NAME = "MarketRadar"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "storage")

SNAPSHOT_DIR = os.path.join(DATA_DIR, "snapshots")

SHAREHOLDER_DIR = os.path.join(DATA_DIR, "shareholders")

SYMBOL_DIR = os.path.join(DATA_DIR, "symbols")

LOG_DIR = os.path.join(BASE_DIR, "logs")

REQUEST_TIMEOUT = 15

RETRY_COUNT = 3
