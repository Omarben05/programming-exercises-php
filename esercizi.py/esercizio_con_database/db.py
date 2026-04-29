import sqlite3

conn = sqlite3.connect('sondaggio.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS surveys')

query = '''
    CREATE TABLE IF NOT EXISTS surveys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        height FLOAT,
        marriage INTEGER,
        subjects TEXT
    );
'''

cur.execute(query)

conn.close()