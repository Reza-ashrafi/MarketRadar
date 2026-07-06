# signal_engine.py

from config import SIGNALS, CAPITAL_RULES, MIN_CONFIDENCE_TO_TRADE


# =========================
# SIGNAL CLASSIFIER
# =========================
def classify_signal(score):
    if score >= SIGNALS["strong_buy"]:
        return "STRONG_BUY"
    elif score >= SIGNALS["buy"]:
        return "BUY"
    elif score >= SIGNALS["wait"]:
        return "WAIT"
    elif score >= SIGNALS["risk"]:
        return "RISK"
    else:
        return "NO_TRADE"


# =========================
# CAPITAL ALLOCATION
# =========================
def capital_allocation(signal):
    return CAPITAL_RULES.get(signal.lower(), 0)


# =========================
# FINAL DECISION ENGINE
# =========================
def generate_signal(score_data):
    """
    score_data:
    {
        total_score,
        confidence
    }
    """

    total = score_data["total_score"]
    confidence = score_data["confidence"]

    signal = classify_signal(total)

    capital = 0

    # 🚫 فیلتر اعتماد
    if confidence < MIN_CONFIDENCE_TO_TRADE:
        return {
            "signal": "NO_TRADE",
            "capital": 0,
            "reason": "Low confidence"
        }

    # 🚦 تخصیص سرمایه
    if signal == "STRONG_BUY":
        capital = CAPITAL_RULES["strong_buy"]
    elif signal == "BUY":
        capital = CAPITAL_RULES["buy"]
    elif signal == "WAIT":
        capital = CAPITAL_RULES["wait"]
    elif signal == "RISK":
        capital = CAPITAL_RULES["risk"]
    else:
        capital = 0

    return {
        "signal": signal,
        "capital": capital,
        "confidence": confidence,
        "score": total
    }
