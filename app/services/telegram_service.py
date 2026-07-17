from os import getenv

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

bot = Bot(token=getenv("BOT_TOKEN"))


async def send_earthquake(chat_id, eq):
    info = eq["EarthquakeInfo"]

    message = f"""🚨 地震速報

📍 {info["Epicenter"]["Location"]}

🌍 規模：M {info["EarthquakeMagnitude"]["MagnitudeValue"]}
📏 深度：{info["FocalDepth"]} km
🕒 {info["OriginTime"]}

#中央氣象署"""

    await bot.send_message(
        chat_id=chat_id,
        text=message,
    )