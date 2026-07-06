from sources import get_silver_price, get_usd_rate

OZ_TO_GRAM = 31.1035


def analyze():

    silver = get_silver_price()
    usd = get_usd_rate()

    if not silver or not usd:
        return {"error": True}

    intrinsic = (1000 / OZ_TO_GRAM) * silver * usd

    # چون بازار نداریم فعلاً:
    market = intrinsic * 1.03  # فرض ساده 3% اختلاف

    bubble = ((market - intrinsic) / intrinsic) * 100

    # تصمیم ساده
    if bubble < 2:
        signal = "🟢 خوبه برای خرید"
    elif bubble < 6:
        signal = "🟡 معمولی"
    else:
        signal = "🔴 فعلاً نخر"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "signal": signal
    }
