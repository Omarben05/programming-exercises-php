import sqlite3
conn = sqlite3.connect('biblioteca.sqlite')
cur = conn.cursor()

# creare database e tabelle e classi
# le tabelle saranno 5: libri, membri, biblioteca, biblioteca_libro, prestiti
# per ogni tabella: 
# libri(id primary key, nome, autore, editore, biblioteca_id), 
# membri(id primary key, nome, cognome, biblioteca_id), 
# biblioteche(id primary key, nome, sede), 
# prestiti(id primary key, membro_id, libro_id, inizio_prestito, fine_prestito)

query = '''
DROP TABLE libri IF EXISTS'''
table1 = '''
CREATE TABLE IF NOT EXISTS libri (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL, 
    autore TEXT NOT NULL,
    editore TEXT NOT NULL,
    FOREIGN KEY (biblioteca_id) REFERENCES biblioteca(id) ON DELETE CASCADE
    )
'''
query = '''
DROP TABLE membri IF EXISTS'''
table2= '''
CREATE TABLE IF NOT EXISTS membri (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    biblioteca_id INTEGER NOT NULL,
    FOREIGN KEY (biblioteca_id) REFERENCES biblioteca(id) ON DELETE CASCADE
    )
'''
query = '''
DROP TABLE biblioteca IF EXISTS'''
table3 = '''
CREATE TABLE IF NOT EXISTS biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    sede TEXT NOT NULL
)
'''

query = '''
DROP TABLE prestiti IF EXISTS'''
table4 = '''
CREATE TABLE IF NOT EXISTS prestiti(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    membro_id TEXT NOT NULL,
    libro_id INTEGER NOT NULL,
    inizio_prestito DATE NOT NULL,
    fine_prestito DATE NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membri(id) ON DELETE CASCADE,
    FOREIGN KEY (libro_id) REFERENCES libri(id) ON DELETE CASCADE
)
'''
cur.execute(table1)
cur.execute(table2)
cur.execute(table3)
cur.execute(table4)


conn.commit()
