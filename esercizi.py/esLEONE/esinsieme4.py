ins=0
numero=0
somma=0
while True : 
	ins=input('inserire una variabile ')
	if type(ins)=='int':
		numero=ins
		somma=somma+numero
	elif ins=='done':
		print('la somma è: '+str(somma))
		print('done')
		exit()
	else :
		print('inserire un numero o done')
		continue