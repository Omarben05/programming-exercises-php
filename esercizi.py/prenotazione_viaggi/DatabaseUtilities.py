def getConnection():
    import sqlite3
    conn = sqlite3.connect('Prenotazione_Viaggi.sqlite')
    return conn

def getCursor(conn):
    return conn.cursor()

def controllo_stringhe (messaggio) :
    while True:
        stringa = input(messaggio).strip()
        if stringa.isalpha() and len(stringa) > 0:
            return stringa
        else:
            print("Errore: Il valore inserito non è valido.")

def controllo_int (messaggio) :
      while True:
        valore = input(messaggio).strip()
        if valore.isdigit():
            return int(valore)
        else:
            print("Errore: Devi inserire un numero valido.")

def numero_tel () :
    while True:
            numero_cellulare = input("\nInserisci il Numero di cellulare: ").strip()
            if numero_cellulare.isdigit() and len(numero_cellulare) >= 10:
                return numero_cellulare
            else:
                print("Errore: Il numero di cellulare deve contenere almeno 10 cifre.")

def agg_utente () :
    from utente import Utenti
    primo_ingresso = True
    while (True) :   
        if primo_ingresso == False: 
            risposta = input("\nHai finito di inserire i utenti? (sì => per uscire): ").strip().lower()
            if risposta == "si":
                break
        primo_ingresso = False
        nome = controllo_stringhe("\nInserisci il nome del utente: ")
        cognome = controllo_stringhe("\nInserisci il Cognome del utente: ")
        numero_telefono = numero_tel()
        utente = Utenti(nome, cognome, numero_telefono)
        try:
            conn = getConnection()
            cur = getCursor(conn)
            cur.execute('INSERT INTO utenti (nome, cognome, numero_telefono) VALUES (?, ?, ?)', (utente.get_nome(),utente.get_cognome(),utente.get_numero_telefono()))
            conn.commit()
            print("Utente registrato con successo!")
        except Exception as e:
            print("Errore:",e)

def agg_volo () :
    from volo import Voli
    primo_ingresso = True
    while (True) :   
        if primo_ingresso == False: 
            risposta = input("\nHai finito di inserire voli? (sì => per uscire): ").strip().lower()
            if risposta == "si":
                break
        primo_ingresso = False
        destinazione = controllo_stringhe("\nInserisci il nome della destinazione del volo: ")
        volo = Voli(destinazione)
        try:
            conn = getConnection()
            cur = getCursor(conn)
            cur.execute('INSERT INTO volo (destinazione) VALUES (?)', (volo.get_destinazione(),))
            conn.commit()
            print("volo registrato con sucesso!")
        except Exception as e:
            print("Errore:",e)

def agg_hotel () :
    from hotel import Hotel
    primo_ingresso = True
    while (True) :   
        if primo_ingresso == False: 
            risposta = input("\nHai finito di inserire hotel? (sì => per uscire): ").strip().lower()
            if risposta == "si":
                break
        primo_ingresso = False
        nome = controllo_stringhe("\nInserisci il nome del hotel: ")
        indirizzo = input("\nInserisci l'indirizzo del hotel: ")
        città = controllo_stringhe("\nInserisci la citta: ")
        numero_telefono = numero_tel()
        hotel = Hotel(nome, indirizzo, città, numero_telefono)
        try:
            conn = getConnection()
            cur = getCursor(conn)
            cur.execute('INSERT INTO hotel (nome, indirizzo, città, numero_telefono) VALUES (?,?,?,?)', (hotel.get_nome(), hotel.get_indirizzo(), hotel.get_città(), hotel.get_numero_telefono()))
            conn.commit()
            print("hotel registrato con sucesso!")
        except Exception as e:
            print("Errore:",e)

def agg_autonoleggi () :
    from autonoLeggio import Autonoleggio
    primo_ingresso = True
    while (True) :   
        if primo_ingresso == False: 
            risposta = input("\nHai finito di inserire auto? (sì => per uscire): ").strip().lower()
            if risposta == "si":
                break
        modello = input('\nInserisci il modello della nuova macchina: ')
        if not len(modello) > 0:
            print("Errore: Il valore inserito non è valido.")
            continue
        primo_ingresso = False
        autonoLeggio = Autonoleggio(modello)
        try:
            conn = getConnection()
            cur = getCursor(conn)
            cur.execute('INSERT INTO autonoleggi (modello) VALUES (?)', (autonoLeggio.get_modello()))
            conn.commit()
            print("veicolo registrato con sucesso!")
        except Exception as e:
            print("Errore:",e)

def prenotazioni():
    primo_ingresso = True
    while True:                                                                                                 #chi sta operando
        if primo_ingresso == False: 
            risposta = input("\nHai finito di inserire prenotazioni? (sì => per uscire): ").strip().lower()
            if risposta == "si":
                break
        primo_ingresso = False
        conn = getConnection()                                                          
        cur = getCursor(conn)
        id_utente = controllo_int("\nInserisci l'ID del utente che vuole prenotare dei servizi: ")
        #print('funge')
        cur.execute("SELECT id FROM utenti WHERE id = ?", (id_utente,))
        utente = cur.fetchone()  

        if utente is None:
            print("Errore: questo membro non esiste.")
            continue
        #print('buono')
        print('''
----- cosa vuoi prenotare? -----
    1. VOLI
    2. VEICOLI
    3. HOTEL
    4. ESCI
--------------------------------
''')
        while True:                                                     #checking the value of the imput 
                try:
                    scelta2 = int(input("Seleziona un'opzione del menù : "))
                    if scelta2 < 1 or scelta2 > 4 :
                        print('Inserisci un valore numerico corretto')
                        continue
                except ValueError:
                    print("Errore: Devi inserire un numero valido.")
                    continue
                break
        
        match (scelta2) :
            case 1 :
                    prenota_voli(id_utente)
            case 2 :
                    prenota_autonoleggi(id_utente)
            case 3 :
                    prenota_hotel(id_utente)
            case 4 :
                break

def prenota_voli(id_utente):
    conn = getConnection()                                                          
    cur = getCursor(conn)

    cur.execute("SELECT * FROM volo")     # Mostra tutti i voli disponibili
    conn.commit()
    for row in cur.fetchall():
        print(row)

    # Input dell'ID del volo
    id_volo = controllo_int("\nInserisci l'ID del volo che vuole prenotare: ")

    cur.execute("SELECT id FROM volo WHERE id = ?", (id_volo,))  # Controllo se il volo esiste
    conn.commit()
    
    volo = cur.fetchone() #prende il valore dal database dopo la select

    if volo is None:
        print("Volo non prenotato\nErrore: questo volo non esiste.")
        return False

    try:
        cur.execute("INSERT INTO utenti_voli (id_utente, id_volo) VALUES (?, ?)", (id_utente, volo[0]))  #volo lo prende come tupla quidni gli devi dire in posizione 0 con [0]
    except Exception as e:
        print("Errore:", e)

    
def prenota_autonoleggi(id_utente):
    conn = getConnection()                                                          
    cur = getCursor(conn)

    cur.execute("SELECT * FROM autonoleggi")
    conn.commit()
    for row in cur.fetchall():
        print(row)
        
    id_auto = controllo_int("\nInserisci l'ID del veicolo che vuoi noleggiare: ")
    #print('funge')
    cur.execute("SELECT id FROM utenti WHERE id = ?", (id_auto,))
    conn.commit()

    auto = cur.fetchone()   #prende il valore dal database dopo la select

    if auto is None:
        print("Veicolo non noleggiato\nErrore: questo veicolo non esiste.")
        return True
    else: print('auto noleggiata con successo')
    try:
        cur.execute('insert into utenti_autonoleggi (id_utente, id_autonoleggio) VALUES (?,?)', (id_utente, auto[0])) #stessa cosa di volo viene preso come tupla
        conn.commit()
    except Exception as e:
        print('Errore:', e)
    

def prenota_hotel(id_utente):
    conn = getConnection()                                                          
    cur = getCursor(conn)

    cur.execute("SELECT * FROM hotel")
    conn.commit()
    for row in cur.fetchall():
        print(row)

    id_hotel = controllo_int("\nInserisci l'ID del hotel in qui vuoi allogiare: ")
    #print('funge')
    cur.execute("SELECT id FROM hotel WHERE id = ?", (id_hotel,))
    conn.commit()

    hotel = cur.fetchone()      #prende il valore dal database dopo la select

    if hotel is None:
        print("hotel non prenotato\nErrore: questo hotel non esiste.")
        return True
    else: print('hotel prenotato con successo')
    try:
        cur.execute('insert into utenti_hotel (id_utente, id_hotel) VALUES (?,?)', (id_utente, hotel[0])) #tupla in posizione 0 
        conn.commit()
    except Exception as e:
        print('Errore:', e)

    