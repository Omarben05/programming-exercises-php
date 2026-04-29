import sqlite3
conn = sqlite3.connect('sistema_prenotazioni_visite.sqlite')
cur = conn.cursor()
#----------------------------------------------------------------------------------------------------

# inp = domanda all'utente

# funzione per controllare che la stringa non contenga numeri

def controllo_string (inp):
    while True:
        messaggio = input(inp).strip()
         #isalpha() restituisce True se tutti i caratteri della stringa sono alfabetici no num spazi caratt
        if messaggio.isalpha() and len(messaggio) > 0:   
            return messaggio
        else:
            print("Errore: la riga non deve contenere numeri! Riprova")

# funzione per controllare che la stringa non contenga lettere

def controllo_int (inp):
    while True:
        messaggio = input(inp).strip()
        #isdigit() restituisce True se tutti i caratteri della stringa sono numerici
        if messaggio.isdigit() and len(messaggio) > 0:    
            return messaggio
        else:
            print("Errore: la riga non deve contenere lettere! Riprova")  

# funzione per controllare che il codice fiscale sia valido

def controllo_codice_fiscale (inp):
    while True:
        messaggio = input(inp).strip()
        if len(messaggio) == 16:    
            return messaggio
        else:
            print("Errore: il codice fiscale deve contenere 16 caratteri! Riprova")

#---------------------------------------------------------------------------------------------

# funzione per registrare un paziente

def registrazione_paziente(): 
    from Paziente import CPaziente
    codice_fiscale_paziente = controllo_codice_fiscale("Inserisci il codice fiscale: ")
    nome = controllo_string("Inserisci il nome: ")
    cognome = controllo_string("Inserisci il cognome: ")
    paziente = CPaziente(codice_fiscale_paziente, nome, cognome)
    try: 
        cur.execute("INSERT INTO pazienti (codice_fiscale_paziente, nome, cognome) VALUES (?, ?, ?)", (paziente.get_codice_fiscale_paziente(), paziente.get_nome(), paziente.get_cognome()))
        conn.commit()
        print("Paziente inserito con successo")
    except Exception as e:
        print("Errore: ", e)

# funzione per visualizzare i pazienti registrati
def visualizza_pazienti():
    cur.execute("SELECT * FROM pazienti")
    conn.commit()
    for row in cur.fetchall():
        print(row)

# funzione per registrare un medico
def registrazione_medico(): 
    from Medico import CMedico 
    codice_fiscale_medico = controllo_codice_fiscale("Inserisci il codice fiscale: ")
    nome = controllo_string("Inserisci il nome: ")  
    cognome = controllo_string("Inserisci il cognome: ")
    campo = controllo_string("Inserisci il campo di specializzazione: ")
    medico = CMedico(codice_fiscale_medico, nome, cognome, campo)
# controllo possibilità prenotare un medico se non esistono almeno un paziente
    try: 
        cur.execute("SELECT * FROM pazienti")
        conn.commit()
        if cur.fetchone() == None:
            print("Errore: non è possibile inserire un medico senza pazienti")
            exit()
        cur.execute("INSERT INTO medici (codice_fiscale_medico, nome, cognome, campo) VALUES (?, ?, ?, ?)", (medico.get_codice_fiscale_medico(), medico.get_nome(), medico.get_cognome(), medico.get_campo()))
        conn.commit()
        print("Medico inserito con successo")
    except Exception as e:
        print("Errore: ", e)

# funzione per visualizzare i medici registrati
def visualizza_medici():
    cur.execute("SELECT * FROM medici")
    conn.commit()
    for row in cur.fetchall():
        print(row)

# FUNZIONE PER REGISTRARE UNA VISITA
def registrazione_visita():
# controllo possibilità prenotare una visita se non esistono almeno un paziente e un medico
    try: 
        cur.execute("SELECT * FROM pazienti")
        conn.commit()
        if cur.fetchone() == None:
            print("Errore: non è possibile inserire una visita senza pazienti")
            exit()
        cur.execute("SELECT * FROM medici")
        conn.commit()
        if cur.fetchone() == None:
            print("Errore: non è possibile inserire una visita senza medici")
            exit()
    except:
        exit()
# controllo possibilità medico può visitare fino a 3 pazienti diversi
    try:
        cur.execute("SELECT COUNT(*) FROM visite WHERE cognome_medico = ?", (visita.get_cognome_medico(),))
        conn.commit()
        if cur.fetchone()[0] >= 3:
            print("Errore: il medico ha già 3 visite")
            exit()
    except:
        exit()
# controllo possibilità prenotare una visita se non ci sono almeno un paziente senza un medico assegnato e un medico con disponibilità
    try: 
        cur.execute("SELECT COUNT(*) FROM visite WHERE cognome_paziente = ?", (visita.get_cognome_paziente(),))
        conn.commit()
        if cur.fetchone()[0] >= 1:
            print("Errore: il paziente ha già una visita")
            exit()
    except:
        exit()
#inserimento effettivo della visita
    from Visita import CVisita
    cognome_paziente = controllo_string("Inserisci il cognome del paziente: ")
    cognome_medico = controllo_string("Inserisci il cognome del medico: ")
    visita = CVisita(cognome_paziente, cognome_medico)
    try: 
        cur.execute("INSERT INTO visite (cognome_paziente, cognome_medico) VALUES (?, ?)", (visita.get_cognome_paziente(), visita.get_cognome_medico()))
        conn.commit()
        print("Visita inserita con successo")
    except Exception as e:
        print("Errore: ", e)
        

# funzione per visualizzare le visite registrate
def visualizza_visite():
    cur.execute("SELECT * FROM visite")
    conn.commit()
    for row in cur.fetchall():
        print(row)

