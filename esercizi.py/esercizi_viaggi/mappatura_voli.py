from DB_utilities import DB_strumenti
import sqlite3
DBS=DB_strumenti()
DBS.connesione()
class Voli:
    
    def __init__(self,ap_partenza,ap_arrivo,compagnia,giorno_orario_partenza):
        self.ap_partenza = ap_partenza
        self.ap_arrivo = ap_arrivo
        self.compagnia = compagnia
        self.giorno_orario_partenza=giorno_orario_partenza
    
    def salva_su_voli(self,DBS):

        DBS.cur.execute('insert into voli (ap_partenza,ap_arrivo,compagnia,giorno_orario_partenza) values ( ?, ?, ?, ?)', 
        (self.ap_partenza, self.ap_arrivo, self.compagnia, self.giorno_orario_partenza))
        DBS.conn.commit()