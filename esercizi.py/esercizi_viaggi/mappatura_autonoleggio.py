from DB_utilities import DB_strumenti
import sqlite3
DBS=DB_strumenti()
DBS.connesione()
class Auto:
    
    def __init__(self,targa,modello):
        self.targa=targa
        self.modello=modello
      
    
    def salva_su_auto(self,DBS):

        DBS.cur.execute('insert into autonoleggio(targa,modello) values (?, ?)', 
        (self.targa, self.modello))
        DBS.conn.commit()