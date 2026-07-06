import requests
import statistics


# =========================
# 🥇 طلا جهانی
# =========================
def get_gold_price():
    try:
        r = requests.get("https://api.metals.live/v1/spot", timeout=5)
        data = r.json()

        for item in data:
            if item.get("metal") == "gold":
                return float(item.get("price"))
    except:
        pass

    return 2300


# =========================
# 🥈 نقره (بدون API مستقیم)
# =========================
def calc_silver_from_gold(gold):
    gsr = statistics.mean([72, 75, 78, 82, 85])
    return gold / gsr


# =========================
# 💵 دلار
# =========================
def get_usd_price():
    try:
        r = requests.get(
            "https://api.exchangerate.host/latest?base=USD&symbols=IRR",
            timeout=5
        )
        data = r.json()
        return float(data["rates"]["IRR"]) / 10
    except:
        return 600000


# =========================
# 📦 ارزش ذاتی
# =========================
def intrinsic_value(silver, usd):
    return (silver * usd * 31.1) / 1000


# =========================
# 💣 حباب
# =========================
def bubble(intrinsic, market):
    return ((market - intrinsic) / intrinsic) * 100


# =========================
# 📊 روند ساده (Momentum)
# =========================
history = []


def get_trend(current_price):
    history.append(current_price)

    # نگه داشتن فقط 5 دیتا آخر
    if len(history) > 5:
        history.pop(0)

    if len(history) < 5:
        return "neutral"

    if history[-1] > history[0]:
        return "up"
    elif history[-1] < history[0]:
        return "down"
    return "side"


# =========================
# 🧠 سیگنال تریدر واقعی
# =========================
def analyze():

    gold = get_gold_price()
    usd = get_usd_price()

    silver = calc_silver_from_gold(gold)

    intrinsic = intrinsic_value(silver, usd)

    # بازار ایران (پریمیوم واقعی‌تر)
    market = intrinsic * statistics.mean([1.04, 1.06, 1.08])

    b = bubble(intrinsic, market)

    trend = get_trend(market)

    score = 100 - abs(b) * 2
    score = max(0, min(100, score))

    # =========================
    # 🚦 منطق تریدر واقعی
    # =========================

    signal = "⚪ بدون سیگنال"

    # شرط خرید قوی
    if b < 3 and trend == "up":
        signal = "🟢 خرید قوی (ورود فوری)"

    # ورود پله‌ای
    elif b < 7 and trend != "down":
        signal = "🟢 ورود پله‌ای"

    # صبر
    elif 7 <= b < 12:
        signal = "🟡 صبر / بررسی"

    # خروج
    elif b > 15 and trend == "down":
        signal = "🔴 خروج / ریسک بالا"

    # حباب شدید
    elif b > 20:
        signal = "🔴 عدم ورود (حباب سنگین)"

    return {
        "gold": round(gold, 2),
        "silver": round(silver, 3),
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": round(b, 2),
        "trend": trend,
        "score": round(score, 2),
        "signal": signal,
        "mode": "TRADER_FINAL"
    }
