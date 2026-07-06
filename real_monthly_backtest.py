# real_monthly_backtest.py

from analyzer import analyze
from data_provider import get_historical_data_mock_real


def run():

    prices = get_historical_data_mock_real()

    data_set = []

    for i in range(20, len(prices)):

        window = prices[i-20:i]

        data_set.append({
            "prices": window,
            "highs": [p * 1.01 for p in window],
            "lows": [p * 0.99 for p in window],
            "closes": window,
            "bubble": (window[-1] - window[0]) / window[0] * 100
        })

    position = 0
    entry = 0
    trades = []
    equity = 100

    for i, data in enumerate(data_set):

        result = analyze(data)
        signal = result["signal"]

        price = prices[i + 20]

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

    print("\n📊 REAL MARKET BACKTEST")
    print("------------------------")
    print("Trades:", len(trades))
    print("Win Rate:", len([t for t in trades if t > 0]) / len(trades) * 100 if trades else 0)
    print("Avg Profit:", sum(trades) / len(trades) if trades else 0)
    print("Final Equity:", equity)
