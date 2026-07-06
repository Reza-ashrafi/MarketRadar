# data_provider.py

import requests
import random


# =========================
# قیمت لحظه‌ای (واقعی TSETMC)
# =========================
def get_fund_price(inscode="NQROBI"):

    try:
        url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{inscode}"
        r = requests.get(url, timeout=10)
        data = r.json()

        return float(data["closingPriceInfo"]["pClosing"])

    except:
        return None


# =========================
# ساخت دیتای تاریخی برای بک‌تست
# =========================
def get_historical_prices():

    base = get_fund_price()

    if base is None:
        base = 100

    prices = []
    price = base

    for _ in range(50):

        change = random.uniform(-1.2, 1.2)
        price = price * (1 + change / 100)

        prices.append(round(price, 2))

    return prices


# =========================
# تابع اصلی که MAIN صدا می‌زند
# =========================
def get_market_data():

    prices = get_historical_prices()

    return {
        "prices": prices,
        "highs": [p * 1.01 for p in prices],
        "lows": [p * 0.99 for p in prices],
        "closes": prices,
        "bubble": 0  # اگر NAV داشتی اینجا واقعی میشه
    }
