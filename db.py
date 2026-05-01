import sqlite3

def get_connection():
    conn = sqlite3.connect("site.db")
    conn.row_factory = sqlite3.Row  # THIS replaces dictionary=True
    return conn

