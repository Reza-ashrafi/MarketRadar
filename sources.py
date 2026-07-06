import requests
from config import SILVER_API, REQUEST_TIMEOUT

def get_silver_price():
    try:
        r = requests.get(SILVER_API, timeout=REQUEST_TIMEOUT)
        data = r.json()
        return float(data[0]["price"])
    except:
        return None


def get_usd_rate():
    try:
        # API ساده و عمومی
        r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=IRR")
        data = r.json()
        return data["rates"]["IRR"] / 10
    except:
        return None


def get_market_price():
    # فعلاً ساده‌سازی شده (بعداً TGJU اضافه می‌کنیم)
    # چون اسکرپینگ الان ریسک کرش داره
    return None
