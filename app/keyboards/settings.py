from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def settings_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✏ 修改地震通知",
                    callback_data="earthquake"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅ 返回首頁",
                    callback_data="home"
                )
            ]
        ]
    )