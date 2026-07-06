def analyze():
    silver = 28.5
    usd = 60000

    intrinsic = silver * usd
    market = 56_000_000

    bubble = ((market - intrinsic) / intrinsic) * 100
    score = 100 - abs(bubble) * 2

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    decision = "🟢 خوب" if bubble < 5 else "🟡 متوسط" if bubble < 15 else "🔴 پرریسک"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }
