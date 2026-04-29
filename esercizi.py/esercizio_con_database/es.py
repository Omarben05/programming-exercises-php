import sqlite3
conn = sqlite3.connect('ripasso.sqlite')

cur = conn.cursor()

query= ''' 
CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    prof TEXT,
    start_date DATE,
    end_date DATE,
    total_hours INTEGER
)
'''
cur.execute(query)
conn.commit() 

ins= '''
INSERT INTO subjects (name, prof, start_date, end_date, total_hours) VALUES
('sql','bogliaccino', '2025-01-10', '2025-02-28', '50'),
('python', 'leone', '2024-12-14', '2025-05-30', '89')

'''
cur.execute(ins)
conn.commit()


conn.close()

