# indicators.py

import statistics


# =========================
# EMA (Exponential Moving Average)
# =========================
def ema(prices, period):
    if len(prices) < period:
        return sum(prices) / len(prices)

    k = 2 / (period + 1)
    ema_value = prices[0]

    for price in prices[1:]:
        ema_value = price * k + ema_value * (1 - k)

    return ema_value


# =========================
# RSI (Relative Strength Index)
# =========================
def rsi(prices, period=14):
    if len(prices) < period + 1:
        return 50

    gains = []
    losses = []

    for i in range(1, period + 1):
        diff = prices[i] - prices[i - 1]
        if diff >= 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(diff))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


# =========================
# MACD
# =========================
def macd(prices):
    ema12 = ema(prices, 12)
    ema26 = ema(prices, 26)
    return ema12 - ema26


# =========================
# Momentum
# =========================
def momentum(prices, period=10):
    if len(prices) < period:
        return 0

    return prices[-1] - prices[-period]


# =========================
# ATR (نوسان)
# =========================
def atr(highs, lows, closes, period=14):
    if len(closes) < period:
        return 0

    trs = []

    for i in range(1, len(closes)):
        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1])
        )
        trs.append(tr)

    return sum(trs[-period:]) / period


# =========================
# Bollinger Band Width
# =========================
def bollinger_width(prices, period=20):
    if len(prices) < period:
        return 0

    mean = sum(prices[-period:]) / period
    std = statistics.stdev(prices[-period:])

    upper = mean + 2 * std
    lower = mean - 2 * std

    return upper - lower
