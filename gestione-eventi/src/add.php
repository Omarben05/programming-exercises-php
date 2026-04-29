<?php

//2 Aggiungi evento Form con: titolo, descrizione, data evento

// Includi funzioni e sessione
// Se il form è stato inviato (POST):
//   - carica eventi
//   - crea nuovo evento con id, titolo, data, descrizione
//   - salva eventi
//   - incrementa operazioni e imposta messaggio flash
//   - reindirizza a index
// Altrimenti mostra il form

include 'includes/functions.php';
include 'includes/session.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Carica eventi
    $events = load_events();

    // Crea nuovo evento
    $new_event = [
        'id' => uniqid(),
        'title' => $_POST['title'],
        'description' => $_POST['description'],
        'date' => $_POST['date']
    ];

    // Aggiungi evento
    $events[] = $new_event;

    // Salva eventi
    save_events($events);

    // Incrementa operazioni
    increment_operations();

    // Imposta messaggio flash
    $_SESSION['flash_message'] = 'Evento aggiunto con successo!';

    // Reindirizza a index
    header('Location: index.php');
    exit;
}

// Mostra form
echo '<h2>Aggiungi Nuovo Evento</h2>';
echo '<form action="add.php" method="post">';
echo '<input type="text" name="title" placeholder="Titolo" required>';
echo '<input type="text" name="description" placeholder="Descrizione" required>';
echo '<input type="date" name="date" required>';
echo '<button type="submit">Aggiungi Evento</button>';
echo '</form>';
