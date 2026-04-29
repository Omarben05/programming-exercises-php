try:
	fname = input('Enter the file name: ')
	fhand = open(fname)
except:
	print('digit another file, file not found') 
	exit()
count = 0
for line in fhand:
   if line.startswith('Subject:'):
    count = count + 1
print('There were', count, 'subject lines in', fname)