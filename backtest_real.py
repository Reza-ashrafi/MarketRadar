# real_backtest.py

from analyzer import analyze
from data_provider import get_historical_data_mock_real


def run():

    prices = get_historical_data_mock_real()

    position = 0
    entry = 0
    trades = []
    equity = 100

    for i in range(20, len(prices)):

        window = prices[i-20:i]

        data = {
            "prices": window,
            "highs": [p * 1.01 for p in window],
            "lows": [p * 1.01 for p in window],
            "closes": window,
            "bubble": (window[-1] - window[0]) / window[0] * 100
        }

        result = analyze(data)
        signal = result["signal"]

        price = prices[i]

        if signal in ["BUY", "STRONG_BUY"] and position == 0:
            position = 1
            entry = price
            print(f"BUY @ {price}")

        elif signal in ["RISK", "NO_TRADE"] and position == 1:

            profit = ((price - entry) / entry) * 100
            equity += equity * (profit / 100)

            trades.append(profit)

            print(f"SELL @ {price} | PnL: {profit:.2f}%")

            position = 0

    print("\n📊 REAL BACKTEST REPORT")
    print("------------------------")

    if trades:
        win = len([t for t in trades if t > 0]) / len(trades) * 100
        avg = sum(trades) / len(trades)
    else:
        win = avg = 0

    print("Trades:", len(trades))
    print("Win Rate:", win)
    print("Avg Profit:", avg)
    print("Final Equity:", equity)


if __name__ == "__main__":
    run()
