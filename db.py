import sqlite3

def init_db():
    # Create/connect database
    conn = sqlite3.connect('crypto.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                change REAL,
                timestamp TEXT
            )
        ''')
    return conn  # Return connection so other scripts can use it
