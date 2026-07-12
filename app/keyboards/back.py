from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def back_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("⬅ 返回首頁", callback_data="home")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
