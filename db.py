import sqlite3

def init_db():
    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        change REAL,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()
