fname= input('Inserire un nome per il file: ')
fhand= open(fname)

a= dict()
t= list()

for line in fhand:
    words= line.split()
    if len(words)>2 and words[0] == 'From': 
     ora=words[5].split(':')
     a[ora[0]]= a.get(ora[0],0) +1
print(a)
for key in a:
    b=(a[key],key)
    t.append(b)
    
t.sort(reverse=True)
print(t[:1])