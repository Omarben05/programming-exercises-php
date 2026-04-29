fname = input('enter a file name: ')
fhand = open(fname)
try:
 fhand= open(fname)
except:
 ('file non trovato')
count=0
somma=0
for line in fhand:
 count= int(line)
 somma= int(count+somma)
print(count)
 

