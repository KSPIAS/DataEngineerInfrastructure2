import requests
import os
import logging

logger = logging.getLogger(__name__)

def notify_telegram(message: str):
    token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    if not token or not chat_id:
        logger.warning("❗️Telegram token/chat_id ยังไม่ถูกตั้งค่าใน .env")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logger.info("✅ ส่งข้อความ Telegram สำเร็จ")
    except Exception as e:
        logger.exception(f"❌ ส่งข้อความ Telegram ไม่สำเร็จ: {e}")
