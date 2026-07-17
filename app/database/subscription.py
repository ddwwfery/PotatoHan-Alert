from database.database import get_connection


def get_earthquake_subscribers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT telegram_id
        FROM subscriptions
        WHERE earthquake_enabled = 1
    """)

    users = [row[0] for row in cur.fetchall()]

    conn.close()

    return users