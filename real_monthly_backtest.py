# monthly_backtest.py

from analyzer import analyze


def load_data():

    prices = [
        100, 101, 99, 98, 100, 102, 103, 104, 103, 105,
        107, 106, 108, 110, 111, 109, 112, 113, 115, 114,
        116, 118, 117, 119, 120, 121, 119, 118, 122, 123
    ]

    return prices


def run():

    prices = load_data()

    position = 0
    entry = 0
    trades = []
    equity = 100

    for i in range(20, len(prices)):

        window = prices[i-20:i]

        data = {
            "prices": window,
            "highs": [p * 1.01 for p in window],
            "lows": [p * 0.99 for p in window],
            "closes": window,
            "bubble": (window[-1] - window[0]) / window[0] * 100
        }

        result = analyze(data)
        signal = result["signal"]

        price = prices[i]

        # =========================
        # ENTRY
        # =========================
        if signal in ["BUY", "STRONG_BUY"] and position == 0:
            position = 1
            entry = price
            print(f"BUY @ {price}")

        # =========================
        # EXIT
        # =========================
        elif signal in ["RISK", "NO_TRADE"] and position == 1:

            profit = ((price - entry) / entry) * 100
            equity += equity * (profit / 100)

            trades.append(profit)

            print(f"SELL @ {price} | PnL: {profit:.2f}%")

            position = 0

    # =========================
    # REPORT
    # =========================
    print("\n📊 BACKTEST REPORT")
    print("------------------------")
    print("Trades:", len(trades))

    if trades:
        win = len([t for t in trades if t > 0])
        print("Win Rate:", win / len(trades) * 100)
        print("Avg Profit:", sum(trades) / len(trades))
    else:
        print("Win Rate: 0")
        print("Avg Profit: 0")

    print("Final Equity:", equity)


if __name__ == "__main__":
    run()
