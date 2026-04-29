## Creazione tabelle


import sqlite3
conn = sqlite3.connect('sistema_prenotazioni.sqlite')
cur = conn.cursor()

# query = '''
# DROP TABLE IF EXISTS viaggi'''  
# cur.execute(query)
Voyages = '''
CREATE TABLE IF NOT EXISTS voli (
    idvolo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    partenza TEXT NOT NULL,
    destinazione TEXT NOT NULL,
    data TEXT NOT NULL,
    ora TEXT NOT NULL,
    prezzo INTEGER NOT NULL
    )
'''

# query = '''
# DROP TABLE IF EXISTS passeggeri''' 
# cur.execute(query)
Passengers = '''
CREATE TABLE IF NOT EXISTS passeggeri (
    idpasseggero integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL
    )
'''

# query = ''''' 
# DROP TABLE IF EXISTS auto_noleggi'''
# cur.execute(query)
CarRental = '''
CREATE TABLE IF NOT EXISTS autonoleggi (
    idauto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    marca TEXT NOT NULL,
    modello TEXT NOT NULL
)
'''

# query = '''
# DROP TABLE IF EXISTS hotels'''
# cur.execute(query)
Hotels = '''
CREATE TABLE IF NOT EXISTS hotels (
    idhotel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    citta TEXT NOT NULL,
    stelle  INTEGER NOT NULL,
    prezzo INTEGER NOT NULL
    )
'''

# query = '''
# DROP TABLE IF EXISTS prenotazioni_voli'''
# cur.execute(query)      
FlightReservations = '''
CREATE TABLE IF NOT EXISTS prenotazioni_voli (
    idprenotazionevoli INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_volo INTEGER NOT NULL,
    id_passeggero TEXT NOT NULL,
    FOREIGN KEY (id_volo) REFERENCES voli(idvolo),
    FOREIGN KEY (id_passeggero) REFERENCES passeggeri(idpasseggero)
    )
'''

# query = ''''
# DROP TABLE IF EXISTS prenotazioni_autonoleggi'''
# cur.execute(query)
CarRentalReservations = '''
CREATE TABLE IF NOT EXISTS prenotazioni_autonoleggi (
    idprenotazioneautonoleggi INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_auto INTEGER NOT NULL,
    id_passeggero TEXT NOT NULL,
    FOREIGN KEY (id_auto) REFERENCES autonoleggi(idauto),
    FOREIGN KEY (id_passeggero) REFERENCES passeggeri(idpasseggero)
)
'''

# query = '''
# DROP TABLE IF EXISTS prenotazioni_hotels''' 
# cur.execute(query)
HotelsReservations = '''
CREATE TABLE IF NOT EXISTS prenotazioni_hotels (
    idprenotazionehotels INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_hotel INTEGER NOT NULL,
    id_passeggero TEXT NOT NULL,
    FOREIGN KEY (id_hotel) REFERENCES hotels(idhotel),
    FOREIGN KEY (id_passeggero) REFERENCES passeggeri(idpasseggero)
    )
'''

cur.execute(Voyages)
cur.execute(Passengers)
cur.execute(CarRental)
cur.execute(Hotels)
cur.execute(FlightReservations)
cur.execute(CarRentalReservations)
cur.execute(HotelsReservations)
conn.commit()
    #conn.close()
    #cur.execute('''drop database sistema_prenotazioni''')
    #conn.commit()