fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  ('file non trovato o inesistente')
numeron=0
numerof=0.0
somman=0
sommaf=0.0
count=0
counts=0
countn=0
countf=0
stringhe=''
for line in fhand:
	count=count+1
	if line.startswith('String:'):
		counts=counts+1
		spazio=line.find(' ')
		stringhe=stringhe+(line[spazio+1:])+'\n'
	if line.startswith('Number:'):
		countn=countn+1
		spazio=line.find(' ')
		numeron=numeron+int(line[spazio+1:])
	if line.startswith('Float:'):
		countf=countf+1
		spazio=line.find(' ')
		numerof=numerof+float(line[spazio+1:])
median=numeron/countn
mediaf=numerof/countf
fout=open ('tes8.txt','w')
fout.write('le rige totali sono: '+str(count)+'\n')
fout.write('le rige totali di stringe sono: '+str(counts)+'\n')
fout.write('le rige totali di numeri interi sono: '+str(countn)+'\n')
fout.write('le rige totali di numeri decimali sono: '+str(countf)+'\n')
fout.write('la somma totale degli interi è: '+str(somman)+'\n')
fout.write('la somma totale dei decimali è: '+str(sommaf)+'\n')
fout.write('la media degli interi è: '+str(median)+'\n')
fout.write('la media dei decimali è: '+str(mediaf)+'\n')
fout.write(stringhe)