import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    food_item TEXT,
    quantity TEXT,
    location TEXT
)
""")

conn.commit()
conn.close()

print("Database created")
