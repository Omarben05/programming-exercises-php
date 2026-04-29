# Scrivere un secondo programma in Python che legga il file di output prodotto dal primo programma e generi statistiche sulle informazioni raccolte. Le statistiche devono includere:
# •	Numero totale di persone registrate.
# •	Elenco dei nomi delle persone con l’indicazione di quante persone con quel nome hanno partecipato al sondaggio (es. “Mario 2, Giovanni 1, Mimmo 6”)
# •	Età media inserita dagli utenti
# •	Altezza media inserita dagli utenti
# •	Percentuale di persone che pensano che sia sposato e che pensano che non lo sia (es. “40% pensa che sia sposato, 60% pensa che non sia sposato”).
# •	Elenco delle materie inserite e il numero di volte che ciascuna materia è stata menzionata
import sqlite3
from survey import Survey
from statistic import Statistic

sondaggi = []

conn = sqlite3.connect('sondaggio.sqlite')
cur = conn.cursor()

query = '''
    SELECT name, age, height, marriage, subjects
    FROM surveys
'''

cur.execute(query)
for row in cur:
    attributi = {
        'name': row[0],
        'age': row[1],
        'height': row[2],
        'married': bool(row[3]),
        'subjects': row[4].split(', ')
    }

    sondaggio = Survey(attributi)
    sondaggi.append(sondaggio)
    
if sondaggi:
    stats = Statistic(sondaggi)
    print('Partecipanti totali:', stats.get_total_participants())
    print('Media età:', stats.get_average_age())
    print('Media altezza:', stats.get_average_height())
    print(f'Sposato? sì {stats.get_yes_no_counts()['True']}%, no {stats.get_yes_no_counts()['False']}%')
    print('\nConteggi nomi:')
    nomi = stats.get_name_counts().items()
    for name, conteggio in nomi:
        print(f'{name}: {conteggio}')

    print('\nConteggi materie:')
    materie = stats.get_subject_counts().items()
    for materia, conteggio in materie:
        print(f'{materia}: {conteggio}')
else:
    print('Non ci sono sondaggi da cui trarre statistiche')