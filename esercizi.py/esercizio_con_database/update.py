import sqlite3

conn = sqlite3.connect('sondaggio.sqlite')
cur = conn.cursor()

query = '''
    UPDATE surveys
    SET name = 'Nesma'
    WHERE id = 2
'''

cur.execute(query)
conn.commit()
conn.close()