# backtest_real.py

import pandas as pd
from analyzer import analyze


# =========================
# LOAD REAL DATA
# =========================
def load_data(path="data.csv"):
    df = pd.read_csv(path)

    prices = df["price"].tolist()

    return prices


# =========================
# BUILD WINDOW DATA
# =========================
def build_window(prices, idx, window=30):

    window_prices = prices[idx-window:idx]

    return {
        "prices": window_prices,
        "highs": [p * 1.01 for p in window_prices],
        "lows": [p * 0.99 for p in window_prices],
        "closes": window_prices,
        "bubble": 0  # اگر NAV داری اینجا واقعی می‌کنی
    }


# =========================
# BACKTEST ENGINE
# =========================
def run_backtest():

    prices = load_data()

    if len(prices) < 40:
        print("❌ Not enough data")
        return

    results = []

    buy_signals = 0
    sell_signals = 0
    no_trade = 0

    for i in range(30, len(prices)):

        data = build_window(prices, i)

        result = analyze(data)

        signal = result["signal"]
        score = result["scores"]["total_score"]

        results.append({
            "index": i,
            "price": prices[i],
            "signal": signal,
            "score": score
        })

        if signal in ["BUY", "STRONG_BUY"]:
            buy_signals += 1
        elif signal in ["RISK"]:
            sell_signals += 1
        else:
            no_trade += 1

    # =========================
    # REPORT
    # =========================
    print("\n📊 REAL BACKTEST REPORT")
    print("---------------------------")
    print("Total Days:", len(results))
    print("BUY:", buy_signals)
    print("RISK/SELL:", sell_signals)
    print("NO TRADE:", no_trade)

    # میانگین امتیاز سیگنال‌ها
    avg_score = sum(r["score"] for r in results) / len(results)

    print("---------------------------")
    print("Avg Score:", round(avg_score, 2))
