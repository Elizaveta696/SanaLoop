import sqlite3
import os

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/words.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS translations (
              finnish TEXT PPRIMARY KEY,
              english TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_translation(finnish, english):
    print(f"Saving to DB: {finnish}")
    conn = sqlite3.connect('data/words.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO translations (finnish, english) VALUES (?, ?)", (finnish, english))
    conn.commit()
    conn.close()

def get_all_translations():
    conn = sqlite3.connect('data/words.db')
    c = conn.cursor()
    c.execute("SELECT finnish, english FROM translations")
    rows = c.fetchall()
    conn.close()
    return rows

def is_translated(word):
    conn = sqlite3.connect('data/words.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM translations WHERE finnish=?", (word,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

