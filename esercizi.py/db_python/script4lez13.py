import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
  print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()



cur.execute('''CREATE TABLE IF NOT EXISTS Artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    title TEXT UNIQUE,
    FOREIGN KEY (artist_id) REFERENCES Artists(id)
)
''')

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