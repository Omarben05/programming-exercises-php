''' Esercizio: Gestione di un Sistema di Prenotazione di Viaggi
Obiettivo
Scrivi un programma in Python che gestisca un sistema di prenotazione di viaggi. Il programma dovrà utilizzare:
-	Un sorgente per ogni classe necessaria per mappare gli oggetti Volo, Hotel, AutoNoleggio, Passeggero (totale 4 sorgenti diversi)
-	Un sorgente per la classe di utilità DatabaseUtilities per gestire la scrittura e lettura dal database
-	un sorgente per il main (potete chiamare il sorgente come volete) per coordinare le operazioni
Il programma dovrà permettere di:
-	registrare voli
-	registrare hotel
-	registrare noleggi auto
-	registrare passeggeri
-	prenotare ognuno dei servizi (volo, hotel, noleggio auto) per dei passeggeri
Requisiti:
-	Scrivere un’analisi
-	Scrivere in un file dump.py uno script che crea le tabelle in modo da permettere al programma di funzionare
-	Commentare il codice dove lo ritenete necessario
-	Gestire la persistenza dei dati utilizzando un database
-	Gestire tutti i possibili errori con il costrutto try-except
-	Gestire l’output a video in modo che sia di facile lettura per l’utente '''
'''analisi:
creazione del db: il db è organizzato in 5 tabelle:voli,hotel,autonoleggio,passeggero le prime 4 sono di semplice
 registrazione mentre la 5 è quella che va a contenere tutti i dettagli del viaggio del passeggero
 il programma si apre con la scelta tra il menu di visualizzazione o quello di modifica
 ogni menù ha 6 scelte per visualizzare/modificare ognuna delle 5 tabelle e per tornare alla scelta del menu
 il menu modifiche ha una settima scelta per cancellare un record '''
import sqlite3
from mappatura_voli import Voli
from mappatura_hotel import Hotel
from mappatura_autonoleggio import Auto
from mappatura_clienti import Cliente
from mappatura_viaggio import Viaggio
from DB_utilities import DB_strumenti
def menuvisualizzazione():
    print('1.visualizzare i voli')
    print('2.visualizzare gli hotel')
    print('3.visualizzare auto a noleggio')
    print('4.visualizzare i clienti')
    print('5.visualizzare viaggi prenotati')
    print('6.per tornare indietro')
def menuaggiunta():
    print('1.aggiungere i voli')
    print('2.aggiungere gli hotel')
    print('3.aggiungere auto a noleggio')
    print('4.aggiungere i clienti')
    print('5.aggiungere viaggi prenotati')
    print('6.per eliminare un record')
    print('7.per tornare indietro')

def visualizzazione(visualizza) :
    for a in visualizza:
        return a
def menu1():
        menu=int((input('inserire 1 applicare modifiche oppure 2 per visualizzare: ')))
        return menu 
def scelta():
        scelta=int(input('inserire il numero corrispondete all\' azione : '))
        return scelta
        
    
DBS=DB_strumenti()
DBS.connesione()

while True:
    try:
        menu=menu1()
    except:
        print('inserire solamente un numero indicato nel menù')
        continue
    if menu<1 or menu>2:
        print('inserire solamente un numero indicato nel menù')
        continue
    if menu==1 or menu==2:
        if menu==1 :
            while True:
                menuaggiunta()
                try :
                    sceltal=scelta()
                except:
                    print('inserire solamente un numero indicato nel menù')
                    continue
                if sceltal>7 or sceltal<1:
                    print('inserire solamente un numero indicato nel menù')
                if sceltal==1 :
                    ap_partenza=input('inserire l\' aereoporto di partenza: ')
                    ap_arrivo=input('inserire l\' aereoporto di arrivo: ')
                    compagnia=input('inserire la compagnia di volo: ')
                    giorno_orario_partenza=input('inserire giorno e orario di partenza: ')
                    volo=Voli(ap_partenza,ap_arrivo,compagnia,giorno_orario_partenza)
                    volo.salva_su_voli(DBS)
                if sceltal==2 :
                    nome_hotel=input('inserire il nome dell\' hotel: ')
                    indirizzo=input('inserire l\' indirizzo dell\'hotel: ')
                    hotel=Hotel(nome_hotel,indirizzo)
                    hotel.salva_su_hotel(DBS)
                if sceltal==3 :
                    targa=input('inserire la targa della vettura: ')
                    modello=input('inserire il modello della vettura: ')
                    auto=Auto(targa,modello)
                    auto.salva_su_auto(DBS)
                if sceltal==4 :
                    nome=input('inserire il nome del cliente: ')
                    cognome=input('inserire il cognome del cliente: ')
                    cliente=Cliente(nome,cognome)
                    cliente.salva_su_cliente(DBS)
                if sceltal==5 :
                    id_volo_andata=input('inserire l\'id del volo d\' andata : ')
                    id_volo_ritorno=input('inserire l\'id del volo di ritorno: ')
                    id_cliente=input('inserire l\'id del cliente : ')
                    id_hotel=input('inserire l\'id  dell hotel: ')
                    id_autonoleggio=input('inserire l\'id dell\'autonoleggio: ')
                    viaggio=Viaggio(id_volo_andata,id_volo_ritorno, id_cliente,id_hotel,id_autonoleggio)
                    viaggio.salva_su_viaggio(DBS)
                if sceltal==7 :
                    break
                if sceltal==6 :
                    while True:
                        print('1.eliminare un volo')
                        print('2.eliminare un hotel')
                        print('3.eliminare un auto a noleggio')
                        print('4.eliminare un cliente')
                        print('5.eliminare un viaggio prenotato')
                        print('6.per tornare indietro')
                        try :
                            sceltal=scelta()
                        except:
                            print('inserire solamente un numero indicato nel menù')
                            continue
                        if sceltal>6 or sceltal<1:
                            print('inserire solamente un numero indicato nel menù')
                        if sceltal==1 :
                            try:
                                dvolo=input('inserire l\'id del volo da eliminare: ')
                                DBS.elimina_volo(dvolo)
                            except:
                                print('Id non trovato o inesistente')
                                continue
                        if sceltal==2 :
                            dhotel=input('inserire l\'id dell\'hotel da cancellare: ')
                            DBS.elimina_hotel(dhotel)
                        if sceltal==3 :
                            dauto=input('inserire l\'id dell\'auto da cancellare :')
                            DBS.elimina_auto(dauto)
                        if sceltal==4 :
                            dcliente=input('inserire l\'id del cliente da eliminare : ')
                            DBS.elimina_cliente(dcliente)
                        if sceltal==5 :
                            dviaggio=input('inserire l\'id del viaggio da eliminare : ')
                            DBS.elimina_viaggio(dviaggio)
                        if sceltal==6 : 
                            break
        else :
            while True:
                menuvisualizzazione()
                try :
                    sceltal=scelta()
                except:
                    print('inserire solamente un numero indicato nel menù')
                    continue
                if sceltal>6 or sceltal<1:
                    print('inserire solamente un numero indicato nel menù')
                if sceltal==1 :
                    try:
                        dvolo=input('inserire l\'id del volo da visualizzare: ')
                        visualizza=DBS.visualizza_volo(dvolo)
                    except:
                        print('Id non trovato o inesistente')
                        continue
                    a=visualizzazione(visualizza)
                    if a==None:
                        print('id non trovato o inesistente')
                        continue
                    print("id,partenza,arrivo,compagnia,orario")
                    print(a)
                    
                if sceltal==2 :
                    try:
                        dhotel=input('inserire l\'id dell\' hotel da visualizzare: ')
                        visualizza=DBS.visualizza_hotel(dhotel)
                    except:
                        print('Id non trovato o inesistente')
                        continue
                    a=visualizzazione(visualizza)
                    if a==None:
                        print('id non trovato o inesistente')
                        continue
                    print("id,nome,indirizzo")
                    print(a)
                if sceltal==6:
                    break
    else:
        print('inserire un numero consentito')