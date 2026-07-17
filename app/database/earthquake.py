from database.database import get_connection


def earthquake_exists(earthquake_no: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT 1 FROM earthquake_history WHERE earthquake_no = ?",
        (earthquake_no,),
    )

    exists = cur.fetchone() is not None

    conn.close()

    return exists


def save_earthquake(
    earthquake_no,
    origin_time,
    magnitude,
    depth,
    location,
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO earthquake_history
        (
            earthquake_no,
            origin_time,
            magnitude,
            depth,
            location
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            earthquake_no,
            origin_time,
            magnitude,
            depth,
            location,
        ),
    )

    conn.commit()
    conn.close()