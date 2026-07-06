import requests


# =========================
# 🥇 قیمت طلا جهانی (برای پایه)
# =========================
def get_gold_price():
    try:
        url = "https://api.metals.live/v1/spot"
        r = requests.get(url, timeout=5)
        data = r.json()

        for item in data:
            if item.get("metal") == "gold":
                return float(item.get("price"))
    except:
        pass

    # fallback منطقی طلا
    return 2300


# =========================
# 💵 دلار
# =========================
def get_usd_price():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        r = requests.get(url, timeout=5)
        data = r.json()

        irr = data["rates"]["IRR"]
        return float(irr) / 10
    except:
        return 600000


# =========================
# 🥈 محاسبه نقره از طلا (بدون API)
# =========================
def calculate_silver_from_gold(gold_price):
    # Gold/Silver Ratio تاریخی حدود 70 تا 90
    GSR = 80

    silver = gold_price / GSR
    return silver


# =========================
# 📦 ارزش ذاتی
# =========================
def intrinsic_value(silver, usd):
    return (silver * usd * 31.1) / 1000


# =========================
# 💣 حباب
# =========================
def bubble_calc(intrinsic, market):
    return ((market - intrinsic) / intrinsic) * 100


# =========================
# 🧠 تحلیل نهایی
# =========================
def analyze():

    gold = get_gold_price()
    usd = get_usd_price()

    silver = calculate_silver_from_gold(gold)

    intrinsic = intrinsic_value(silver, usd)

    # بازار ایران (حباب طبیعی)
    market = intrinsic * 1.06

    bubble = bubble_calc(intrinsic, market)

    score = 100 - abs(bubble) * 2
    score = max(0, min(100, score))

    # =========================
    # 🚦 سیگنال حرفه‌ای
    # =========================
    if bubble < 2:
        signal = "🟢 خرید قوی"
    elif bubble < 6:
        signal = "🟢 ورود پله‌ای"
    elif bubble < 12:
        signal = "🟡 صبر"
    elif bubble < 20:
        signal = "🔴 پرریسک"
    else:
        signal = "🔴 حباب بالا"

    return {
        "gold": gold,
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "signal": signal
    }
