<?php
// Connessione PDO al database MySQL
function getPDO() {
    $host = 'localhost';
    $db   = 'challenge';
    $user = 'root'; // Cambia se necessario
    $pass = 'dima';
    $charset = 'utf8mb4';
    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];
    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (PDOException $e) {
        die('Connessione fallita: ' . $e->getMessage());
    }
}
