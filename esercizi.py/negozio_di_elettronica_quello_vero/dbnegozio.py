import sqlite3

conn = sqlite3.connect('negozio.sqlite')
db = conn.cursor()

query = '''
DROP TABLE IF EXISTS prodotti'''
db.execute(query)
table1 = '''
CREATE TABLE IF NOT EXISTS prodotti (
    codProdotto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    prezzo TEXT NOT NULL, 
    nome TEXT NOT NULL,
    quantita INTEGER NOT NULL,
    codCliente INTEGER,
    codNegozio INTEGER,
    FOREIGN KEY (codCliente) REFERENCES clienti(cf),
    FOREIGN KEY (codNegozio) REFERENCES negozio(codNegozio)
    )
'''

query = '''
DROP TABLE IF EXISTS clienti'''
db.execute(query)
table2= '''
CREATE TABLE IF NOT EXISTS clienti (
    cf TEXT PRIMARY KEY  NOT NULL,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    citta TEXT NOT NULL
    )
'''

query = '''
DROP TABLE IF EXISTS negozio'''
db.execute(query)
table3 = '''
CREATE TABLE IF NOT EXISTS negozio (
    codNegozio INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    citta TEXT NOT NULL
)
'''

query = '''
DROP TABLE IF EXISTS acquisti '''
db.execute(query)
table4 = '''
CREATE TABLE IF NOT EXISTS acquisti(
    cf INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    codice_prodotto TEXT NOT NULL,
    quantita INT NOT NULL,
    citta TEXT NOT NULL
)'''

db.execute(table1)
db.execute(table2)
db.execute(table3)
db.execute(table4)

conn.commit()
conn.close()
