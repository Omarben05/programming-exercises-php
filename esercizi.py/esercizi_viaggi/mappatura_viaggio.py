from DB_utilities import DB_strumenti
import sqlite3
DBS=DB_strumenti()
DBS.connesione()
class Viaggio:
    
    def __init__(self,id_volo_andata,id_volo_ritorno,id_cliente,id_hotel,id_autonoleggio):
        self.id_volo_andata=id_volo_andata
        self.id_volo_ritorno=id_volo_ritorno
        self.id_cliente=id_cliente
        self.id_hotel=id_hotel
        self.id_autonoleggio=id_autonoleggio

      
    
    def salva_su_viaggio(self,DBS):

        DBS.cur.execute('insert into viaggio(id_volo_andata,id_volo_ritorno,id_cliente,id_hotel,id_autonoleggio) values (?, ?, ?, ?, ?)', 
        (self.id_volo_andata,self.id_volo_ritorno, self.id_cliente,self.id_hotel,self.id_autonoleggio))
        DBS.conn.commit()