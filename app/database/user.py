from database.database import get_connection


def add_user(user):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO users
        (
            telegram_id,
            username,
            first_name,
            language
        )
        VALUES (?, ?, ?, ?)
    """, (
        user.id,
        user.username,
        user.first_name,
        user.language_code
    ))

    cur.execute("""
        UPDATE users
        SET
            username = ?,
            first_name = ?,
            language = ?,
            last_seen = CURRENT_TIMESTAMP
        WHERE telegram_id = ?
    """, (
        user.username,
        user.first_name,
        user.language_code,
        user.id
    ))

    conn.commit()
    conn.close()
