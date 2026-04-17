import sqlite3

conn = sqlite3.connect("game.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    coins INTEGER DEFAULT 100,
    xp INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS clans (
    name TEXT PRIMARY KEY,
    owner INTEGER,
    power INTEGER DEFAULT 1000
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS map_tiles (
    x INTEGER,
    y INTEGER,
    owner TEXT
)
""")

conn.commit()
