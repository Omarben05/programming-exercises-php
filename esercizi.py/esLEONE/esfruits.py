# #1.	Partendo dalla tupla di tuple fruits_tuple creata nel terzo esercizio, scrivi una funzione chiamata find_fruit che accetta una chiave come argomento e restituisce il frutto corrispondente. 
# Utilizza try-except per gestire le chiavi non valide.
# 2.	Scrivi un ciclo for che itera su fruits_tuple e stampa ogni coppia chiave-valore.

def find_fruit(tuplaa,frutto):
    for item in tuplaa:
        if item[0] == frutto:
            return item
    print('Frutto non trovato')
    return None
def es2(tupla):
    for fruit, i in tupla:
        print('Frutto:', fruit, ',', 'quantità:', i )
elenco = {'arancia': 2, 'mela': 5, 'banana': 1}
fruits_tuple= list(elenco.items())
fdaTrovare = input('Inserisci un frutto: ')
fruit= find_fruit(fruits_tuple, fdaTrovare)
print(fruit)


    