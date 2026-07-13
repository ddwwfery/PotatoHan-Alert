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

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

init_database()

if not TOKEN:
    raise RuntimeError("BOT_TOKEN 未設定")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback_handler))

print("🚀 PotatoHan Alert v1 啟動成功")

app.run_polling()