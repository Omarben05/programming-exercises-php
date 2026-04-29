import sqlite3
conn = sqlite3.connect('biblioteca.sqlite')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS prestiti')
cur.execute('DROP TABLE IF EXISTS membri')
cur.execute('DROP TABLE IF EXISTS libri')
cur.execute('DROP TABLE IF EXISTS biblioteca')


cur.execute('''
CREATE TABLE IF NOT EXISTS biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    sede TEXT NOT NULL
)
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS libri (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL, 
    autore TEXT NOT NULL,
    editore TEXT NOT NULL,
    biblioteca_id INTEGER NOT NULL,
    FOREIGN KEY (biblioteca_id) REFERENCES biblioteca(id) ON DELETE CASCADE
)
''')

cur.execute(''' 
CREATE TABLE IF NOT EXISTS membri (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    biblioteca_id INTEGER NOT NULL,
    FOREIGN KEY (biblioteca_id) REFERENCES biblioteca(id) ON DELETE CASCADE
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS prestiti(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    membro_id INTEGER NOT NULL,
    libro_id INTEGER NOT NULL,
    inizio_prestito DATE NOT NULL,
    fine_prestito DATE NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membri(id) ON DELETE CASCADE,
    FOREIGN KEY (libro_id) REFERENCES libri(id) ON DELETE CASCADE
)
''')

conn.commit()
conn.close()
