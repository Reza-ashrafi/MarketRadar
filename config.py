BOT_TOKEN = "8961298923:AAFbuiQm0peaGQ4gssD34G0shYeBjk2RaN8"
CHAT_ID = "111954131"


# =========================
# Market Settings
# =========================
UPDATE_INTERVAL_MINUTES = 15

# ساعات فعال بازار نقرابی (ایران)
MARKET_START_HOUR = 12
MARKET_END_HOUR = 17

# =========================
# Weights (مهم‌ترین بخش سیستم)
# =========================
WEIGHTS = {
    "trend": 0.25,
    "value": 0.30,
    "momentum": 0.15,
    "risk": 0.15,
    "capital": 0.10,
    "confidence": 0.05
}

# =========================
# Signal Thresholds
# =========================
SIGNALS = {
    "strong_buy": 85,
    "buy": 70,
    "wait": 55,
    "risk": 40
}

# =========================
# Capital Allocation Rules
# =========================
CAPITAL_RULES = {
    "strong_buy": 0.5,
    "buy": 0.3,
    "wait": 0.1,
    "risk": 0.0
}

# =========================
# Safety
# =========================
MIN_CONFIDENCE_TO_TRADE = 0.65
