print("BOT STARTED")

from telegram_sender import send_report

try:
    send_report()
    print("MESSAGE SENT")
except Exception as e:
    print("ERROR:", e)

print("BOT DONE")
