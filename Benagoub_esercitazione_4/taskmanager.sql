-- 🗄️ Creazione del database
CREATE DATABASE IF NOT EXISTS taskmanager;
USE taskmanager;

-- 📋 Creazione della tabella "tasks"
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    descrizione TEXT,
    completato BOOLEAN DEFAULT FALSE
);

-- 🧪 Inserimento di dati mock (come da traccia)
INSERT INTO tasks (titolo, descrizione, completato) VALUES
('Preparare la presentazione', 'Slide per il corso di PHP avanzato', FALSE),
('Scrivere documentazione API', 'Endpoint REST per il task manager', TRUE),
('Controllare esercizi studenti', 'Verifica esercitazione su file e sessioni', FALSE);
