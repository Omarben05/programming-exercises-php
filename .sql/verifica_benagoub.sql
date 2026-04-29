create database biblioteche_verifica;
use biblioteche_verifica;

create table biblioteche (
codice int primary key,
nome_b varchar(100) not null,
indirizzo varchar(100) not null,
città varchar(100) not null,
telefono_b int not null,
apertura time not null);

create table libri (
isbn varchar(100) primary key,
titolo varchar(100) not null,
autore varchar(100) not null,
genere varchar(100),
anno_pubblicazione int);

create table copie (
codice int auto_increment primary key,
isbn varchar(100) not null,
codice_biblioteca int not null,
stato_conservazione varchar(100),
foreign key(isbn) references Libri(isbn) on delete cascade,
foreign key (codice_biblioteca) references Biblioteche(codice) on delete cascade);

create table utenti (
codice int auto_increment primary key,
nome_u varchar(100) not null,
cognome varchar(100) not null,
datanascita date not null,
telefono_u int not null);

create table iscrizioni (
codice_utente int,
codice_biblioteca int,
primary key (codice_utente, codice_biblioteca),
foreign key (codice_utente) references utenti(codice) on delete cascade,
foreign key (codice_biblioteca) references biblioteche(codice) on delete cascade);

create table prestiti (
codice int auto_increment primary key,
codice_utente int not null,
codice_copia int not null,
data_inizio date not null,
data_restituzione date,
foreign key (codice_utente) references utenti(codice) on delete cascade,
foreign key (codice_copia) references copie(codice) on delete cascade);

create table prenotazioni (
codice int auto_increment primary key,
codice_utente int not null,
isbn varchar(100) not null,
codice_biblioteca int not null,
data_prenotazione date not null,
foreign key (codice_utente) references utenti(codice) on delete cascade,
foreign key (isbn) references libri(isbn) on delete cascade,
foreign key (codice_biblioteca) references biblioteche(codice) on delete cascade);

create table eventi (
codice int auto_increment primary key,
titolo varchar(100) not null,
descrizione varchar(100),
data_evento date not null,
orario time not null,
codice_biblioteca int not null,
max_partecipanti int not null,
foreign key (codice_biblioteca) references biblioteche(codice) on delete cascade );

create table iscrizionieventi (
codice_evento int,
codice_utente int,
primary key (codice_evento, codice_utente),
foreign key (codice_evento) references eventi(codice) on delete cascade,
foreign key (codice_utente) references utenti(codice) on delete cascade);

insert into biblioteche (codice, nome_b, indirizzo, città, telefono_b, apertura) VALUES
(1, 'Biblioteca anna', 'via chieri 1', 'torino', '0111567892', '08:00'),
(2, 'biblioteca rosario', 'via lingotto 4', 'torino', '0111567894', '09:00'),
(3, 'biblioteca parlacino', 'via trapani 2', 'milano', '0111567992', '07:00');
insert into libri (isbn, titolo, autore, genere, anno_pubblicazione) VALUES
('9781234567890', 'Il Signore degli Anelli', 'J.R.R. Tolkien', 'Fantasy', 1954),
('9789876543210', '1984', 'George Orwell', 'Distopia', 1949),
('9781111111111', 'Il Nome della Rosa', 'Umberto Eco', 'Mistero', 1980),
('9782222222222', 'Harry Potter e la Pietra Filosofale', 'J.K. Rowling', 'Fantasy', 1997),
('9783333333333', 'Orgoglio e Pregiudizio', 'Jane Austen', 'Romanzo', 1813);
insert into copie (isbn, codice_biblioteca, stato_conservazione) VALUES
('9781234567890', 1, 'ottimo'),
('9781234567890', 2, 'buono'),
('9789876543210', 1, 'nuovo'),
('9781111111111', 3, 'discreto'),
('9782222222222', 1, 'Danneggiato'),
('9783333333333', 2, 'Buono');
insert into utenti (nome_u, cognome, datanascita, telefono_u) VALUES
('Mario', 'Rossi', '1990-05-15', '3331234567'),
('Luca', 'Bianchi', '1985-07-20', '3349876543'),
('Anna', 'Verdi', '1995-09-10', '3355678901'),
('Giulia', 'Neri', '2000-01-25', '3361112233'),
('Marco', 'Gialli', '1992-11-30', '3374455667');
insert into iscrizioni (codice_utente, codice_biblioteca) VALUES
(1, 1),
(2, 2),
(3, 3),
(1, 2), 
(4, 1),
(5, 2),
(5, 3);

insert into prestiti (codice_utente, codice_copia, data_inizio, data_restituzione) VALUES
(1, 1, '2024-02-01', NULL),
(2, 3, '2024-02-10', '2024-02-28'),
(3, 2, '2024-01-05',  NULL),
(4, 5, '2024-03-01', NULL),
(5, 6, '2024-02-20',  NULL);
insert into prenotazioni (codice_utente, isbn, codice_biblioteca, data_prenotazione) VALUES
(1, '9789876543210', 1, '2024-02-15'),
(2, '9781234567890', 2, '2024-02-18'),
(3, '9781111111111', 3, '2024-02-25'),
(4, '9782222222222', 1, '2024-03-01'),
(5, '9783333333333', 2, '2024-03-05');

insert into eventi (titolo, descrizione, data_evento, orario, codice_biblioteca, max_partecipanti) VALUES
('Presentazione libro', 'Incontro con lautore di un bestseller', '2024-03-15', '17:00', 1, 30),
('Workshop di scrittura', 'Laboratorio di scrittura creativa', '2024-04-10', '10:00', 2, 20),
('Conferenza sulla letteratura', 'Discussione sui classici della letteratura', '2024-05-20', '15:00', 3, 50);
insert into iscrizionieventi (codice_evento, codice_utente) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 1),
(3, 2),
(3, 3);
-- Query di Test
-- Elencare tutti i libri disponibili in una specifica biblioteca.
select l.isbn, l.titolo, l.autore, c.stato_conservazione
from copie c
join libri l on c.isbn = l.isbn
where c.codice_biblioteca = 1;
-- Trovare gli utenti con più di 3 libri in prestito attualmente.


-- Elencare i prestiti attivi di un determinato utente.

-- Elencare tutti gli eventi in una specifica biblioteca ordinati per data.
select *
from eventi
where codice_biblioteca = 1
order by data_evento;
-- Verificare quali libri hanno il maggior numero di prenotazioni.
select l.titolo, count(p.codice) as numero_prenotazioni
from prenotazioni p
join libri l on p.isbn = l.isbn
group by l.titolo
order by numero_prenotazioni desc;
-- Trovare i libri più frequentemente prestati nell’ultimo anno.

-- Elencare le biblioteche con il maggior numero di prestiti attivi.

-- Visualizzare gli utenti iscritti a più di una biblioteca.
select u.codice, u.nome_u, u.cognome, count(i.codice_biblioteca) as numero_iscrizioni
from utenti u
join iscrizioni i on u.codice = i.codice_utente
group by u.codice
having count(i.codice_biblioteca) > 1;
-- Trovare i libri danneggiati presenti in una biblioteca specifica.
select l.titolo, c.stato_conservazione
from copie c
join libri l on c.isbn = l.isbn
where c.stato_conservazione = 'danneggiato';
-- Trovare gli eventi con più iscritti e verificare se hanno ancora posti disponibili.


create database biblioteche_verifica;
