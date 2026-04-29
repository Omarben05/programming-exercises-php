CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    descrizione TEXT,
    completato BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (titolo, descrizione, completato) VALUES
('Preparare la presentazione', 'Slide per il corso di PHP avanzato', FALSE),
('Scrivere documentazione API', 'Endpoint REST per il task manager', TRUE),
('Controllare esercizi studenti', 'Verifica esercitazione su file e sessioni', FALSE);
