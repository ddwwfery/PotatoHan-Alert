from database.database import get_connection


def set_earthquake_level(telegram_id: int, level: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO subscriptions
    (
        telegram_id,
        earthquake_enable,
        earthquake_level
    )
    VALUES(?,?,?)
    ON CONFLICT(telegram_id)
    DO UPDATE SET

        earthquake_enable=1,

        earthquake_level=excluded.earthquake_level
    """,
    (
        telegram_id,
        1,
        level
    ))

    conn.commit()
    conn.close()


def get_earthquake_level(telegram_id: int):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    SELECT earthquake_level

    FROM subscriptions

    WHERE telegram_id=?

    """,(telegram_id,))

    row=cur.fetchone()

    conn.close()

    if row:

        return row["earthquake_level"]

    return 0
def get_subscription(telegram_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM subscriptions
        WHERE telegram_id = ?
    """, (telegram_id,))

    row = cur.fetchone()
    conn.close()

    return row
