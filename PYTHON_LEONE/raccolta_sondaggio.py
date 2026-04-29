def raccogli_dati():   # funzione che raccolga tutti i dati del sondaggio
    sposato_si = ['si', 's', 'vero', 'true', '1', 'yes', 'y', 'ya', 'oui']    # liste di possibili risposte 
    sposato_no = ['no', 'n', 'none', 'nope', '0', 'nein', 'false']

    nome = input("Inserisci il tuo nome: ").capitalize()     #input del nome del partecipante, e inserimento della prima lettera maiuscola in caso non venga messa

    while True:     #inserimento dell'età, e controllo se viene inserito un numero
        try:
            età = int(input("Quanti anni pensi che abbia? "))
            break
        except ValueError:
            print("Errore: Devi inserire un numero intero per l'età.")

    while True:     #inserimento altezza, con controllo numerico
        try:
            altezza = float(input("Quanto pensi che sia alto (in m)? "))
            break
        except ValueError:
            print("Errore: Devi inserire un numero decimale per l'altezza.")

    while True:         # inserimento stato matrimoniale, basando il controllo sulle liste create all'inizio del programma
        sposato = input("Pensi che sia sposato?: ").strip().lower()
        if sposato in sposato_si:
            sposato = "True"
            break
        elif sposato in sposato_no:
            sposato = "False"
            break
        else:
            print("Errore: Dai una risposta più sensata.")      # controllo in caso la risposta non sia presente nelle liste

    while True:
        materie = input("Quali materie credi che insegni? (separate da virgola): ").strip()     #inserimento materie
        if materie:
            break
        else:
            print("Errore: Devi inserire almeno una materia.")    #controllo se non viene inserito nulla

    materie_lista = ""
    for materia in materie.split(','):
        materia = materia.strip()  # Rimuoviamo gli spazi extra
        if materia:  # Verifica che non sia vuota
            if materie_lista:
                materie_lista += ";"  # Aggiungi il separatore solo se non è la prima materia
            materie_lista += materia

    file = open('sondaggio.txt', 'a')   #apertura file di testo in modalità append, in modo tale da non sovrascrivere i dati
    file.write(nome + "," + str(età) + "," + str(altezza) + "," + sposato + "," + materie_lista + "\n")   #aggiunta informazioni nel file
    file.close()   #chiusura file

    print("Dati salvati correttamente!")     

raccogli_dati()

