from DB_utilities import DB_strumenti
import sqlite3
DBS=DB_strumenti()
DBS.connesione()
class Hotel:
    
    def __init__(self,nome_hotel,indirizzo):
        self.nome_hotel=nome_hotel
        self.indirizzo=indirizzo
      
    
    def salva_su_hotel(self,DBS):

        DBS.cur.execute('insert into hotel (nome_hotel,indirizzo) values (?, ?)', 
        (self.nome_hotel, self.indirizzo))
        DBS.conn.commit()