import sqlite3
conn =  sqlite3.connect('ripasso.sqlite')
cur = conn.cursor()

query= '''
SELECT * FROM subjects ;
'''

cur.execute(query)

for row in cur :
    print(row)

conn.close()


