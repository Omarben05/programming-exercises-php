#Riscrivi lo script del capitolo precedente creando una funzione chiamata computegrade che accetta un punteggio come parametro e restituisce un voto sotto forma di stringa.

#Score Grade
'''>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Prova ripetutamente lo script per testare diversi valori in input.'''



def computergrade(valore) :
    if valore>0 and valore<1:
        if valore <0.6 :
            stringa = 'bad score'
        elif valore == 0.6 :
            stringa = 'bad score'
        elif valore>0.6 and valore<0.7 :
            stringa = 'bad score'
        elif valore == 0.7 :
            stringa = 'discreto' 
        elif valore>0.7 and valore<0.8 :
            stringa = 'discreto'
        elif valore == 0.8 :
            stringa = 'nice score' 
        elif valore == 0.9 :
            stringa = 'perfect score' 
        return stringa
    else :
        print('inserire un numero tra 0.0 e 1.0')
    
grado = float(input('digita un valore: '))
x = computergrade(grado)
print('score:',str(x))
        