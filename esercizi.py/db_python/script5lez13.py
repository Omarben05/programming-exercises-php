import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()



cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('''CREATE TABLE IF NOT EXISTS Artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE)''')

cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('''
CREATE TABLE IF NOT EXISTS Albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    title TEXT UNIQUE,
    FOREIGN KEY (artist_id) REFERENCES Artists(id)
)
''')

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('''
CREATE TABLE IF NOT EXISTS Tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_id INTEGER,
    title TEXT UNIQUE,
    plays INTEGER,
    FOREIGN KEY (album_id) REFERENCES Albums(id)
)
''')

cur.close()