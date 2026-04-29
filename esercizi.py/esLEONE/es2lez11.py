# Esercizio 2: Scrivi un programma per trovare le stringhe contenenti

# New Revision: 39772

# provvedendo ad estrarre il numero da ciascuna tramite l’uso del metodo findall() e di una espressione regolare. Calcola e visualizza la media dei numeri.

# COSA HO FATTO IO
# import re
 
# fhand= open('mbox.txt')

# count= 0 
# for line in fhand:
#     line= line.rstrip()
#     if re.search('^New Revision: [0-18]+', line):
#         count= count + 1

# revisione = re.findall('^New Revision: ([13-18])', line) 

# media = sum(revisione)/count
# print('La media delle revisioni è:', media) 

#COME VA FATTO
import re
fhand= open('mbox.txt')
count= 0
somma= 0.0
for line in fhand:
    line= line.rstrip()
    x = re.findall('^New Revision: [0-9]+1', line)
    if len(x) >0:
            y= 0.0
    for i in range(len(x)):
            y= float(x[i])
    somma= somma + y
    count= count + 1
media= somma/count
print('La media delle revisioni è:', media)