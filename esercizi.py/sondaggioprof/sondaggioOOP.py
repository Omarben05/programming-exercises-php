from classeProf import Prof 

# liste di possibili risposte 
sposato_si = ['si', 's', 'vero', 'true', '1', 'yes', 'y', 'ya', 'oui']    
sposato_no = ['no', 'n', 'none', 'nope', '0', 'nein', 'false']


def nome():
    while True:
        try:
            n = input("Inserisci il tuo nome: ").capitalize()  # input del nome del partecipante
            break
        except ValueError:
            print("Errore: Devi inserire un nome valido.")
    return n

def età():
    while True:
        try:
            eta = int(input("Quanti anni pensi che abbia? "))  # input dell'età
            break
        except ValueError:
            print("Errore: Devi inserire un numero intero per l'età.")
    return eta

def altezza():
    while True:
        try:
            alt = float(input("Quanto pensi che sia alto (in m)? "))
            break
        except ValueError:
            print("Errore: Devi inserire un numero decimale per l'altezza.")
    return alt

def sposato():
    while True:
        stato = input("Pensi che sia sposato?: ").strip().lower()
        if stato in sposato_si:
            return "True"
        elif stato in sposato_no:
            return "False"
        else:
            print("Errore: Dai una risposta più sensata.")

def materie():
    while True:
        materie_input = input("Quali materie credi che insegni? (separate da virgola): ").strip()
        if materie_input:
            break
        else:
            print("Errore: Devi inserire almeno una materia.")

    # Converte la stringa in una lista di materie separate da ;
    materie_lista = ""
    for materia in materie_input.split(','):
        materia = materia.strip()
        if materia:
            if materie_lista:
                materie_lista += ";"
            materie_lista += materia
    return materie_lista

    
n = nome()
e = età()
a = altezza()
s = sposato()
m = materie()

with open('sondaggio.txt', 'a') as file:   # apertura file in modalità append
    file.write(n + ",")
    file.write(str(e) + ",")
    file.write(str(a) + ",")
    file.write(s + ",")
    file.write(m + "\n")

persona1 = Prof(n, e, a, s, m)
print(persona1.get_nome(),persona1.get_età(), persona1.get_altezza(), persona1.get_sposato(),persona1.get_materie())

print("Dati salvati correttamente!")


