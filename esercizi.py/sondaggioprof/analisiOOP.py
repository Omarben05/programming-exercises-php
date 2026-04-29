# from sondaggioOOP import Prof


def analizza_dati():     #funzione che prende i dati dal file di testo, e restituisce tutti gli output richiesti per il sondaggio
    
    try:     # Controllo in caso il file non sia presente nel percorso giusto
        file = open('sondaggio.txt','r') 
    except FileNotFoundError:
        print("Errore: Il file non esiste. Esegui prima il programma di raccolta dati, oppure controlla che sia nel percorso file giusto.")
        return
    
    num_partecipanti = 0           #creazione vari contatori utili all'analisi 
    nomi_counter = {}
    età_totale = 0
    altezza_totale = 0.0
    sposato_counter = 0
    non_sposato_counter = 0
    materie_counter = {}

    for riga in file:  # Lettura del file riga per riga
        dati = riga.strip().split(',')
        if len(dati) != 5:
            continue  # Salta righe non valide
        
        nome = dati[0].capitalize()     #inserisce la prima lettere maiuscola in caso i dati siano stati modificati direttamente nel file 
        età = dati[1]
        altezza = dati[2]
        sposato = dati[3]
        materie = dati[4]
        num_partecipanti += 1
       
        nomi_counter[nome] = nomi_counter.get(nome, 0) + 1    #aggiornamento contatore dei nomi ripetuti
        
        età_totale += int(età)
        altezza_totale += float(altezza)
        
        if sposato == "True":
            sposato_counter += 1
        else:
            non_sposato_counter += 1
        
        for materia in materie.split(';'):     #ciclo for basato su quante materie vengono scritte per riga
            if materia in materie_counter:
                materie_counter[materia] += 1
            else:
                materie_counter[materia] = 1

    file.close()

    if num_partecipanti == 0:    #controllo in caso il file sia vuoto
        print("Il file è vuoto. Nessun dato da analizzare.")
        return

    # Calcolo statistiche
    età_media = età_totale / num_partecipanti
    altezza_media = altezza_totale / num_partecipanti
    perc_sposato = (sposato_counter / num_partecipanti) * 100
    perc_sposato = round(perc_sposato, 2)
    perc_non_sposato = (non_sposato_counter / num_partecipanti) * 100
    perc_non_sposato = round(perc_non_sposato, 2)
    
    print("Statistiche raccolte su Leone:")
    print('-------------------------------')
    print("Numero totale di partecipanti:", num_partecipanti)
    print("Nomi e frequenze:")
    for nome, count in nomi_counter.items():
        print(nome, count,"", end=" ")     #end consente di stampare sulla stessa riga il print
    print("\nEtà media:", round(età_media, 0), "anni")
    print("Altezza media:", round(altezza_media, 2), "m")
    print("%d%% pensa che sia sposato, %d%% pensa che non lo sia" % (perc_sposato, perc_non_sposato))   # la formattazione %d%% stampa la variabile con il simbolo percentuale
    print("Materie menzionate:")
    for materia, count in materie_counter.items():
        print(materia, count, "", end=" ")


if __name__ == "__main__":
    analizza_dati()



