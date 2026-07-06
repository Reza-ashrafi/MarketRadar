from telegram import Bot
from config import BOT_TOKEN, CHAT_ID
from analyzer import analyze

bot = Bot(token=BOT_TOKEN)


def build_message(data):

    if "error" in data:
        return "❌ داده‌ها در دسترس نیست"

    return f"""
📊 گزارش نقره

🌍 قیمت جهانی: {data['silver']:.2f} $
💵 دلار: {int(data['usd']):,} تومان

📦 ارزش ذاتی: {int(data['intrinsic']):,}
🏪 قیمت فرضی بازار: {int(data['market']):,}

📈 حباب: {data['bubble']:.2f}%

{data['signal']}
"""


def send_report():
    data = analyze()
    msg = build_message(data)
    bot.send_message(chat_id=CHAT_ID, text=msg)
