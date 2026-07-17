import sqlite3
import os

DB_PATH = "/database/potatohan.db"


def get_connection():
    os.makedirs("/database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def init_database():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(

        telegram_id INTEGER PRIMARY KEY,

        username TEXT,

        first_name TEXT,

        language TEXT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        last_seen TEXT DEFAULT CURRENT_TIMESTAMP

    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions(

        telegram_id INTEGER PRIMARY KEY,

        earthquake_enable INTEGER DEFAULT 1,

        earthquake_level INTEGER DEFAULT 0,

        earthquake_analysis INTEGER DEFAULT 0,

        weather_enable INTEGER DEFAULT 1,

        email TEXT,

        FOREIGN KEY(telegram_id)
        REFERENCES users(telegram_id)

    )
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS earthquake_history (
    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
    
        earthquake_no TEXT UNIQUE,
    
        origin_time TEXT,
    
        magnitude REAL,
    
        depth REAL,
    
        location TEXT,
    
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    
    """)

    conn.commit()
    conn.close()
