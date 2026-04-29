## CREAZIONE DELLE TABELLE NEL DATABASE



# importazione di sqlite3
import sqlite3
#connessione al database e creazione dello stesso
conn = sqlite3.connect('sistema_prenotazioni_visite.sqlite') 
# creazione del cursore
cur = conn.cursor() 

# creazione delle tabelle
cur.executescript('''
                  
CREATE TABLE IF NOT EXISTS pazienti (
    codice_fiscale_paziente TEXT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS medici (
    codice_fiscale_medico TEXT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    campo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS visite (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cognome_paziente TEXT NOT NULL,
    cognome_medico TEXT NOT NULL,
    FOREIGN KEY (cognome_paziente) REFERENCES pazienti(cognome),
    FOREIGN KEY (cognome_medico) REFERENCES medici(cognome)
);
                  
''')


conn.commit()  # salva i cambiamenti
