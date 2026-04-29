# prendere dati
# 

# from oggetti import prof

class prof:
    def __init__(self, nome, età, altezza, sposato, materie): 
        self.__nome= nome
        self.__età= età
        self.__altezza= altezza
        self.__sposato= sposato
        self.__materie= materie

    def get_nome(self):
        return self.__nome
    def get_età(self):
        return self.__età
    def get_altezza(self):
        return self.__altezza
    def get_sposato(self):
        return self.__sposato
    def get_materie(self):
        return self.__materie 

# def raccogli_dati():   # funzione che raccolga tutti i dati del sondaggio
    sposato_si = ['si', 's', 'vero', 'true', '1', 'yes', 'y', 'ya', 'oui']    # liste di possibili risposte 
    sposato_no = ['no', 'n', 'none', 'nope', '0', 'nein', 'false']

def nome():
    while True:
        try:
            nome = input("Inserisci il tuo nome: ").capitalize()     #input del nome del partecipante, e inserimento della prima lettera maiuscola in caso non venga messa
            n = prof(nome)
            print(n)
            break
        except ValueError:
            print("Errore: Devi inserire un nome valido.")
def età():
    while True:     #inserimento dell'età, e controllo se viene inserito un numero
        try:
            età = int(input("Quanti anni pensi che abbia? "))
            break
        except ValueError:
            print("Errore: Devi inserire un numero intero per l'età.")
def altezza():
    while True:     #inserimento altezza, con controllo numerico
        try:
            altezza = float(input("Quanto pensi che sia alto (in m)? "))
            break
        except ValueError:
            print("Errore: Devi inserire un numero decimale per l'altezza.")
def sposato():
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
def materie():
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

#get_nome(self)
#get_età(self)

    #     return self.__età
    # def get_altezza(self):
    #     return self.__altezza
    # def get_sposato(self):
    #     return self.__sposato
    # def get_materie(self):
    #     return self.__materie 



## analisi dei dati

# def analizza_dati():     #funzione che prende i dati dal file di testo, e restituisce tutti gli output richiesti per il sondaggio
    
#     try:     # Controllo in caso il file non sia presente nel percorso giusto
#         file = open('sondaggio.txt','r') 
#     except FileNotFoundError:
#         print("Errore: Il file non esiste. Esegui prima il programma di raccolta dati, oppure controlla che sia nel percorso file giusto.")
#         return
    
#     num_partecipanti = 0           #creazione vari contatori utili all'analisi 
#     nomi_counter = {}
#     età_totale = 0
#     altezza_totale = 0.0
#     sposato_counter = 0
#     non_sposato_counter = 0
#     materie_counter = {}

#     for riga in file:  # Lettura del file riga per riga
#         dati = riga.strip().split(',')
#         if len(dati) != 5:
#             continue  # Salta righe non valide
        
#         nome = dati[0].capitalize()     #inserisce la prima lettere maiuscola in caso i dati siano stati modificati direttamente nel file 
#         età = dati[1]
#         altezza = dati[2]
#         sposato = dati[3]
#         materie = dati[4]
#         num_partecipanti += 1
        
#         nomi_counter[nome] = nomi_counter.get(nome, 0) + 1    #aggiornamento contatore dei nomi ripetuti
        
#         età_totale += int(età)
#         altezza_totale += float(altezza)
        
#         if sposato == "True":
#             sposato_counter += 1
#         else:
#             non_sposato_counter += 1
        
#         for materia in materie.split(';'):     #ciclo for basato su quante materie vengono scritte per riga
#             if materia in materie_counter:
#                 materie_counter[materia] += 1
#             else:
#                 materie_counter[materia] = 1

#     file.close()

#     if num_partecipanti == 0:    #controllo in caso il file sia vuoto
#         print("Il file è vuoto. Nessun dato da analizzare.")
#         return

#     # Calcolo statistiche
#     età_media = età_totale / num_partecipanti
#     altezza_media = altezza_totale / num_partecipanti
#     perc_sposato = (sposato_counter / num_partecipanti) * 100
#     perc_sposato = round(perc_sposato, 2)
#     perc_non_sposato = (non_sposato_counter / num_partecipanti) * 100
#     perc_non_sposato = round(perc_non_sposato, 2)
    
#     print("Statistiche raccolte su Leone:")
#     print("Numero totale di partecipanti:", num_partecipanti)
#     print("Nomi e frequenze:")
#     for nome, count in nomi_counter.items():
#         print(nome, count," ", end="")     #end consente di stampare sulla stessa riga il print
#     print("\nEtà media:", round(età_media, 0), "anni")
#     print("Altezza media:", round(altezza_media, 2), "m")
#     print("%d%% pensa che sia sposato, %d%% pensa che non lo sia" % (perc_sposato, perc_non_sposato))   # la formattazione %d%% stampa la variabile con il simbolo percentuale
#     print("Materie menzionate:")
#     for materia, count in materie_counter.items():
#         print(materia, "", count, "", end="")

# analizza_dati()


