import asyncio

from database.subscription import get_earthquake_subscribers
from services.telegram_service import send_earthquake
from database.earthquake import (
    earthquake_exists,
    save_earthquake,
)
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CWA_API_KEY")

URL = (
    "https://opendata.cwa.gov.tw/api/v1/rest/datastore/"
    "E-A0015-001"
)

def fetch_latest_earthquake():
    if not API_KEY:
        raise RuntimeError("CWA_API_KEY 未設定")

    response = requests.get(
        URL,
        params={
            "Authorization": API_KEY,
            "limit": 1,
            "format": "JSON",
        },
        timeout=15,
    )

    print("HTTP:", response.status_code)

    response.raise_for_status()

    data = response.json()

    records = data.get("records", {})
    earthquakes = records.get("Earthquake", [])

    if not earthquakes:
        print("沒有取得地震資料")
        return None

    eq = earthquakes[0]

    print("=" * 40)
    print("編號：", eq["EarthquakeNo"])
    print("時間：", eq["EarthquakeInfo"]["OriginTime"])
    print("位置：", eq["EarthquakeInfo"]["Epicenter"]["Location"])
    print("規模：", eq["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"])
    print("深度：", eq["EarthquakeInfo"]["FocalDepth"])
    print("=" * 40)

    eq_no = eq["EarthquakeNo"]

    print("檢查是否已存在：", eq_no)

    exists = earthquake_exists(eq_no)
    print("exists =", exists)

    if exists:
        print("這筆地震已經存在，略過。")
        return

    print("開始寫入 SQLite...")

    save_earthquake(
        earthquake_no=eq_no,
        origin_time=eq["EarthquakeInfo"]["OriginTime"],
        magnitude=float(
            eq["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"]
        ),
        depth=float(eq["EarthquakeInfo"]["FocalDepth"]),
        location=eq["EarthquakeInfo"]["Epicenter"]["Location"],
    )

    print("已寫入 SQLite。")
    users = get_earthquake_subscribers()

    print(f"準備通知 {len(users)} 位使用者")

    for user in users:
        try:
            asyncio.run(send_earthquake(user, eq))
            print(f"已通知 {user}")
        except Exception as e:
            print(f"{user} 推播失敗：{e}")
            import time


def earthquake_loop():
    while True:
        try:
            fetch_latest_earthquake()
        except Exception as e:
            print(f"[Earthquake Worker] {e}")

        time.sleep(60)

if __name__ == "__main__":
    earthquake_loop()