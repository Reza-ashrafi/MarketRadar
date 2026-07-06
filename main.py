import time
from telegram_bot import send_report


def run():
    while True:
        try:
            send_report()
            print("sent")

        except Exception as e:
            print("error:", e)

        time.sleep(86400)  # 24h


if __name__ == "__main__":
    run()
