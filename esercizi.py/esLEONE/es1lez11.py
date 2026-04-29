# Esercizio 1: Scrivi un semplice programma che simuli il comportamento del comando grep di Unix. 
# Fai che richieda all’utente l’inserimento di un’espressione regolare e poi ritorni il numero di righe che corrispondono alle specifiche della ricerca.

# image.png





import re

fhand= open('mbox.txt')

parola= input('Inserisci la parola da cercare: ')
count=0

try:
    for line in fhand:
        line= line.rstrip()
        if re.search(parola, line):
            count= count+1
except:
    print('la parola', parola, 'non è stata trovata')

print('la parola', parola, 'è stata trovata ', count, 'volte')

fhand.close()

#GODO PRIMO ESERCIZIO FATTO GODO
