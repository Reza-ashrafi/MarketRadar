# score_engine.py

from config import WEIGHTS


# =========================
# Trend Score
# =========================
def trend_score(ema20, ema50):
    if ema20 > ema50:
        return 80
    elif ema20 < ema50:
        return 40
    return 60


# =========================
# Value Score (حباب)
# =========================
def value_score(bubble):
    if bubble < 0:
        return 90
    elif bubble < 5:
        return 80
    elif bubble < 10:
        return 60
    elif bubble < 15:
        return 40
    return 20


# =========================
# Momentum Score
# =========================
def momentum_score(rsi, macd):
    score = 50

    if 40 <= rsi <= 60:
        score += 20  # ناحیه سالم
    elif rsi > 70:
        score -= 20  # اشباع خرید
    elif rsi < 30:
        score += 10  # اشباع فروش

    if macd > 0:
        score += 15
    else:
        score -= 10

    return max(0, min(100, score))


# =========================
# Risk Score (برعکس: هرچی بیشتر، بهتر)
# =========================
def risk_score(atr, bollinger_width):
    score = 100

    if atr > 0:
        score -= atr * 2

    if bollinger_width > 0:
        score -= bollinger_width * 1.5

    return max(0, min(100, score))


# =========================
# Capital Score
# =========================
def capital_score(score):
    if score > 85:
        return 90
    elif score > 70:
        return 70
    elif score > 55:
        return 40
    return 10


# =========================
# FINAL SCORE (مغز اصلی)
# =========================
def final_score(inputs):
    """
    inputs:
    {
        ema20, ema50,
        bubble,
        rsi, macd,
        atr, bollinger_width
    }
    """

    trend = trend_score(inputs["ema20"], inputs["ema50"])
    value = value_score(inputs["bubble"])
    momentum = momentum_score(inputs["rsi"], inputs["macd"])
    risk = risk_score(inputs["atr"], inputs["bollinger_width"])
    capital = capital_score((trend + value + momentum + risk) / 4)

    total =
        trend * WEIGHTS["trend"] +
        value * WEIGHTS["value"] +
        momentum * WEIGHTS["momentum"] +
        risk * WEIGHTS["risk"] +
        capital * WEIGHTS["capital"]

    confidence = min(1.0, (trend + value + momentum + risk) / 400)

    return {
        "trend_score": trend,
        "value_score": value,
        "momentum_score": momentum,
        "risk_score": risk,
        "capital_score": capital,
        "total_score": round(total, 2),
        "confidence": round(confidence, 2)
    }
