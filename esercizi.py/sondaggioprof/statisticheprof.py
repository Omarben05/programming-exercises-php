# statistiche prof: lavoro di gruppo 
# Esercizio: Statistiche sul prof
#Obiettivo: Creare due programmi in Python. Il primo programma raccoglie informazioni su di me e le scrive su un file di output. Il secondo programma legge il file scritto dal primo e genera statistiche.
#Parte 1: Raccolta delle Informazioni
'''Scrivere un programma in Python che chieda all'utente di partecipare ad un sondaggio su di me. Il programma deve:
1.	Chiedere il nome della persona che sta partecipando.
2.	Chiedere quanti anni crede che io abbia (gestito come un numero intero).
3.	Chiedere quanto pensa che sia alto (gestito come un numero decimale).
4.	Chiedere se pensa che sia sposato (gestito come un valore booleano).
5.	Chiedere quali materie crede che insegni sul corso di Software Developer (gestito come un elenco di stringhe).
Le informazioni raccolte devono essere scritte su un file di output. Ogni volta che il programma viene eseguito, le nuove informazioni devono essere aggiunte al file senza sovrascrivere quelle esistenti
 (quindi dopo 5 utenti il file dovrà avere “5 x 5” valori)
Parte 2: Generazione delle Statistiche
Scrivere un secondo programma in Python che legga il file di output prodotto dal primo programma e generi statistiche sulle informazioni raccolte. Le statistiche devono includere:
•	Numero totale di persone registrate.
•	Elenco dei nomi delle persone con l indicazione di quante persone con quel nome hanno partecipato al sondaggio (es. “Mario 2, Giovanni 1, Mimmo 6”)
•	Età media inserita dagli utenti
•	Altezza media inserita dagli utenti
•	Percentuale di persone che pensano che sia sposato e che pensano che non lo sia (es. “40% pensa che sia sposato, 60% pensa che non sia sposato”).
•	Elenco delle materie inserite e il numero di volte che ciascuna materia è stata menzionata.
Requisiti/suggerimenti:
•	Scrivere un analisi
•	Commentare il codice dove lo ritenete necessario
•	Scrivere 2 programmi separati
•	Il primo programma deve essere eseguito una volta per ogni utente (quindi NO ciclo per permettere l’inserimento a più utenti)
•	Attenzione alla gestione del file di output: alla prima esecuzione non esisterà, dalla seconda esecuzione in poi non dovremo sovrascrivere quanto inserito fino a quel momento
•	Gestire gli errori con il costrutto try/except prevedendo di mostrare messaggi di errore comprensibili all’utente.
•	Visualizzare le informazioni raccolte in modo strutturato alla fine del programma.
'''
#aprire un file in modalità scrittura
fhand = open('sondaggio.txt', 'w')
#scrivere nel file
#creare input nome stringa
def utente():
    nome_partecipante = str(input('Inserisci il tuo nome: '))
#creare input anni intero
    anni = int(input('Quanti anni pensi che abbia il professore? '))
#creare input altezza float
    altezza = float(input('Quanto pensi sia alto? '))
    altezza = round(altezza, 2) #fa in modo che mi escono solo 2 cifre dopo la virgola
    #creare input sposato Bool
    positive = ['si', 's','y', 'yes', 'true', '1']
    negative=['no', 'n', 'none' , 'false', '0']
    matrimonio = input('è sposato? ')
    matrimonio=matrimonio.lower()
    if matrimonio in positive:
        matrimonio = True
    elif matrimonio in negative:
        matrimonio = False

    #creare una lista vuota (materie)
    materie = []
    n = int(input('Quante materie pensi che insegni il professore? '))
    for i in range(n):
        materia = input('Inserisci la materia: ')
        materie.append(materia)
    print(nome_partecipante,anni,altezza,matrimonio, materie)
    fhand.write(nome_partecipante,anni,altezza,matrimonio, materie)
for n in range(2):
    utente()


#creare input materie Leone lista stringhe
#chiudi file scrittura
#apriamo file lettura
#somma partecipanti int
#lista nomi vuota
#lista nomi ( fai conteggio nomi uguali)
#età media prof
#altezza media prof
#media sposato prof
#lista materia vuota
#lista materia (fai il conteggio materie)