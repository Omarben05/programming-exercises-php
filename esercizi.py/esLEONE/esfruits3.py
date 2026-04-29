# 3.	Scrivi un ciclo while che continua a chiedere all'utente di inserire una chiave finché non viene inserita una chiave valida. Utilizza la funzione find_fruit per restituire il frutto corrispondente.
# 4.	Utilizza il metodo .get() per verificare se una chiave specifica (ad esempio, 3) è presente nel dizionario originale fruits_dict e stampa il frutto corrispondente o un messaggio di errore se la chiave non esiste.

def find_fruit(tuplaa):
    while True:
        frutto= input('Inserisci il nome di un frutto: ')
        for i in tuplaa:
            if i[0] == frutto:
                return i
                exit()
    print('Frutto non trovato')
    continue

elenco = {'arancia': 2, 'mela': 5, 'banana': 1}
fruits_tuple= list(elenco.items())
fruit= find_fruit(fruits_tuple)
print(fruit)
