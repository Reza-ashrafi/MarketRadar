# data_provider.py

import requests
import pandas as pd
from datetime import datetime


# =========================
# 📊 1. قیمت صندوق (مثال: نقرابی)
# =========================
def get_fund_price(symbol="NQROBI"):
    """
    دریافت قیمت از TSETMC (یا هر API مشابه)
    """

    try:
        url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{symbol}"
        r = requests.get(url, timeout=10)
        data = r.json()

        # قیمت پایانی
        price = data["closingPriceInfo"]["pClosing"]
        return float(price)

    except Exception as e:
        print("Fund price error:", e)
        return None


# =========================
# 📊 2. NAV (ارزش ذاتی صندوق)
# =========================
def get_nav(symbol="NQROBI"):
    """
    NAV معمولاً جداگانه از سایت صندوق یا فرابورس میاد
    """

    try:
        url = f"https://api.fund-info.ir/nav/{symbol}"
        r = requests.get(url, timeout=10)
        data = r.json()

        return float(data["nav"])

    except Exception as e:
        print("NAV error:", e)
        return None


# =========================
# 💵 3. دلار آزاد (تقریبی بازار)
# =========================
def get_usd():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        r = requests.get(url, timeout=10)
        data = r.json()

        usd = data["rates"]["IRR"] / 10  # تبدیل به تومان تقریبی
        return float(usd)

    except Exception as e:
        print("USD error:", e)
        return 60000


# =========================
# 🧠 MAIN DATA BUILDER
# =========================
def get_market_data():

    price = get_fund_price()
    nav = get_nav()
    usd = get_usd()

    if price is None or nav is None:
        return None

    # =========================
    # محاسبه حباب واقعی
    # =========================
    bubble = ((price - nav) / nav) * 100

    return {
        "price": price,
        "nav": nav,
        "usd": usd,
        "bubble": bubble,
        "timestamp": datetime.now()
    }
