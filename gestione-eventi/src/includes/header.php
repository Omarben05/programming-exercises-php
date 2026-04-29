<?php
// Includi il file di sessione
// Mostra intestazione HTML con nome utente e numero operazioni
// Includi link alla home e al form di aggiunta

// Includi il file di sessione
include 'session.php';
// Mostra intestazione HTML con nome utente e numero operazioni
echo '<!DOCTYPE html>';
echo '<html lang="it">';
echo '<head>';
echo '<meta charset="UTF-8">';
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo '<title>Gestione Eventi</title>';  
echo '<link rel="stylesheet" href="style.css">';  // Includi il CSS
echo '</head>';
echo '<body>';
echo '<header>';
echo '<h1>Gestione Eventi</h1>';
echo '<nav>';
echo '<ul>';
echo '<li><a href="index.php">Home</a></li>';
echo '<li><a href="add.php">Aggiungi Evento</a></li>';
echo '</ul>';
echo '</nav>';
echo '</header>';
