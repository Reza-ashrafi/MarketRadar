import requests


def get_silver_price():
    try:
        url = "https://api.metals.live/v1/spot"
        r = requests.get(url, timeout=10)
        data = r.json()

        for item in data:
            if item.get("metal") == "silver":
                return float(item.get("price"))
    except:
        pass

    return 28.5


def get_usd_price():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        r = requests.get(url, timeout=5)
        data = r.json()

        irr = data["rates"]["IRR"]
        return float(irr) / 10
    except:
        return 60000


def analyze():
    silver = get_silver_price()
    usd = get_usd_price()

    fair_value = (silver * usd * 31.1) / 1000
    market = fair_value * 1.05

    bubble = ((market - fair_value) / fair_value) * 100

    score = 100 - abs(bubble) * 2
    score = max(0, min(100, score))

    if bubble < 5:
        decision = "🟢 مناسب ورود"
    elif bubble < 15:
        decision = "🟡 محتاط"
    else:
        decision = "🔴 پرریسک"

    return {
        "silver": silver,
        "usd": usd,
        "fair": fair_value,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }
