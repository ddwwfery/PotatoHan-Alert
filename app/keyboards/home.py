from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def home_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🚨 地震速報", callback_data="earthquake"),
            InlineKeyboardButton("📊 地震分析", callback_data="analysis"),
        ],
        [
            InlineKeyboardButton("🌧 天氣通知", callback_data="weather"),
            InlineKeyboardButton("⚙️ 我的訂閱", callback_data="settings"),
        ],
        [
            InlineKeyboardButton("🌐 官方網站", url="https://alert.potatohan.com"),
        ],
        [
            InlineKeyboardButton("❓ 使用說明", callback_data="help"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
