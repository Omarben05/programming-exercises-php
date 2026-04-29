'''Scrivi un programma per richiedere un valore compreso tra 0.0 e 1.0. Se non è compreso nell’intervallo specificato, visualizza un messaggio di errore.
Se è compreso tra 0,0 e 1,0, visualizza un giudizio utilizzando la seguente tabella:'''

valore = float(input('digita un valore tra 0.0 e 1.0: '))


if valore>0 and valore<1:
    
    if valore <0.6 :
        print(valore , 'F')
    elif valore == 0.6 :
        print(valore , 'D')
    elif valore>0.6 and valore<0.7 :
        print(valore, 'D')
    elif valore == 0.7 :
        print(valore , 'C') 
    elif valore>0.7 and valore<0.8 :
        print(valore , 'C')
    elif valore == 0.8 :
        print(valore , 'B') 
    elif valore == 0.9 :
        print(valore , 'A') 
else :
    print('inserire un numero tra 0.0 e 1.0')
    
