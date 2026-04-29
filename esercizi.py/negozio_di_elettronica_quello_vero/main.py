import sqlite3
from Prodotti import Prodotti
from Cliente import Clienti
from Negozio import Negozio

def menu():
    print("Benvenuto nel negozio di elettronica")
    print("Cosa vuoi fare?")
    print("1. Inserisci un cliente")
    print("2. Inserisci un prodotto")
    print("3. Inserisci un negozio")
    print("4. Effettua un acquisto")
    print("5. Visualizza i clienti")
    print("6. Visualizza i prodotti")
    print("7. Visualizza i negozi")
    print("8. Visualizza gli acquisti")
    print("9. Esci")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def contains_digit(s):
    return any(char.isdigit() for char in s)

def main():
    # Crea una connessione al database
    conn = sqlite3.connect('negozio.sqlite')
    c = conn.cursor()

    try:
        while True:
            menu()
            scelta = input("inserisci un numero : ")
#punto 1 
            if scelta == "1":
                while True:
                    cf = input("Inserisci il codice fiscale del cliente: ")
                    if len(cf) != 16:
                        print("Il codice fiscale deve essere di 16 caratteri")
                    else:
                        break

                while True:
                    nome = input("Inserisci il nome del cliente: ")
                    if contains_digit(nome):
                        print("Errore: la riga non deve contenere numeri!! Riprova")
                    else:
                        print("parametro accetato")
                        break   
                while True:
                    cognome = input("Inserisci il cognome del cliente: ")
                    if contains_digit(cognome):
                        print("Errore: la riga non deve contenere numeri!! Riprova")
                    else:
                        print("parametro accetato")
                        break

                while True:
                    citta = input("Inserisci la città del cliente: ")
                    if contains_digit(citta):
                        print("Errore: la riga non deve contenere numeri!! Riprova")
                    else:
                        print("parametro accetato")
                        break

                cliente_inserito = Clienti(cf, nome, cognome, citta)
                c.execute("INSERT INTO clienti (cf, nome, cognome, citta) VALUES (?, ?, ?, ?)", (cliente_inserito.cf, cliente_inserito.nome, cliente_inserito.cognome, cliente_inserito.citta))
                conn.commit()
                print("Cliente inserito con successo")

#punto 2 
            elif scelta == "2":
                codice_prodotto = input("Inserisci il codice del prodotto: ")

                while True:
                    nome = input("Inserisci il nome del prodotto: ")
                    if contains_digit(nome):
                        print("Errore: la riga non deve contenere numeri!! Riprova")
                    else:
                        print("parametro accetato")
                        break

                while True:
                    prezzo = input("Inserisci il prezzo del prodotto: ")
                    if is_number(prezzo):
                        prezzo = float(prezzo)
                        break
                    else:
                        print("Errore: inserisci un numero valido per il prezzo!! Riprova")

                while True:
                    quantita = input("Inserisci la quantità del prodotto: ")
                    if is_number(quantita):
                        quantita = int(quantita)
                        break
                    else:
                        print("Errore: inserisci un numero valido per la quantità!! Riprova")

                prodotto_inserito = Prodotti(codice_prodotto, nome, prezzo, quantita)
                c.execute("INSERT INTO prodotti (codProdotto, nome, prezzo, quantita) VALUES (?, ?, ?, ?)", (prodotto_inserito.codice_prodotto, prodotto_inserito.nome, prodotto_inserito.prezzo, prodotto_inserito.quantita))
                conn.commit()
                print("Prodotto inserito con successo")
#punto 3

            elif scelta == "3":
                nome = input("Inserisci il nome del negozio: ")

                while True:
                        nome = input("Inserisci il nome del negozio: ")
                        if contains_digit(nome):
                            print("Errore: la riga non deve contenere numeri!! Riprova")
                        else:
                            print("parametro accetato")
                        break
                
                nome = input("Inserisci il cognome del cliente: ")
                while True:
                    nome = input("Inserisci il cognome del cliente: ")
                    if contains_digit(nome):
                        print("Errore: la riga non deve contenere numeri!! Riprova")
                    else:
                        print("parametro accetato")
                        break

                citta = input("Inserisci la città del negozio: ")

                while True:
                        nome = input("Inserisci la città del negozio: ")
                        if contains_digit(nome):
                            print("Errore: la riga non deve contenere numeri!! Riprova")
                        else:
                            print("parametro accetato")
                            break

                negozio_inserito = Negozio(nome, citta)
                c.execute("INSERT INTO negozio (nome, citta) VALUES (?, ?)", (negozio_inserito.nome, negozio_inserito.citta))
                conn.commit()
                print("Negozio inserito con successo")
#punto 4

            elif scelta == "4":
                cf = input("Inserisci il codice fiscale del cliente: ")
                codice_prodotto = input("Inserisci il codice del prodotto: ")
                quantita = input("Inserisci la quantità del prodotto: ")
                if is_number(quantita):
                    quantita = int(quantita)
                else:
                    print("Errore: inserisci un numero valido per la quantità!! Riprova")
                    continue
                citta = input("Inserisci la città del negozio: ")
                c.execute("INSERT INTO acquisti (cf, codice_prodotto, quantita, citta) VALUES (?, ?, ?, ?)", (cf, codice_prodotto, quantita, citta))
                conn.commit()
                print("Acquisto effettuato con successo")
#punto 5

            elif scelta == "5":
                c.execute("SELECT * FROM clienti")
                clienti = c.fetchall()
                if clienti:
                    for cliente in clienti:
                        print(cliente)
                else:
                    print("Nessun cliente trovato")
#punto 6

            elif scelta == "6":
                c.execute("SELECT * FROM prodotti")
                prodotti = c.fetchall()
                if prodotti:
                    for prodotto in prodotti:
                        print(prodotto)
                else:
                    print("Nessun prodotto trovato")
#punto 7

            elif scelta == "7":
                c.execute("SELECT * FROM negozio")
                negozio = c.fetchall()
                if negozio:
                    for negozio in negozio:
                        print(negozio)
                else:
                    print("Nessun negozio trovato")
#punto 8

            elif scelta == "8":
                c.execute("SELECT * FROM acquisti")
                acquisti = c.fetchall()
                if acquisti:
                    for acquisto in acquisti:
                        print(acquisto)
                else:
                    print("Nessun acquisto trovato")
#punto 9

            elif scelta == "9":
                break

            else:
                print("Scelta non valida")
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        # Chiudi la connessione al database
        conn.commit()
        conn.close()

if __name__ == "__main__":
    main()





