<?php

// 1	Elenco eventi	index.php legge e mostra gli eventi da events.json

// Includi funzioni e sessione
// Carica eventi da JSON
// Mostra lista eventi con link per modificare e cancellare
// Mostra messaggi flash se presenti
// Mostra form per aggiungere un nuovo evento
include 'includes/functions.php';
include 'includes/session.php';
$events = load_events();

// Mostra messaggi flash se presenti
if (isset($_SESSION['flash_message'])) {
    echo '<div class="alert alert-success">' . $_SESSION['flash_message'] . '</div>';
    unset($_SESSION['flash_message']);
}

// Mostra lista eventi
echo '<h1>Elenco Eventi</h1>';
foreach ($events as $event) {
    echo '<div class="event">';
    echo '<h2>' . htmlspecialchars($event['title']) . '</h2>';
    echo '<p>' . htmlspecialchars($event['description']) . '</p>';
    echo '<p>Data: ' . htmlspecialchars($event['date']) . '</p>';
    echo '<a href="edit.php?id=' . $event['id'] . '">Modifica</a> | ';
    echo '<a href="delete.php?id=' . $event['id'] . '">Cancella</a>';
    echo '</div>';
}
// Mostra form per aggiungere un nuovo evento
echo '<h2>Aggiungi Nuovo Evento</h2>';
echo '<form action="add.php" method="post">';
echo '<input type="text" name="title" placeholder="Titolo" required>';
echo '<input type="text" name="description" placeholder="Descrizione" required>';
echo '<input type="date" name="date" required>';
echo '<button type="submit">Aggiungi Evento</button>';
echo '</form>';

// Incrementa il contatore delle operazioni
increment_operations(); 
// Mostra il numero di operazioni effettuate
echo '<p>Operazioni effettuate: ' . $_SESSION['operations'] . '</p>';
// Mostra il nome utente se presente
if (isset($_SESSION['user'])) {
    echo '<p>Utente: ' . htmlspecialchars($_SESSION['user']) . '</p>';
}   