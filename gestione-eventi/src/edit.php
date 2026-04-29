<?php

// 3	Modifica evento	Form precompilato con dati da events.json

// Includi funzioni e sessione
// Carica evento da modificare tramite ID in GET
// Se evento non trovato mostra errore
// Se form inviato:
//   - aggiorna i dati dell'evento
//   - salva eventi, incrementa operazioni, messaggio flash
//   - reindirizza
// Altrimenti mostra il form

include 'includes/functions.php';
include 'includes/session.php';

//carica l'evento da modificare
if (isset($_GET['id'])) {
    $event = get_event_by_id($_GET['id']);
    if (!$event) {
        echo 'Evento non trovato!';
        exit;
    }
}

// Se il form è stato inviato (POST):
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Aggiorna i dati dell'evento
    $event['title'] = $_POST['title'];
    $event['description'] = $_POST['description'];
    $event['date'] = $_POST['date'];

    // Salva eventi
    save_events($events);

    // Incrementa operazioni
    increment_operations();

    // Imposta messaggio flash
    $_SESSION['flash_message'] = 'Evento modificato con successo!';

    // Reindirizza a index
    header('Location: index.php');
    exit;
}

// Mostra form
echo '<h2>Modifica Evento</h2>';
echo '<form action="edit.php?id=' . $event['id'] . '" method="post">';
echo '<input type="text" name="title" value="' . htmlspecialchars($event['title']) . '" required>';
echo '<input type="text" name="description" value="' . htmlspecialchars($event['description']) . '" required>';
echo '<input type="date" name="date" value="' . htmlspecialchars($event['date']) . '" required>';
echo '<button type="submit">Salva Modifiche</button>';
echo '</form>';
