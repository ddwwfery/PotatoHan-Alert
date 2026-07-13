from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.home import home_keyboard
from services.subscription_service import (
    set_earthquake_level,
    get_subscription
)


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # ========================
    # 回首頁
    # ========================
    if query.data == "home":

        await query.edit_message_text(
            "👋 歡迎使用 PotatoHan Alert\n\n"
            "🇹🇼 台灣災害即時通知系統\n\n"
            "請選擇下方功能👇",
            reply_markup=home_keyboard()
        )

    # ========================
    # 地震速報
    # ========================
    elif query.data == "earthquake":

        keyboard = [
            [
                InlineKeyboardButton("🌍 全部地震", callback_data="eq_all")
            ],
            [
                InlineKeyboardButton("🟢 3級以上", callback_data="eq3"),
                InlineKeyboardButton("🟠 4級以上", callback_data="eq4"),
            ],
            [
                InlineKeyboardButton("🔴 5級以上", callback_data="eq5"),
            ],
            [
                InlineKeyboardButton("⬅ 返回首頁", callback_data="home"),
            ],
        ]

        await query.edit_message_text(
            "🚨 地震速報\n\n"
            "請選擇通知門檻",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # ========================
    # 地震通知等級
    # ========================
    elif query.data == "eq_all":

        set_earthquake_level(query.from_user.id, 0)

        await query.answer(
            "✅ 已儲存：全部地震",
            show_alert=True,
        )

    elif query.data == "eq3":

        set_earthquake_level(query.from_user.id, 3)

        await query.answer(
            "✅ 已儲存：3級以上通知",
            show_alert=True,
        )

    elif query.data == "eq4":

        set_earthquake_level(query.from_user.id, 4)

        await query.answer(
            "✅ 已儲存：4級以上通知",
            show_alert=True,
        )

    elif query.data == "eq5":

        set_earthquake_level(query.from_user.id, 5)

        await query.answer(
            "✅ 已儲存：5級以上通知",
            show_alert=True,
        )
    # ========================
    # 地震分析
    # ========================
    elif query.data == "analysis":

        keyboard = [
            [
                InlineKeyboardButton("📅 最近24小時", callback_data="analysis24")
            ],
            [
                InlineKeyboardButton("📆 最近7天", callback_data="analysis7")
            ],
            [
                InlineKeyboardButton("📈 地震統計", callback_data="analysis_stat")
            ],
            [
                InlineKeyboardButton("⬅ 返回首頁", callback_data="home")
            ],
        ]

        await query.edit_message_text(
            "📊 地震分析\n\n"
            "請選擇查詢項目",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data in ["analysis24", "analysis7", "analysis_stat"]:

        await query.answer(
            "🚧 地震分析功能開發中",
            show_alert=True,
        )

    # ========================
    # 天氣通知
    # ========================
    elif query.data == "weather":

        keyboard = [
            [
                InlineKeyboardButton("🌧 豪雨", callback_data="rain")
            ],
            [
                InlineKeyboardButton("🌀 颱風", callback_data="typhoon")
            ],
            [
                InlineKeyboardButton("⚡ 雷雨", callback_data="storm")
            ],
            [
                InlineKeyboardButton("🔥 高溫", callback_data="hot")
            ],
            [
                InlineKeyboardButton("⬅ 返回首頁", callback_data="home")
            ],
        ]

        await query.edit_message_text(
            "🌤 天氣通知\n\n"
            "請選擇通知項目",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data in ["rain", "typhoon", "storm", "hot"]:

        await query.answer(
            "🚧 天氣通知功能開發中",
            show_alert=True,
        )

    # ========================
    # 我的訂閱
    # ========================
    elif query.data == "settings":

        sub = get_subscription(query.from_user.id)

        if sub:

            level = sub["earthquake_level"]

            if level == 0:
                level_text = "🌍 全部地震"
            elif level == 3:
                level_text = "🟢 3級以上"
            elif level == 4:
                level_text = "🟠 4級以上"
            elif level == 5:
                level_text = "🔴 5級以上"
            else:
                level_text = "未設定"

            weather = "✅ 開啟" if sub["weather_enable"] else "❌ 關閉"

        else:

            level_text = "未設定"
            weather = "未設定"

        keyboard = [
            [
                InlineKeyboardButton(
                    "⬅ 返回首頁",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            f"⚙️ 我的訂閱\n\n"
            f"🚨 地震速報：{level_text}\n"
            f"🌤 天氣通知：{weather}\n"
            f"📧 Email：未綁定",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    # ========================
    # 使用說明
    # ========================
    elif query.data == "help":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⬅ 返回首頁",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            "📖 PotatoHan Alert\n\n"
            "Version 1.2 Alpha\n\n"
            "目前功能：\n"
            "✅ 地震速報訂閱\n"
            "🚧 地震分析\n"
            "🚧 天氣通知\n"
            "🚧 Email 綁定\n\n"
            "© 2026 PotatoHan™ — 馬鈴薯飯\n"
            "All Rights Reserved.\n"
            "📧 contact@potatohan.com",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # ========================
    # 未知按鈕
    # ========================
    else:

        await query.answer(
            "⚠️ 未知功能",
            show_alert=True,
        )
