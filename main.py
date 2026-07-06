# main.py

import time
from datetime import datetime

from data_provider import get_market_data
from analyzer import analyze
from telegram_sender import send_report

# =========================
# CHECK MARKET HOURS
# =========================
def is_market_open():
    hour = datetime.now().hour
    return 12 <= hour <= 17


def is_market_open():
    return True
# =========================
# RUN BOT
# =========================
def run_bot():

    print("SilverMind Pro - LIVE MODE Started...")

    last_signal = None

    while True:

        try:

            if not is_market_open():
                print("Market Closed...")
                time.sleep(300)
                continue

            # =========================
            # REAL DATA
            # =========================
            market_data = get_market_data()

            if market_data is None:
                print("No market data available")
                time.sleep(300)
                continue

            # =========================
            # ANALYSIS
            # =========================
            result = analyze(market_data)

            if not result:
                print("No signal generated")
                time.sleep(300)
                continue

            signal = result["signal"]

            # =========================
            # FILTER (جلوگیری از اسپم)
            # =========================
            if signal != last_signal:
                send_report(result)
                last_signal = signal
                print("📡 Sent:", signal)
            else:
                print("No change:", signal)

            time.sleep(300)  # هر 5 دقیقه

        except Exception as e:
            print("ERROR:", e)
            time.sleep(60)


# =========================
# START
# =========================
if __name__ == "__main__":
    run_bot()
