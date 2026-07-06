# score_engine.py

from config import WEIGHTS


def trend_score(ema20, ema50):
    if ema20 > ema50:
        return 80
    elif ema20 < ema50:
        return 40
    return 60


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


def momentum_score(rsi, macd):
    score = 50

    if 40 <= rsi <= 60:
        score += 20
    elif rsi > 70:
        score -= 20
    elif rsi < 30:
        score += 10

    if macd > 0:
        score += 15
    else:
        score -= 10

    return max(0, min(100, score))


def risk_score(atr, bollinger_width):
    score = 100

    if atr:
        score -= atr * 2

    if bollinger_width:
        score -= bollinger_width * 1.5

    return max(0, min(100, score))


def capital_score(avg_score):
    if avg_score > 85:
        return 90
    elif avg_score > 70:
        return 70
    elif avg_score > 55:
        return 40
    return 10


def final_score(inputs):

    trend = trend_score(inputs["ema20"], inputs["ema50"])
    value = value_score(inputs["bubble"])
    momentum = momentum_score(inputs["rsi"], inputs["macd"])
    risk = risk_score(inputs["atr"], inputs["bollinger_width"])

    capital = capital_score((trend + value + momentum + risk) / 4)

    total = (
        trend * WEIGHTS["trend"] +
        value * WEIGHTS["value"] +
        momentum * WEIGHTS["momentum"] +
        risk * WEIGHTS["risk"] +
        capital * WEIGHTS["capital"]
    )

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
