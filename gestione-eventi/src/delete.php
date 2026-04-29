<?php

// 4	Cancella evento	Conferma ed eliminazione da JSON

// Includi funzioni e sessione
// Carica eventi, cerca ID da eliminare
// Se trovato, rimuovi evento, salva, incrementa contatore, messaggio flash
// Reindirizza  

include 'includes/functions.php';
include 'includes/session.php';


if (isset($_GET['id'])) {
    $events = load_events();
    $event_id = $_GET['id'];
    $event_key = array_search($event_id, array_column($events, 'id'));
    if ($event_key !== false) {
        unset($events[$event_key]);
        save_events($events);
        increment_operations();
        $_SESSION['flash_message'] = 'Evento eliminato con successo!';
    }
    header('Location: index.php');
    exit;
}
