<?php

//  gestione sessioni e utente fittizio

// Inizializza la sessione
// Memorizza l'utente (da $_GET['user']) e il contatore delle operazioni
// Crea una funzione per incrementare il contatore
// Crea una funzione per i messaggi flash

session_start();  // Inizializza la sessione 

//memorizza l'utente
if (isset($_GET['user'])) {
    $_SESSION['user'] = htmlspecialchars($_GET['user']);
}
// Inizializza il contatore delle operazioni se non esiste
if (!isset($_SESSION['operations'])) {
    $_SESSION['operations'] = 0;
}

// Funzione per incrementare il contatore delle operazioni
function increment_operations() {
    if (isset($_SESSION['operations'])) {
        $_SESSION['operations']++;
    }
}

// Funzione per i messaggi flash
function set_flash_message($message) {
    $_SESSION['flash_message'] = $message;
}
