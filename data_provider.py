# data_provider.py

import requests


# =========================
# گرفتن قیمت از TSETMC
# =========================
def get_fund_price(inscode="NQROBI"):

    try:
        url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{inscode}"
        r = requests.get(url, timeout=10)
        data = r.json()

        price = data["closingPriceInfo"]["pClosing"]
        return float(price)

    except Exception as e:
        print("TSETMC error:", e)
        return None


# =========================
# ساخت دیتای واقعی برای بک‌تست
# =========================
def get_historical_data_mock_real():

    # ⚠️ اگر API تاریخچه نداشتی، از قیمت واقعی اخیر شروع می‌کنیم
    base_price = get_fund_price()

    if base_price is None:
        base_price = 100

    # شبیه‌سازی نزدیک به واقعیت بازار (نوسان کم صندوق طلا/نقره)
    prices = []
    price = base_price

    for i in range(30):

        import random

        change = random.uniform(-1.5, 1.5)  # نوسان واقعی بازار صندوق‌ها
        price = price * (1 + change / 100)

        prices.append(round(price, 2))

    return prices
