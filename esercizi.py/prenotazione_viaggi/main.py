#programma in Python che gestisca un sistema di prenotazione di viaggi, tramite multiple sorgenti: classe di oggetti 1.Volo 2.Hotel 3.AutoNoleggio 4.Passeggero, database, main
#il programma per le prenotazioni di viaggi deve permettere di (registrare voli) - (registrare hotel) - (registrare noleggi auto) - (registrare passeggeri) - (prenotare ognuno dei servizi (volo, hotel, noleggio auto) per dei passeggeri)

#   end recaption: 
#       the program crate's the database on it's own and the tables "utenti" "volo" "hotel" "autonoleggi", 
#       whit the main i use a multiple coice based menu, to operate on the classes and insert the information on the database

from DatabaseUtilities import *
from dump import *

while True :                                                        #this is the menu and it cycle until the user inserts the value "6"
    print('''\n
    ------------------- viaggi ---------------------
        1. registra un nuovo utente
        2. registra un nuovo volo
        3. regiusta un nuovo hotel
        4. registra un nuovo veicolo da noleggiare
        5. prenota
        6. Uscire 
    ------------------------------------------------
    ''')


    while True:                                                     #checking the value of the imput 
        try:
            scelta = int(input("Seleziona un'opzione del menù : "))
            if scelta < 1 or scelta > 6 :
                print('Inserisci un valore numerico corretto')
                continue
        except ValueError:
            print("Errore: Devi inserire un numero valido.")
            continue
        break


    match (scelta) :
        case 1 :
                agg_utente()                                        #add a new user
        case 2 :
                agg_volo()                                          #add a new flight
        case 3 :
                agg_hotel()                                         #add a new hotel
        case 4 :
                agg_autonoleggi()                                   #add a new cars to the car rental
        case 5:
                prenotazioni()                                      #let the user make reservations
        case 6 :
            exit()