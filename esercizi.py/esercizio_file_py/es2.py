try: 
	inp = input('enter a file name: ')
	fname = open.inp()
	
except:
	print('file non trovato', input)
	exit()

fname = inp.read()
for line in fname:
	if line.startswith('X-DSPAM-Confidence:'):
	 print(line)