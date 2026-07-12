from telegram import Update
from telegram.ext import ContextTypes

from keyboards.home import home_keyboard
from database.user import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # 自動建立/更新使用者
    add_user(update.effective_user)

    await update.message.reply_text(
        "👋 歡迎使用 PotatoHan Alert\n\n"
        "🇹🇼 台灣災害即時通知系統\n\n"
        "目前可訂閱：\n"
        "🚨 地震速報\n"
        "📊 地震分析\n"
        "🌧️ 天氣通知\n\n"
        "請選擇下方功能👇",
        reply_markup=home_keyboard()
    )
