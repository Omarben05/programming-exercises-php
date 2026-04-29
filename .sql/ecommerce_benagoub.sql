
use ecommerce;


create table prodotti (
	codp varchar(10) primary key,
    nome varchar(100) not null,
    colore varchar(50),
    taglia varchar(10),
    magazzino varchar(10)
    );
create table fornitori (
	codf varchar(10) primary key,
    nome varchar(100) not null,
    nSoci int,
    sede varchar(100)
);
create table clienti (
	cod_Cliente varchar(10) primary key,
    nome varchar(100) not null,
    email varchar(100),
    data_registrazione date default (current_date)
);
create table prodottiArchivio (
	codp varchar(10) primary key,
    nome varchar(100) not null,
    colore varchar(50),
    taglia varchar(10)
);
create table ordini (
	codOrdine varchar(10) primary key,
    cod_Cliente varchar(10) not null,
    dataOrdine date not null,
    foreign key (cod_cliente) references clienti(cod_cliente)
);
create table vendite (
	codVendita varchar(10) primary key,
    codprodotto varchar(10) not null,
    quantita int not null,
    totale decimal(10,2),
    foreign key (codprodotto) references prodotti(codp)
);
create table fornitoriProdotti (
	codf varchar(10) not null,
	codp varchar(10) not null,
    qta int not null,
    primary key (codf, codp),  -- chiave primaria composta
    foreign key (codf) references fornitori(codf), 
    foreign key (codp) references prodotti(codp)
);
create table ordiniTemp (
	codOrdine varchar(10) primary key,
    cod_Cliente varchar(10) not null,
    data_Ordine date not null
    );
    

-- 1. Inserire record nella tabella Prodotti
INSERT INTO Prodotti (CodP, Nome, Colore, Taglia, Magazzino) VALUES
('P001', 'Maglietta', 'Rosso', 'M', 'MZ01'),
('P002', 'Pantaloni', 'Blu', 'L', 'MZ02'),
('P003', 'Scarpe', 'Nero', '42', 'MZ03'),
('P004', 'Cappello', 'Verde', 'Unica', 'MZ01'),
('P005', 'Giacca', 'Grigio', 'XL', 'MZ02'),
('P006', 'Zaino', 'Rosso', NULL, 'MZ03'),
('P007', 'Occhiali', 'Nero', 'Unica', 'MZ01'),
('P008', 'Guanti', 'Bianco', 'M', 'MZ02'),
('P009', 'Cintura', 'Marrone', 'L', 'MZ03'),
('P010', 'Orologio', 'Oro', 'Unica', 'MZ01');
-- 2. Inserire record nella tabella Fornitori
INSERT INTO Fornitori (CodF, Nome, NSoci, Sede) VALUES
('F001', 'Forniture Srl', 10, 'Milano'),
('F002', 'Prodotti Spa', 15, 'Roma'),
('F003', 'Servizi & Co.', 8, 'Napoli'),
('F004', 'Global Supply', 20, 'Torino'),
('F005', 'Tech Parts', 5, 'Bologna'),
('F006', 'Fashion Line', 12, 'Firenze'),
('F007', 'Home Goods', 6, 'Verona'),
('F008', 'Quick Deliver', 9, 'Genova'),
('F009', 'Market Solutions', 7, 'Palermo'),
('F010', 'Green Supply', 4, 'Venezia');
-- 3. Inserire record nella tabella Clienti
INSERT INTO Clienti (cod_Cliente, Nome, Email, Data_Registrazione) VALUES
('C001', 'Mario Rossi', 'mario.rossi@example.com', '2024-01-01'),
('C002', 'Anna Bianchi', 'anna.bianchi@example.com', '2024-01-02'),
('C003', 'Luca Verdi', 'luca.verdi@example.com', '2024-01-03'),
('C004', 'Giulia Neri', 'giulia.neri@example.com', '2024-01-04'),
('C005', 'Marco Gialli', 'marco.gialli@example.com', '2024-01-05'),
('C006', 'Elisa Blu', 'elisa.blu@example.com', '2024-01-06'),
('C007', 'Francesco Viola', 'francesco.viola@example.com', '2024-01-07'),
('C008', 'Chiara Marrone', 'chiara.marrone@example.com', '2024-01-08'),
('C009', 'Alessio Rosa', 'alessio.rosa@example.com', '2024-01-09'),
('C010', 'Sara Arancio', 'sara.arancio@example.com', '2024-01-10');
-- 4. Inserire record nella tabella ProdottiArchivio
INSERT INTO ProdottiArchivio (CodP, Nome, Colore, Taglia) VALUES
('A001', 'Maglietta Vintage', 'Rosso', 'M'),
('A002', 'Pantaloni Retrò', 'Blu', 'L'),
('A003', 'Scarpe Classiche', 'Nero', '42'),
('A004', 'Cappello d\'Epoca', 'Verde', 'Unica'),
('A005', 'Giacca Pesante', 'Grigio', 'XL'),
('A006', 'Zaino Montagna', 'Rosso', NULL),
('A007', 'Occhiali Retrò', 'Nero', 'Unica'),
('A008', 'Guanti Termici', 'Bianco', 'M'),
('A009', 'Cintura di Cuoio', 'Marrone', 'L'),
('A010', 'Orologio Vintage', 'Oro', 'Unica');
-- 5. Inserire record nella tabella Ordini
INSERT INTO Ordini (CodOrdine, Cod_Cliente, Data_Ordine) VALUES
('O001', 'C001', '2024-01-11'),
('O002', 'C002', '2024-01-12'),
('O003', 'C003', '2024-01-13'),
('O004', 'C004', '2024-01-14'),
('O005', 'C005', '2024-01-15'),
('O006', 'C006', '2024-01-16'),
('O007', 'C007', '2024-01-17'),
('O008', 'C008', '2024-01-18'),
('O009', 'C009', '2024-01-19'),
('O010', 'C010', '2024-01-20');
-- 6. Inserire record nella tabella Vendite
INSERT INTO Vendite (CodVendita, CodProdotto, Quantita, Totale) VALUES
('V001', 'P001', 10, 159.90),
('V002', 'P002', 5,  149.95),
('V003', 'P003', 8, 399.92),
('V004', 'P004', 12,  119.88),
('V005', 'P005', 6, 539.94),
('V006', 'P006', 3, 179.97),
('V007', 'P007', 15, 299.85),
('V008', 'P008', 10, 129.90),
('V009', 'P009', 4, 99.96),
('V010', 'P010', 2, 399.98);
-- 7. Inserire record nella tabella FornitoriProdotti
INSERT INTO FornitoriProdotti (CodF, CodP, Qta) VALUES
('F001', 'P001', 100),
('F002', 'P002', 200),
('F003', 'P003', 150),
('F004', 'P004', 250),
('F005', 'P005', 300),
('F006', 'P006', 50),
('F007', 'P007', 80),
('F008', 'P008', 70),
('F009', 'P009', 90),
('F010', 'P010', 60);
-- 8. Inserire record nella tabella OrdiniTemp
INSERT INTO OrdiniTemp (CodOrdine, Cod_Cliente, Data_Ordine) VALUES
('T001', 'C001', '2024-01-21'),
('T002', 'C002', '2024-01-22'),
('T003', 'C003', '2024-01-23'),
('T004', 'C004', '2024-01-24'),
('T005', 'C005', '2024-01-25'),
('T006', 'C006', '2024-01-26'),
('T007', 'C007', '2024-01-27'),
('T008', 'C008', '2024-01-28'),
('T009', 'C009', '2024-01-29'),
('T010', 'C010', '2024-01-30');


select codordine from ordinitemp;


select * from prodotti;

select nome from clienti;

insert into prodotti values ('T001', 'nomignolo', 'rosso', 'xxl', 'casa tua');

update prodotti
set colore = 'rosso'
where codP = 'P001' ; 

set sql_safe_updates = 0;


insert into prodotti values
('I002', 'omar', 'rosso', '5', 'torino'),
('I002', 'guido', 'verde', '15', 'milano'),
('I002', 'jani', 'arancione', '3', 'tirana')
;





-- Esegui 10 esercizi di INSERT in SQL per esercitarsi con la sintassi e i concetti.

-- 1. Inserire un singolo record
-- Inserire un prodotto nella tabella Prodotti:
INSERT INTO Prodotti (CodP, Nome, Colore, Taglia, Magazzino)
VALUES ('P001', 'Maglia', 'blu', 'M', 'MZ001');
-- 2. Inserire più record in una sola istruzione
-- Inserire più fornitori nella tabella Fornitori: `
INSERT INTO Fornitori (CodF, Nome, NSoci, Sede)
VALUES 
    ('F001', 'Fornitore 12', 1, 'Torino'),
    ('F002', 'Fornitore 35', 3, 'Bergamo'),
    ('F003', 'Fornitore 20', 6, 'Firenze');
-- 3. Inserire un record parziale
-- Inserire un cliente con alcuni campi lasciati nulli:
INSERT INTO Clienti (Cod_Cliente, Nome, Email)
VALUES ('C001', 'Mario Rossi', NULL);
-- 4. Inserire un record calcolato da un'altra tabella
-- Copiare un prodotto dalla tabella Prodotti alla tabella ProdottiArchivio:
INSERT INTO ProdottiArchivio (CodP, Nome, Colore, Taglia)
SELECT CodP, Nome, Colore, Taglia FROM Prodotti WHERE CodP = 'P001';
-- 5. Inserire una riga con una sottoquery
-- Inserire un ordine per il cliente più recente:
INSERT INTO Ordini (CodOrdine, Cod_Cliente, Data_Ordine)
SELECT 'O001', Cod_Cliente, GETDATE()
FROM Clienti
WHERE Data_Registrazione = (SELECT MAX(Data_Registrazione) FROM Clienti);
-- 6. Inserire un record con valori default
-- Inserire un fornitore con i valori predefiniti per alcuni campi:
INSERT INTO Fornitori (CodF, NomeF)
VALUES ('F004', 'Fornitore D');
-- 7. Inserire dati con valori calcolati
-- Inserire un record nella tabella Vendite calcolando il totale:
INSERT INTO Vendite (CodVendita, CodProdotto, Quantita,  Totale)
VALUES ('V001', 'P002', 5, 5 * 20);
-- 8. Inserire dati duplicati con modifiche
-- Duplicare un prodotto con un nuovo codice e colore:
INSERT INTO Prodotti (CodP, Nome, Colore, Taglia, Magazzino)
SELECT 'P002', Nome, 'blu', Taglia, Magazzino
FROM Prodotti WHERE CodP = 'P001';
-- 9. Inserire dati nella tabella di associazione
-- Aggiungere una relazione tra fornitori e prodotti:
INSERT INTO FornitoriProdotti (CodF, CodP, Qta)
VALUES ('F001', 'P003', 100);
-- 10. Inserire dati provenienti da una tabella di log
-- Inserire tutti i record da una tabella temporanea a una tabella definitiva:
INSERT INTO Ordini (CodOrdine, Cod_Cliente, Data_Ordine)
SELECT CodOrdine, Cod_Cliente, Data_Ordine FROM OrdiniTemp;

-- Esegui 10 esercizi di UPDATE in SQL per esercitarsi con la sintassi e i concetti.

-- 1. Aggiornare il colore dei prodotti con il codice "P001" in "rosso"
UPDATE Prodotti
SET Colore = 'rosso'
WHERE CodP = 'P001';
-- 2. Incrementare il numero di soci di tutti i fornitori con sede a "Milano" di 2
update fornitori
set nsoci = nsoci + 2
where sede = 'Milano';
-- 3. Aggiornare il magazzino del prodotto "P002" a "MZ002"
UPDATE Prodotti
SET Magazzino = 'MZ002'
WHERE CodP = 'P002';
-- 4. Ridurre del 10% la quantità disponibile per tutti i prodotti forniti da "F001"
UPDATE FornitoriProdotti
SET Qta = Qta * 0.9
WHERE CodF = 'F001';
-- 5. Impostare il colore dei prodotti senza un colore definito a "bianco"
UPDATE Prodotti
SET Colore = 'bianco'
WHERE Colore IS NULL;
-- 6. Cambiare l'indirizzo di tutti i fornitori con codice "F002" in "Via Roma, 10"
UPDATE Fornitori
SET Sede = 'Via Roma, 10'
WHERE CodF = 'F002';
-- 7. Impostare la quantità a 0 per i prodotti mai forniti da alcun fornitore
UPDATE Prodotti
SET Magazzino = 'Non fornito'
WHERE CodP NOT IN (SELECT DISTINCT CodP FROM FornitoriProdotti);
-- 8. Aggiornare la sede dei fornitori con meno di 3 soci a "Sede Sconosciuta"
UPDATE Fornitori
SET Sede = 'Sede Sconosciuta'
WHERE NSoci < 3;
-- 9. Cambiare la taglia di tutti i prodotti di colore "verde" a "L"
UPDATE Prodotti
SET Taglia = 'L'
WHERE Colore = 'verde';
-- 10. Aggiornare il nome dei fornitori che hanno fornito almeno un prodotto con quantità superiore a 100 in "Fornitore Premium"
UPDATE Fornitori
SET Nome = 'Fornitore Premium'
WHERE CodF IN (
    SELECT CodF
    FROM FornitoriProdotti
    WHERE Qta > 100 );
    
    
-- 1. Eliminare i prodotti con magazzino "MZ003"
delete from prodotti
where magazzino = 'MZ003';
-- 2. Rimuovere tutti i fornitori con sede a "Napoli"
delete from fornitori
where sede = 'Napoli';
-- 3. Eliminare tutte le relazioni prodotto-fornitore per il prodotto con codice "P004"
delete from fornitoriprodotti
where codp= 'P004';
-- 4. Rimuovere tutti i prodotti con colore "nero"
DELETE FROM Prodotti
WHERE Colore = 'nero';
-- 5. Eliminare tutti i fornitori con meno di 5 soci
DELETE FROM Fornitori
WHERE NSoci < 5;
-- 6. Eliminare le relazioni prodotto-fornitore per i fornitori con codice "F003"
DELETE FROM FornitoriProdotti
WHERE CodF = 'F003';
-- 7. Eliminare tutti i prodotti mai forniti da alcun fornitore
DELETE FROM Prodotti
WHERE CodP NOT IN (SELECT DISTINCT CodP FROM FornitoriProdotti);
-- 8. Rimuovere tutti i fornitori che non hanno fornito prodotti
DELETE FROM Fornitori
WHERE CodF NOT IN (SELECT DISTINCT CodF FROM FornitoriProdotti);
-- 9. Eliminare tutti i prodotti con quantità inferiore a 10 in qualsiasi relazione prodotto-fornitore
DELETE FROM FornitoriProdotti
WHERE Qta < 10;
-- 10. Rimuovere tutti i prodotti di taglia "S" e colore "giallo"
DELETE FROM Prodotti
WHERE Taglia = 'S' AND Colore = 'giallo';

-- 1. Selezionare tutti i dettagli dei prodotti di colore rosso
SELECT * 
FROM Prodotti
WHERE Colore = 'rosso';
-- 2. Trovare i nomi e le sedi dei fornitori con più di 5 soci
SELECT Nome, Sede
FROM Fornitori
WHERE NSoci > 5;
-- 3. Trovare il nome e l'email dei clienti registrati negli ultimi 30 giorni
SELECT Nome, Email
FROM Clienti ;
-- WHERE Data_Registrazione >= CURRENT_DATE - INTERVAL '30 days' ;
-- 4. Calcolare il totale delle vendite per ogni prodotto
SELECT CodProdotto, SUM(Totale) AS TotaleVendite
FROM Vendite
GROUP BY CodProdotto;
-- 5. Recuperare i dettagli dei fornitori che forniscono almeno un prodotto di colore "verde"
SELECT DISTINCT F.CodF, F.NomeF, F.Sede
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
JOIN Prodotti P ON FP.CodP = P.CodP
WHERE P.Colore = 'verde';
-- 6. Trovare i nomi dei clienti che hanno effettuato ordini
SELECT DISTINCT C.Nome
FROM Clienti C
JOIN Ordini O ON C.Cod_Cliente = O.Cod_Cliente;
-- 7. Visualizzare i prodotti mai forniti da alcun fornitore
SELECT P.NomeP
FROM Prodotti P
LEFT JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
WHERE FP.CodP IS NULL;
-- 8. Trovare i fornitori che forniscono almeno due prodotti diversi
SELECT CodF
FROM FornitoriProdotti
GROUP BY CodF
HAVING COUNT(DISTINCT CodP) >= 2;
-- 9. Recuperare i dettagli delle vendite per prodotti il cui prezzo unitario è maggiore della media
SELECT *
FROM Vendite
WHERE PrezzoUnitario > (SELECT AVG(PrezzoUnitario) FROM Vendite);
-- 10. Trovare i prodotti venduti esclusivamente nel magazzino "MZ001"
SELECT P.NomeP
FROM Prodotti P
WHERE P.Magazzino = 'MZ001'
AND NOT EXISTS (
    SELECT 1
    FROM Vendite V
    WHERE V.CodProdotto = P.CodP AND P.Magazzino != 'MZ001'
);


-- 1. Selezionare il nome e il prezzo aumentato del 10% per tutti i prodotti
SELECT NomeP, Prezzo * 1.1 AS NuovoPrezzo
FROM Prodotti;
-- 2. Trovare i prodotti con un prezzo tra 50 e 100 (inclusi)
SELECT NomeP, Prezzo
FROM Prodotti
WHERE Prezzo BETWEEN 50 AND 100;
-- 3. Visualizzare i fornitori con un numero di soci maggiore o uguale a 10
SELECT NomeF, NSoci
FROM Fornitori
WHERE NSoci >= 10;
-- 4. Calcolare la quantità totale fornita per ogni prodotto
SELECT CodP, SUM(Qta) AS TotaleQuantita
FROM FornitoriProdotti
GROUP BY CodP;
-- 5. Trovare i fornitori con il nome che inizia con "A"
SELECT Nome
FROM Fornitori
WHERE Nome LIKE 'A%';
-- 6. Mostrare tutti i prodotti che non sono né rossi né gialli
SELECT NomeP, Colore
FROM Prodotti
WHERE Colore NOT IN ('rosso', 'giallo');
-- 7. Trovare i fornitori che si trovano in città diverse da "Milano"
SELECT NomeF, Sede
FROM Fornitori
WHERE Sede <> 'Milano';
-- 8. Calcolare la media delle quantità fornite da ciascun fornitore
SELECT CodF, AVG(Qta) AS MediaQuantita
FROM FornitoriProdotti
GROUP BY CodF;
-- 9. Selezionare tutti i fornitori che forniscono almeno un prodotto in quantità superiore a 50
SELECT DISTINCT CodF
FROM FornitoriProdotti
WHERE Qta > 50;
-- 10. Visualizzare i prodotti con prezzo maggiore di 20 e in magazzini diversi da "MZ001"
SELECT NomeP, Prezzo, Magazzino
FROM Prodotti
WHERE Prezzo > 20 AND Magazzino <> 'MZ001';

-- 1. Mostrare il nome dei prodotti e i nomi dei fornitori che li forniscono
SELECT P.NomeP, F.Nome
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
JOIN Fornitori F ON FP.CodF = F.CodF;
-- 2. Trovare i fornitori che non forniscono alcun prodotto (LEFT JOIN con condizione NULL)
SELECT F.Nome
FROM Fornitori F
LEFT JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
WHERE FP.CodP IS NULL;
-- 3. Calcolare la quantità totale fornita per ogni prodotto e visualizzare anche i prodotti che non sono forniti (LEFT JOIN)
SELECT P.NomeP, COALESCE(SUM(FP.Qta), 0) AS TotaleQuantita
FROM Prodotti P
LEFT JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP;

-- 4. Visualizzare i fornitori che forniscono prodotti con quantità maggiore di 50
SELECT F.Nome, P.NomeP, FP.Qta
FROM FornitoriProdotti FP
JOIN Fornitori F ON FP.CodF = F.CodF
JOIN Prodotti P ON FP.CodP = P.CodP
WHERE FP.Qta > 50;
-- 5. Trovare i prodotti non forniti da nessun fornitore
SELECT P.NomeP
FROM Prodotti P
LEFT JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
WHERE FP.CodF IS NULL;
-- 6. Trovare i fornitori che forniscono solo prodotti di colore "rosso"
SELECT DISTINCT F.Nome
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
JOIN Prodotti P ON FP.CodP = P.CodP
WHERE P.Colore = 'rosso'
  AND F.CodF NOT IN (
      SELECT FP2.CodF
      FROM FornitoriProdotti FP2
      JOIN Prodotti P2 ON FP2.CodP = P2.CodP
      WHERE P2.Colore <> 'rosso'
  );
-- 7. Visualizzare i fornitori che forniscono almeno due prodotti diversi
SELECT F.Nome
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
GROUP BY F.CodF, F.Nome
HAVING COUNT(DISTINCT FP.CodP) >= 2;
-- 8. Trovare i prodotti forniti solo da un unico fornitore
SELECT P.NomeP
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP
HAVING COUNT(DISTINCT FP.CodF) = 1;
-- 9. Trovare i fornitori che forniscono prodotti con quantità media superiore a 30
SELECT F.Nome
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
GROUP BY F.CodF, F.Nome
HAVING AVG(FP.Qta) > 30;
-- 10. Visualizzare i prodotti e il numero di fornitori che li forniscono
SELECT P.NomeP, COUNT(DISTINCT FP.CodF) AS NumeroFornitori
FROM Prodotti P
LEFT JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP;

-- 1. Contare il numero totale di prodotti disponibili
SELECT COUNT(*) AS NumeroProdotti
FROM Prodotti;
-- 2. Calcolare la quantità totale fornita per ogni prodotto
SELECT P.NomeP, SUM(FP.Qta) AS QuantitaTotale
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP;
-- 3. Determinare la quantità media di prodotti forniti da ciascun fornitore
SELECT F.Nome, AVG(FP.Qta) AS QuantitaMedia
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
GROUP BY F.CodF, F.Nome;
-- 4. Calcolare il numero di fornitori per ciascun prodotto
SELECT P.NomeP, COUNT(DISTINCT FP.CodF) AS NumeroFornitori
FROM Prodotti P
LEFT JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP;
-- 5. Trovare il prodotto con la quantità massima fornita
SELECT P.NomeP, MAX(FP.Qta) AS QuantitaMassima
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP
ORDER BY QuantitaMassima DESC
LIMIT 1;
-- 6. Determinare la quantità totale fornita per ciascun colore di prodotto
SELECT P.Colore, SUM(FP.Qta) AS QuantitaTotale
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.Colore;
-- 7. Contare il numero di prodotti forniti da ogni fornitore
SELECT F.Nome, COUNT(DISTINCT FP.CodP) AS NumeroProdotti
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
GROUP BY F.CodF, F.Nome;
-- 8. Calcolare il numero medio di soci dei fornitori per città
SELECT F.Sede, AVG(F.NSoci) AS NumeroMedioSoci
FROM Fornitori F
GROUP BY F.Sede;
-- 9. Trovare i prodotti con una quantità totale fornita superiore a 100
SELECT P.NomeP, SUM(FP.Qta) AS QuantitaTotale
FROM Prodotti P
JOIN FornitoriProdotti FP ON P.CodP = FP.CodP
GROUP BY P.CodP, P.NomeP
HAVING SUM(FP.Qta) > 100;
-- 10. Determinare il numero di prodotti forniti e la quantità totale fornita da fornitori con più di 5 soci
SELECT F.Nome, COUNT(DISTINCT FP.CodP) AS NumeroProdotti, SUM(FP.Qta) AS QuantitaTotale
FROM Fornitori F
JOIN FornitoriProdotti FP ON F.CodF = FP.CodF
WHERE F.NSoci > 5
GROUP BY F.CodF, F.Nome;

-- Esercizio 1: Convertire il testo in maiuscolo
-- Descrizione: Seleziona i nomi dei clienti in maiuscolo.


SELECT UPPER(nome) AS nome_maiuscolo, cognome 
FROM clienti;
-- Esercizio 2: Convertire il testo in minuscolo
-- Descrizione: Seleziona i cognomi dei clienti in minuscolo.


SELECT LOWER(cognome) AS cognome_minuscolo, nome 
FROM clienti;
-- Esercizio 3: Concatenare stringhe
-- Descrizione: Crea una colonna che mostri il nome completo (nome + cognome).


SELECT CONCAT(nome, ' ', cognome) AS nome_completo 
FROM clienti;
-- Esercizio 4: Estrarre una parte di testo
-- Descrizione: Estrai i primi tre caratteri del nome del cliente.


SELECT nome, SUBSTRING(nome, 1, 3) AS abbreviazione 
FROM clienti;
-- Esercizio 5: Calcolare la lunghezza di una stringa
-- Descrizione: Trova la lunghezza del nome dei clienti.


SELECT nome, CHAR_LENGTH(nome) AS lunghezza 
FROM clienti;
-- Esercizio 6: Rimuovere spazi iniziali e finali
-- Descrizione: Rimuovi spazi inutili dai nomi dei clienti.


SELECT nome, TRIM(nome) AS nome_senza_spazi 
FROM clienti;
-- Esercizio 7: Sostituire una parte di testo
-- Descrizione: Sostituisci "Rosso" con "Red" nei colori dei prodotti.


SELECT colore, REPLACE(colore, 'Rosso', 'Red') AS colore_modificato 
FROM prodotti;
-- Esercizio 8: Cercare una sottostringa
-- Descrizione: Trova i clienti con lettera iniziale del nome "A".


SELECT nome 
FROM clienti 
WHERE nome LIKE 'A%';
-- Esercizio 9: Inserire testo con zeri a sinistra
-- Descrizione: Formatta gli ID degli ordini in modo che abbiano sempre 5 cifre (es. 00001).


SELECT LPAD(id, 5, '0') AS id_formattato, data_ordine 
FROM ordini;

-- Esercizio 1: Arrotondare un numero
-- Descrizione: Arrotonda il prezzo dei prodotti a due decimali.


SELECT nome, prezzo, ROUND(prezzo, 2) AS prezzo_arrotondato 
FROM prodotti;
-- Esercizio 2: Trovare il valore assoluto
-- Descrizione: Calcola il valore assoluto della differenza tra quantità e 50.


SELECT nome, quantita, ABS(quantita - 50) AS differenza_assoluta 
FROM prodotti;
-- Esercizio 3: Calcolare la potenza
-- Descrizione: Calcola il quadrato della quantità dei prodotti.


SELECT nome, quantita, POWER(quantita, 2) AS quantita_al_quadrato 
FROM prodotti;
-- Esercizio 4: Calcolare la radice quadrata
-- Descrizione: Trova la radice quadrata del prezzo di ogni prodotto.


SELECT nome, prezzo, SQRT(prezzo) AS radice_prezzo 
FROM prodotti;
-- Esercizio 5: Generare numeri casuali
-- Descrizione: Associa un numero casuale a ogni cliente.


SELECT nome, cognome, RAND() AS numero_casuale 
FROM clienti;
-- Esercizio 6: Trovare il valore massimo e minimo
-- Descrizione: Mostra il prezzo massimo e minimo dei prodotti.


SELECT MAX(prezzo) AS prezzo_massimo, MIN(prezzo) AS prezzo_minimo 
FROM prodotti;
-- Esercizio 7: Arrotondare per eccesso e per difetto
-- Descrizione: Mostra il prezzo arrotondato per eccesso e per difetto.


SELECT nome, prezzo, CEIL(prezzo) AS arrotondato_eccesso, FLOOR(prezzo) AS arrotondato_difetto 
FROM prodotti;
-- Esercizio 8: Calcolare il resto della divisione (MOD)
-- Descrizione: Trova il resto della divisione tra quantità e 3 per ogni prodotto.


SELECT nome, quantita, MOD(quantita, 3) AS resto_divisione 
FROM prodotti;
-- Esercizio 9: Calcolare una media
-- Descrizione: Calcola la media dei prezzi dei prodotti.


SELECT AVG(prezzo) AS prezzo_medio 
FROM prodotti;
-- Esercizio 1: Estrarre la data corrente
-- Descrizione: Visualizza la data corrente per ogni ordine.


SELECT id, data_ordine, CURRENT_DATE AS data_corrente 
FROM ordini;
-- Esercizio 2: Calcolare l'età di un cliente
-- Descrizione: Calcola l'età in anni di ogni cliente in base alla data di nascita.


SELECT nome, cognome, YEAR(CURRENT_DATE) - YEAR(data_nascita) AS eta 
FROM clienti;
-- Esercizio 3: Estrarre anno, mese e giorno
-- Descrizione: Estrai l'anno, il mese e il giorno dalla data di un ordine.


SELECT id, data_ordine, YEAR(data_ordine) AS anno, MONTH(data_ordine) AS mese, DAY(data_ordine) AS giorno 
FROM ordini;
-- Esercizio 4: Calcolare la differenza tra date
-- Descrizione: Calcola il numero di giorni trascorsi tra la data dell'ordine e oggi.


SELECT id, data_ordine, DATEDIFF(CURRENT_DATE, data_ordine) AS giorni_trascorsi 
FROM ordini;
-- Esercizio 5: Aggiungere giorni a una data
-- Descrizione: Aggiungi 10 giorni alla data di ogni ordine.


SELECT id, data_ordine, DATE_ADD(data_ordine, INTERVAL 10 DAY) AS data_modificata 
FROM ordini;
-- Esercizio 6: Sottrarre mesi da una data
-- Descrizione: Sottrai 3 mesi alla data di ogni ordine.


SELECT id, data_ordine, DATE_SUB(data_ordine, INTERVAL 3 MONTH) AS data_modificata 
FROM ordini;
-- Esercizio 7: Estrarre il giorno della settimana
-- Descrizione: Mostra il giorno della settimana per ogni ordine (1 = Domenica, 7 = Sabato).


SELECT id, data_ordine, DAYOFWEEK(data_ordine) AS giorno_settimana 
FROM ordini;
-- Esercizio 8: Formattare una data
-- Descrizione: Formatta la data degli ordini nel formato "GG/MM/AAAA".

SELECT id, data_ordine, DATE_FORMAT(data_ordine, '%d/%m/%Y') AS data_formattata 
FROM ordini;
-- Esercizio 9: Calcolare il numero di mesi tra due date
-- Descrizione: Calcola il numero di mesi tra la data dell'ordine e oggi.


SELECT id, data_ordine, TIMESTAMPDIFF(MONTH, data_ordine, CURRENT_DATE) AS mesi_trascorsi 
FROM ordini;