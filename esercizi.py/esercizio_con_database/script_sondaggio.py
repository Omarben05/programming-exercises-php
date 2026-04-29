# chiededo al utente se vuole participare al sondaggio, salvo la risposta in input in una variabile.

import sqlite3
from survey import Survey

while True:
    domanda = input("Hey vuoi participare al sondaggio? ") 

# se la risposta e no stampiamo un output dove obblighiamo l'utente a partecipare.

    if (domanda.lower() not in ['si', 'sì']):
        print('Risposta invalida: usare si/sì o ti boccio')
        continue
    break

# creo un dizionario dove salvero le informazioni.

sondaggio = Survey()

# chiediamo l'informazione al utente in input:
# - nome: stringa;

while True:
    nome = input('Come ti chiami? ').strip().lower()
    response = sondaggio.set_name(nome)
    if response['successful']:
        break

    print(response['error_message'])

# - anni: intero;
while True:
    age = input('Quanti anni pensi che io abbia? ').strip()
    response = sondaggio.set_age(age)
    if response['successful']:
        break

    print(response['error_message'])

# - altezza: flot;
while True:
    altezza = input('Quanto pensi sia alto? ').strip()
    response = sondaggio.set_height(altezza)
    if response['successful']:
        break

    print(response['error_message'])


# - sposato: booleano;
while True:
    risposta = input('Pensi sia sposato? ').strip()
    response = sondaggio.set_married(risposta)
    if response['successful']:
        break

    print(response['error_message'])


# - materie: elenco di stringhe;

while True:
    mat = input('Quale materia insegno? (Scrivimi \'done\' per uscire) ').strip().lower()
    if mat == 'done':
        if sondaggio.get_subjects():
            break
        else:
            print('Fornire almeno una materia')
            continue

    response = sondaggio.set_subjects(mat)

    if response['successful']:
        continue

    print(response['error_message'])

# print(sondaggio.get_name(), sondaggio.get_age(), sondaggio.get_height(), sondaggio.get_married(), sondaggio.get_subjects())

# # apriamo il file in modalità scrittura se non esiste, altrimenti lo apriamo in modalità append e dopo averlo aperto salviamo i nostri dati.

# file = open('sondaggio.txt', 'a')

# file.write(f'{sondaggio.get_name()}, {sondaggio.get_age()}, {sondaggio.get_height()}, {sondaggio.get_married()}, {' --- '.join(sondaggio.get_subjects())}')
# file.write("\n")
# file.close()

conn = sqlite3.connect('sondaggio.sqlite')
cur = conn.cursor()

query = '''
    INSERT INTO surveys (name, age, height, marriage, subjects) VALUES
    (?, ?, ?, ?, ?)
'''

materie = sondaggio.get_subjects()
stringa_materie = ', '.join(materie)

tupla = (sondaggio.get_name(), sondaggio.get_age(), sondaggio.get_height(), sondaggio.get_married(), stringa_materie)

cur.execute(query, tupla)
conn.commit()
conn.close()
