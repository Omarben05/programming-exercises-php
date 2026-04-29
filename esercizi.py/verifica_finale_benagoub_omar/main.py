#importo la creazione il database 
from dump import *
# importo le funzioni per la gestione del database
from DatabaseUtilities import *

# creo il menu con le varie opzioni
def menu():
    print('''\n
    ------------------- Sistema prenotazioni visite ---------------------
        1. registra un nuovo paziente
        2. visualizza i pazienti registrati
        3. registra un nuovo medico
        4. visualizza i medici registrati
        5. registra una nuova visita
        6. visualizza le visite registrate
        7. Esci
    ------------------------------------------------
    ''')
    
# Main
# ciclo while che richiede il numero fino a quando non si ha inserito un valore
# contenuto nel menu 
while True:      
    print(menu())
    try:
        scelta = int(input("Inserire un numero: "))
        if scelta < 1 or scelta > 7 :
            print('Inserisci un numero valido')
            continue
    except ValueError:
        print("Errore: la scelta inserita non è valida.")
        continue
    break

# switch case per la scelta dell'utente
match (scelta):
        case 1:
            registrazione_paziente()
        case 2:
            visualizza_pazienti()
        case 3:
            registrazione_medico()
        case 4:
            visualizza_medici()
        case 5:
            registrazione_visita()
        case 6:
            visualizza_visite()