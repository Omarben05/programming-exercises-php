#Esercizio 6: Riscrivi il calcolo della tua retribuzione con gli straordinari pagati il 50% in più creando una funzione chiamata computepay che richieda i due parametri hours e rate. 
#(Hint: le ore di straordinario sono tutte quelle dopo le 40 "standard" settimanali)

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

def computepay (hours , rate) :
    totale = 0.0
    if ore <= 40:
        totale = ore * paga
        return totale
    else :
        totale = 40 * paga
        totale = totale + ((ore - 40) * paga * 1.5)
        print('il tuo totale è: ' + str(totale))
        return totale


ore = float(input('scrivi le ore fatte: '))
paga = float(input('scrivi la paga oraria: '))

computepay (ore , paga)






    

