from analyzer import analyze
from datetime import datetime, timedelta


def run():

    # 📊 داده نمونه نزدیک به بازار (می‌تونی بعداً واقعی‌ترش کنیم)
    prices = [
        100, 101, 99, 98, 100, 102, 103, 104, 103, 105,
        107, 106, 108, 110, 111, 109, 112, 113, 115, 114,
        116, 118, 117, 119, 120, 121, 119, 118, 122, 123
    ]

    # 📅 شروع تاریخ (مثلاً 8 تیر)
    start_date = datetime(2025, 6, 29)

    position = 0
    entry_price = 0
    trades = []
    equity = 100

    print("\n📊 SILVERMIND PRO - REAL BACKTEST")
    print("━━━━━━━━━━━━━━━━━━━━━━")

    for i in range(20, len(prices)):

        date = start_date + timedelta(days=i - 20)

        window = prices[i-20:i]

        data = {
            "prices": window,
            "highs": [p * 1.01 for p in window],
            "lows": [p * 0.99 for p in window],
            "closes": window,
            "bubble": (window[-1] - window[0]) / window[0] * 100
        }

        result = analyze(data)

        score = result["scores"]["total_score"]
        signal = result["signal"]
        confidence = result["confidence"]

        price = prices[i]

        # =========================
        # ENTRY
        # =========================
        if signal in ["BUY", "STRONG_BUY"] and position == 0:
            position = 1
            entry_price = price

            print(f"""
📅 {date.strftime('%Y-%m-%d')} (≈ {date.day} تیر)
💰 BUY @ {price}
📊 Score: {score}
🎯 Confidence: {confidence}
━━━━━━━━━━━━━━━
""")

        # =========================
        # EXIT
        # =========================
        elif signal in ["RISK", "NO_TRADE"] and position == 1:

            profit = ((price - entry_price) / entry_price) * 100
            equity += equity * (profit / 100)

            trades.append(profit)

            print(f"""
📅 {date.strftime('%Y-%m-%d')} (≈ {date.day} تیر)
💰 SELL @ {price}
📊 PnL: {profit:.2f}%
💰 Equity: {equity:.2f}
━━━━━━━━━━━━━━━
""")

            position = 0

    # =========================
    # FINAL REPORT
    # =========================

    print("\n📊 FINAL REPORT")
    print("━━━━━━━━━━━━━━━━━━━━━━")

    if trades:
        win_rate = len([t for t in trades if t > 0]) / len(trades) * 100
        avg_profit = sum(trades) / len(trades)
    else:
        win_rate = 0
        avg_profit = 0

    print(f"Trades: {len(trades)}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Avg Profit: {avg_profit:.2f}%")
    print(f"Final Equity: {equity:.2f}")

    print("━━━━━━━━━━━━━━━━━━━━━━")


if __name__ == "__main__":
    run()
