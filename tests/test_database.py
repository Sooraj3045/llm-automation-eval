
import sqlite3

from database import (
    create_table,
    save_chat,
    get_all_chats
)


def test_database_connection():
    connection = sqlite3.connect(":memory:")

    assert connection is not None

    connection.close()


def test_chat_table_creation():
    connection = sqlite3.connect(":memory:")

    connection.execute("""
        CREATE TABLE chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL
        )
    """)

    result = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchone()

    assert result[0] == "chat_history"

    connection.close()


def test_save_and_retrieve_chat():
    # Ensure the table exists before inserting data
    create_table()

    save_chat(
        "My order is late",
        "You are eligible for a refund."
    )

    records = get_all_chats()

    assert len(records) > 0
    assert records[-1]["user_message"] == "My order is late"
    assert "refund" in records[-1]["bot_response"].lower()
