#TRY-EXCEPT CON OGGETTO EXCEPTION

try:
	...
	...
	...
except Exception as e:
	print("errore")
	print(e)
	
	

#MATCH-CASE
scelta = input('inserisci la scelta')
match scelta:
	case "1":
		inserisci()
	case "2":
		aggiorna()
	case "3":
		vendi()
	case "4":
		exit()
	case _:
        print("valore non ammesso, inserisci un numero tra 1 e 4")
		

#FETCHALL
# Esecuzione di una query
cursor.execute("SELECT * FROM utenti")

# Recupero di tutti i risultati della query
risultati = cursor.fetchall()

# Stampa dei risultati
for riga in risultati:
    print(riga)
	
	

#IF CON ALIASING
# Supponiamo di avere una funzione che restituisce un valore
def calcola_valore():
    return 42

# Utilizzo dell'aliasing all'interno dell'istruzione if
if (val := calcola_valore()) > 40:
    print(f"Il valore {val} è maggiore di 40")
else:
    print(f"Il valore {val} non è maggiore di 40")