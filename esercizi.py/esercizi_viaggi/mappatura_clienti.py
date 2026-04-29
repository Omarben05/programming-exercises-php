from DB_utilities import DB_strumenti
import sqlite3
DBS=DB_strumenti()
DBS.connesione()
class Cliente:
    
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
      
    
    def salva_su_cliente(self,DBS):

        DBS.cur.execute('insert into cliente(nome,cognome) values (?, ?)', 
        (self.nome, self.cognome))
        DBS.conn.commit()