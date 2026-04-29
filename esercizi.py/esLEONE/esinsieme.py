#ESERCIZIO STEP-BY-STEP
#STEP 1: Scrivere uno script che prenda in input due stringhe, le concateni e stampi il risultato
#STEP 2: Scrivere uno script che prenda in input due numeri, li sommi e stampi il risultato
#STEP 3: Verificare con il costrutto if-else “coniugato” come necessario (ad esempio if-elif o if -else nidificati) se il risultato è positivo,
# negativo o uguale a zero. Stampare il risultato
#STEP 4: Aggiungere un ciclo che richieda più volte l'input all'utente, prevedere di interrompere la richiesta di input alla digitazione di un determinato input 
#(ad esempio “done”) e calcolare la somma di tutti i numeri digitati in input
#STEP 5: Aggiungere il costrutto Try-Except dove lo si ritiene necessario
#STEP 6: Spostare parte del codice in una o più funzioni che restituiscano dei valori. 
# Le istruzioni di print vanno previste nel corpo “principale” dello script (quindi non all’interno delle funzioni)
#STEP 7: Creare un file di testo che abbia ad ogni riga un numero, leggere il file e richiamare le funzioni generate allo step precedente. 
# L’obiettivo è sempre quello di calcolare la somma. Scrivere il risultato in un altro file di testo

def stringa ():
    stringa1 = input('scrivi la prima stringa: ')
    stringa2 = input('scrivi la seconda stringa: ')
    print(stringa1+stringa2)
def numeri(n1,n2):
        somma = n1+n2
        return somma
def sommaF ():
    if somma > 0 :
        print('positive')
    elif somma<0 :
        print('negative')
    else:
        print('the number is 0')
def somma1F ():        
    ins=0
    numero=0
    somma1=0
    while True :
        ins=input('inserire una variabile ')
        if type(ins)=='int':
            numero=ins
            somma1=somma1+numero
        elif ins=='done':
            print('la somma è: '+str(somma1))
            print('done')
            exit()
        else :
            print('inserire un numero o done')
            continue
stringa()
try:
    numero1 = int(input('scrivi il primo numero: '))
    numero2 = int(input('scrivi il secondo numero: '))
    numeri (numero1,numero2)
    print (numeri())
     
except:
    print('insert a fucking number')  



    