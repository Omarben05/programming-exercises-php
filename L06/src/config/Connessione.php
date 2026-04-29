<?php

class Connessione {

    private $database;

    public function __construct() {
        try {
            $this->database = new PDO('mysql:host=' . HOST . ';dbname=esercitazioni', USER,PASS);
        } catch (PDOException $eccezione) {
            echo "Connessione fallita: " . $eccezione->getMessage();
        }
    }

    public function getDatabase() {
        return $this->database;
    }
}