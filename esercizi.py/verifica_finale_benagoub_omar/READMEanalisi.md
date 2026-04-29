Il programma dovrà permettere di:
-	registrare Pazienti
-	registrare Medici
    o	Non deve essere possibile registrare medici se non esistono pazienti
-	organizzare visite
    o	Non deve essere possibile prenotare una visita se non esistono almeno un paziente e un medico
    o	Un medico può visitare fino a 3 pazienti diversi
    o	Non deve essere possibile prenotare una visita se non ci sono almeno un paziente senza un medico assegnato e un medico con disponibilità


Creo una sorgente per ogni classe all'interno una classe per :
Pazienti, Medici e Visita

creo un database su cui salvare i dati di input:
creo 3 tabelle:
-Tabella pazienti
    codice fiscale
    nome
    cognome
-Tabella medici
    codice fiscale
    nome
    cognome
-tabella visite
    id visita
    codice fiscale paziente
    codice fiscale medico

Progettazione del main
creo il menù con le opzioni possibili da eligere:
registrare pazienti o medici, visualizzarli, o prenotare una visita.

mi sposto su DatabaseUtilities dove creo 
-le funzioni per gestire l'input di stringhe e interi, ma 
    anche per il controllo validità del cf di 16 caratteri
-le funzioni per ciascuna opzione in modo tale da inserire nel database 
    gli input dell'utente, ogni dato viene inserito all'interno della classe 

    il tutto secondo le regole impostate:
    o	Non deve essere possibile registrare medici se non esistono pazienti
    o	Non deve essere possibile prenotare una visita se non esistono almeno un paziente e un medico
    o	Un medico può visitare fino a 3 pazienti diversi
    o	Non deve essere possibile prenotare una visita se non ci sono almeno un paziente senza un medico assegnato e un medico con disponibilità


