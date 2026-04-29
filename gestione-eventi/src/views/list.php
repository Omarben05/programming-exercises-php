<?php
// Includi header e funzioni
// Carica gli eventi e mostra l'elenco in HTML
$events = load_events();
echo '<ul>';
foreach ($events as $event) {
    echo '<li>';
    echo '<h3>' . htmlspecialchars($event['title']) . '</h3>';
    echo '<p>' . htmlspecialchars($event['description']) . '</p>';
    echo '<p><strong>Data:</strong> ' . htmlspecialchars($event['date']) . '</p>';
    echo '<a href="edit.php?id=' . $event['id'] . '">Modifica</a> | ';
    echo '<a href="delete.php?id=' . $event['id'] . '">Elimina</a>';
    echo '</li>';
}
echo '</ul>';