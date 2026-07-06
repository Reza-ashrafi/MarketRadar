import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID
from analyzer import analyze

bot = Bot(token=BOT_TOKEN)


def build_message(data):
    return f"""
📊 گزارش نقره

🌍 قیمت جهانی: {data.get('silver', 0):.2f} $
💵 دلار: {int(data.get('usd', 0)):,}

📦 ارزش ذاتی: {int(data.get('intrinsic', 0)):,}
🏪 بازار: {int(data.get('market', 0)):,}

📈 حباب: {data.get('bubble', 0):.2f}%
⭐ امتیاز: {data.get('score', 0):.0f}/100

{data.get('decision', 'بدون تحلیل')}
"""


async def send_async():
    data = analyze()
    msg = build_message(data)
    await bot.send_message(chat_id=CHAT_ID, text=msg)


def send_report():
    asyncio.run(send_async())
