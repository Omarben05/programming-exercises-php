#Riscrivi lo script del calcolo della retribuzione per attribuire ad un dipendente una maggiorazione oraria di 1,5 volte, per le ore di lavoro straordinario fatte oltre le 40.

#Es.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0


ore = float(input('scrivi le ore fatte: '))
paga = float(input('scrivi la paga oraria: '))
totale = 0.0

if ore <= 40:
    totale = ore * paga
    
else :
   totale = 40 * paga
   totale = totale + ((ore - 40) * paga * 1.5)
   
print('il tuo totale è: ' + str(totale)) 
    
