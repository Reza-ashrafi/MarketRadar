# data_provider.py

import requests
import random


# =========================
# قیمت لحظه‌ای
# =========================
def get_live_price(inscode="NQROBI"):

    try:
        url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{inscode}"
        r = requests.get(url, timeout=10)
        data = r.json()

        return float(data["closingPriceInfo"]["pClosing"])

    except:
        return None


# =========================
# ساخت دیتای تاریخی واقعی-شبیه‌سازی شده
# =========================
def get_historical_prices(days=50):

    base = get_live_price()

    if base is None:
        base = 100

    prices = []
    price = base

    for _ in range(days):

        change = random.uniform(-1.2, 1.2)
        price = price * (1 + change / 100)

        prices.append(round(price, 2))

    return prices


# =========================
# 👇 این همون چیزیه که main.py لازم داره
# =========================
def get_market_data():

    prices = get_historical_prices()

    return {
        "prices": prices,
        "highs": [p * 1.01 for p in prices],
        "lows": [p * 0.99 for p in prices],
        "closes": prices,
        "bubble": 0
    }
