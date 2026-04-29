### Esercizio 1: Rivedi uno degli script precedenti nel modo seguente: leggi e analizza le righe contenenti “From” ed estrai gli indirizzi dalla riga.
### Conta il numero di messaggi provenienti da ogni persona usando un dizionario. Dopo aver letto tutti i dati, 
### visualizza la persona con il maggior numero di occorrenze creando un elenco di tuple (count, email) dal dizionario. 
### Quindi ordina l’elenco in ordine inverso e visualizza la persona che ha il maggior numero di occorrenze. Esempio di risultato atteso:

### Inserire un nome per il file: mbox-short.txt
### cwen@iupui.edu 5
### Immettere un nome file: mbox.txt
### zqian@umich.edu 195


fname= input('Inserire un nome per il file: ')
fhand= open(fname)

a= dict()
t= list()
for line in fhand:
    words= line.split()
    if len(words)>2 and words[0] == 'From': 
     a[words[1]]= a.get(words[1],0) +1
for key in a:
    b=(a[key], key)
    t.append(b)
t.sort(reverse=True)
print(t[:1])