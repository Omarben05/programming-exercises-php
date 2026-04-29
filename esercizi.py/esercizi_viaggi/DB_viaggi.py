import sqlite3
from DB_utilities import DB_strumenti

conn = sqlite3.connect('viaggi.sqlite')
cur = conn.cursor()

cur.execute('''create TABLE IF NOT EXISTS voli(
            id_volo integer primary key autoincrement not null,
            ap_partenza varchar(20) not null,
            ap_arrivo varchar(20) not null,
            compagnia varchar(20)not null,
            giorno_orario_partenza varchar(30) not null
             )''')

cur.execute('''create TABLE IF NOT EXISTS hotel(
            id_hotel integer primary key autoincrement not null,
            nome_hotel varchar(50)not null,
            indirizzo varchar(20)not null
            )''')

cur.execute('''create TABLE IF NOT EXISTS autonoleggio(
            id_auto integer primary key autoincrement not null,
            targa varchar(20)not null,
            modello varchar(20)not null
            )''')
cur.execute('''create TABLE IF NOT EXISTS cliente(
            id_cliente integer primary key autoincrement not null,
            nome varchar(20)not null,
            cognome varchar(20)not null
            )''')
cur.execute('''create TABLE IF NOT EXISTS viaggio(
            id_viaggio integer primary key autoincrement not null,
            id_volo_andata integer not null,
            id_volo_ritorno integer not null,
            id_cliente integer not null, 
            id_hotel integer not null,
            id_autonoleggio integer not null,
            foreign key(id_volo_andata) references voli(id_volo),
            foreign key(id_volo_ritorno) references voli(id_volo),
            foreign key(id_hotel) references hotel(id_hotel),
            foreign key(id_autonoleggio) references autonoleggio(id_autonoleggio),
            foreign key(id_cliente) references cliente(id_cliente)
            )''')

conn.close()