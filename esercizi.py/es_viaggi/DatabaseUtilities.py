import sqlite3
conn = sqlite3.connect('sistema_prenotazioni.sqlite')
cur = conn.cursor()

# inp = domanda all'utente

def controllo_string (inp):
    while True:
        messaggio = input(inp).strip()
        if messaggio.isalpha() and len(messaggio) > 0:    #isalpha() restituisce True se tutti i caratteri della stringa sono alfabetici no num spazi caratt
            return messaggio
        else:
            print("Errore: la riga non deve contenere numeri!! Riprova")
        
def controllo_int (inp):
    while True:
        messaggio = input(inp).strip()
        if messaggio.isdigit() and len(messaggio) > 0:    #isdigit() restituisce True se tutti i caratteri della stringa sono numerici
            return messaggio
        else:
            print("Errore: la riga non deve contenere lettere!! Riprova")   


def registrazione_volo(): 
    from Volo import CVolo
    partenza = controllo_string("Inserisci la città di partenza: ")
    destinazione = controllo_string("Inserisci la città di destinazione: ")
    data = input("Inserisci la data: ")
    ora = input("Inserisci l'ora: ")
    prezzo = controllo_int("Inserisci il prezzo: ")
    
    volo = CVolo(partenza, destinazione, data, ora, prezzo)
    try: 
        cur.execute("INSERT INTO voli (partenza, destinazione, data, ora, prezzo) VALUES (?, ?, ?, ?, ?)", (volo.get_partenza(), volo.get_destinazione(), volo.get_data(), volo.get_ora(), volo.get_prezzo()))
        conn.commit()
        print("Volo inserito con successo")
    except Exception as e:
        print("Errore: ", e)

def registrazione_hotel():
    print()
def registrazione_auto():
    print()
def registrazione_passeggero():
    from Passeggero import CPasseggero
    nome = controllo_string("Inserisci il nome: ")
    cognome = controllo_string("Inserisci il cognome: ")
    passeggero = CPasseggero(nome, cognome) 
    try: 
        cur.execute("INSERT INTO passeggeri (nome, cognome) VALUES (?, ?)", (passeggero.get_nome(), passeggero.get_cognome()))
        conn.commit()
        print("Passeggero inserito con successo")
    except Exception as e:
        print("Errore: ", e)

    

def visualizza_voli():
    cur.execute("SELECT * FROM voli")
    for row in cur.fetchall():
        print(row)
    
def visualizza_hotel():
    print()
def visualizza_auto():
    print()
def visualizza_passeggeri():
    print()
    

def prenotazione_volo():
    id_volo = controllo_int("Inserisci l'id del volo: ")
    id_passeggero = controllo_int("Inserisci l'id del passeggero: ")
    try: 
        cur.execute("INSERT INTO prenotazioni_voli (id_volo, id_passeggero) Values (?, ?)" , (id_volo, id_passeggero))
        conn.commit()
        print("Prenotazione effettuata con successo")
    except Exception as e:
        print("Errore: ", e)

def prenotazione_hotel():
    print()
def prenotazione_auto():
    print()
    

def v_prenotazioni_voli():
    print()
    cur.execute("SELECT * FROM prenotazioni_voli")
    for row in cur.fetchall():
        print(row)
def v_prenotazioni_hotel():
    print()
def v_prenotazioni_auto():
    print()





