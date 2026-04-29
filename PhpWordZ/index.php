<?php
session_start();

// Initialize game state if not exists
if (!isset($_SESSION['secret_word'])) {
    // Read words from file
    $words = file('parole.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $_SESSION['secret_word'] = strtoupper(trim($words[array_rand($words)]));
    $_SESSION['attempts'] = [];
    $_SESSION['game_over'] = false;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['guess'])) {
        $guess = strtoupper(trim($_POST['guess']));
        if (strlen($guess) === 5) {
            $_SESSION['attempts'][] = $guess;
        }
    } elseif (isset($_POST['reset'])) {
        session_destroy();
        header('Location: index.php');
        exit;
    }
}

// Check game state
$won = false;
if (!empty($_SESSION['attempts'])) {
    $lastGuess = end($_SESSION['attempts']);
    if ($lastGuess === $_SESSION['secret_word']) {
        $won = true;
        $_SESSION['game_over'] = true;
    } elseif (count($_SESSION['attempts']) >= 6) {
        $_SESSION['game_over'] = true;
    }
}
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>PHPWordz</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>PHPWordz</h1>
    
    <div class="game-container">
        <?php
        // Display previous attempts
        foreach ($_SESSION['attempts'] as $attempt) {
            echo '<div class="word-row">';
            for ($i = 0; $i < 5; $i++) {
                $class = 'gray';
                if ($attempt[$i] === $_SESSION['secret_word'][$i]) {
                    $class = 'green';
                } elseif (strpos($_SESSION['secret_word'], $attempt[$i]) !== false) {
                    $class = 'yellow';
                }
                echo "<span class='letter $class'>{$attempt[$i]}</span>";
            }
            echo '</div>';
        }
        ?>

        <?php if (!$_SESSION['game_over']) : ?>
            <form method="POST">
                <input type="text" name="guess" maxlength="5" pattern=".{5,5}" required 
                       placeholder="Inserisci una parola di 5 lettere">
                <button type="submit">Prova</button>
            </form>
        <?php else : ?>
            <div class="game-over">
                <?php if ($won) : ?>
                    <p>Congratulazioni! Hai indovinato la parola!</p>
                <?php else : ?>
                    <p>Game Over! La parola era: <?php echo $_SESSION['secret_word']; ?></p>
                <?php endif; ?>
                <form method="POST">
                    <button type="submit" name="reset">Nuova Partita</button>
                </form>
            </div>
        <?php endif; ?>
    </div>
</body>
</html>