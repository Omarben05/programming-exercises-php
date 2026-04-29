import sqlite3

conn = sqlite3.connect('Prenotazione_Viaggi.sqlite') 
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS destinazioni (
    città TEXT NOT NULL PRIMARY KEY
);
                      
CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    numero_telefono TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS hotel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    indirizzo TEXT NOT NULL,
    città TEXT NOT NULL,
    numero_telefono TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS utenti_hotel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utente INTEGER,
    id_hotel INTEGER,
    FOREIGN KEY (id_hotel) REFERENCES hotel(id),
    FOREIGN KEY (id_utente) REFERENCES utenti(id)
);

CREATE TABLE IF NOT EXISTS volo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destinazione text not null,
    FOREIGN KEY (destinazione) REFERENCES destinazioni(città)
);
                
CREATE TABLE IF NOT EXISTS utenti_voli (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utente INTEGER,
    id_volo INTEGER,
    FOREIGN KEY (id_volo) REFERENCES volo(id),
    FOREIGN KEY (id_utente) REFERENCES utenti(id)
);
                      
CREATE TABLE IF NOT EXISTS autonoleggi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modello TEXT not null
);

CREATE TABLE IF NOT EXISTS utenti_autonoleggi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utente INTEGER,
    id_autonoleggio INTEGER,
    FOREIGN KEY (id_autonoleggio) REFERENCES autonoleggi(id),
    FOREIGN KEY (id_utente) REFERENCES utenti(id)
);

''')

def drop_database():
        cur.executescript ('DROP DATABASE IF IT EXISTS Prenotazione_Viaggi')
#drop_database()  #da usare in caso di necessita di ripulire e ravviare il database