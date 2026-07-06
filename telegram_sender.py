# telegram_sender.py

import requests
from config import BOT_TOKEN, CHAT_ID


# =========================
# SEND MESSAGE TO TELEGRAM
# =========================
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print("Telegram Error:", e)


# =========================
# FORMAT REPORT
# =========================
def format_report(result):
    scores = result["scores"]
    indicators = result["indicators"]

    signal = result["signal"]
    capital = int(result["capital"] * 100)
    confidence = int(result["confidence"] * 100)

    text = f"""
📊 *SilverMind Pro Report*

━━━━━━━━━━━━━━━

📈 Score: *{scores['total_score']} / 100*
🎯 Confidence: *{confidence}%*

🚦 Signal: *{signal}*
💰 Capital: *{capital}%*

━━━━━━━━━━━━━━━

📊 Indicators:

EMA20: {indicators['ema20']:.2f}
EMA50: {indicators['ema50']:.2f}

RSI: {indicators['rsi']:.2f}
MACD: {indicators['macd']:.2f}

Momentum: {indicators['momentum']:.2f}
ATR: {indicators['atr']:.2f}

━━━━━━━━━━━━━━━

🧠 Entry Status:
{result['entry_text']}

━━━━━━━━━━━━━━━
"""

    return text


# =========================
# MAIN FUNCTION
# =========================
def send_report(result):
    if not result:
        return

    message = format_report(result)
    send_message(message)
