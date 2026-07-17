import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from handlers.start import start
from handlers.callback import callback_handler
from database.database import init_database
from workers.earthquake_worker import fetch_latest_earthquake

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

init_database()

if not TOKEN:
    raise RuntimeError("BOT_TOKEN 未設定")


async def earthquake_job(context):
    try:
        fetch_latest_earthquake()
    except Exception as e:
        print(f"[Earthquake Worker] {e}")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback_handler))

# 每 60 秒執行一次，第一次啟動 5 秒後開始
app.job_queue.run_repeating(
    earthquake_job,
    interval=60,
    first=5,
)

print("🚀 PotatoHan Alert v1 啟動成功")

app.run_polling()