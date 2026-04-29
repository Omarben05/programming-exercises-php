from DatabaseUtilities import *
from dump import *

def menu():
    print("-----Benvenuto nel sistema di prenotazione viaggi-----")
    print("-----Cosa vuoi fare?-----")
    print("-----1. Registra un volo-----")
    print("-----2. Registra un hotel-----")
    print("-----3. Registra un auto-----")
    print("-----4. Registra un passeggero-----")
    print("-----5. Visualizza i voli-----")
    print("-----6. Visualizza gli hotel-----")
    print("-----7. Visualizza le auto-----")
    print("-----8. Visualizza i passeggeri-----")
    print("-----9. Prenota un volo-----")
    print("-----10. Prenota un hotel-----")
    print("-----11. Prenota un auto-----")
    print("-----12. Visualizza le prenotazioni voli-----")
    print("-----13. Visualizza le prenotazioni hotel-----")
    print("-----14. Visualizza le prenotazioni auto-----")
    print("-----15. Esci-----")
   
while True:
    menu()
    scelta = int(input("Inserisci un numero: "))
    match (scelta): 
        case 1: 
            registrazione_volo()
        case 2: 
            registrazione_hotel()
        case 3: 
            registrazione_auto()
        case 4: 
            registrazione_passeggero()

        case 5: 
            visualizza_voli()
        case 6: 
            visualizza_hotel()
        case 7: 
            visualizza_auto
        case 8: 
            visualizza_passeggeri()

        case 9: 
            prenotazione_volo()
        case 10:
            prenotazione_hotel()
        case 11:
            prenotazione_auto()

        case 12: 
            v_prenotazioni_voli()
        case 13: 
            v_prenotazioni_hotel()
        case 14: 
            v_prenotazioni_auto()
            
        case 15:
            break 