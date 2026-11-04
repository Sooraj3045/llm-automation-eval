
import sqlite3


DATABASE_NAME = "chatbot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_chat(user_message, bot_response):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO chat_history (user_message, bot_response)
        VALUES (?, ?)
        """,
        (user_message, bot_response)
    )

    connection.commit()
    connection.close()


def get_all_chats():
    connection = get_connection()

    records = connection.execute(
        "SELECT * FROM chat_history ORDER BY id"
    ).fetchall()

    connection.close()

    return [dict(record) for record in records]
