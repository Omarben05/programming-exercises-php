import sqlite3
class DB_strumenti:
    def __init__(self):
        self.conn=None
        self.cur=None
    def connesione(self):
        self.conn =sqlite3.connect('viaggi.sqlite')
        self.cur = self.conn.cursor()
    def elimina_volo(self,dvolo):
        self.cur.execute('''DELETE from voli where id_volo=? ''',(dvolo))
        self.conn.commit()
    def visualizza_volo(self,dvolo):
        visualizza=self.cur.execute('''SELECT * from voli where id_volo=? ''',(dvolo))
        self.conn.commit()
        return visualizza
    def elimina_hotel(self,dhotel):
        self.cur.execute('''DELETE from hotel where id_hotel=? ''',(dhotel))
        self.conn.commit()
    def visualizza_hotel(self,dhotel):
        visualizza=self.cur.execute('''SELECT * from hotel where id_hotel=? ''',(dhotel))
        self.conn.commit()
        return visualizza
    def elimina_auto(self,dauto):
        self.cur.execute('''DELETE from autonoleggio where id_auto=? ''',(dauto))
        self.conn.commit()
    def elimina_cliente(self,dcliente):
        self.cur.execute('''DELETE from cliente where id_cliente=? ''',(dcliente))
        self.conn.commit()
    def elimina_viaggio(self,dviaggio):
        self.cur.execute('''DELETE from viaggio where id_viaggio=? ''',(dviaggio))
        self.conn.commit()


 