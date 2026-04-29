<?php
// Crea un form HTML per:
// - titolo (text, required)
// - data (date, required)
// - descrizione (textarea, required)
// Il form viene usato sia per aggiunta che modifica
echo '<form action="" method="post">';
echo '<input type="text" name="title" placeholder="Titolo" required>';
echo '<input type="date" name="date" required>';
echo '<textarea name="description" placeholder="Descrizione" required></textarea>';
echo '<button type="submit">Salva</button>';
echo '</form>';
