<?php
require_once __DIR__ . '/../src/DiarioRepo.php';


session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = $_POST['data'] ?? '';
    $testo = $_POST['testo'] ?? '';

    if (!$data || !$testo) {
        $_SESSION['error'] = "Inserisci data e testo.";
        header("Location: scrivi.php");
        exit;
    }

    $repo = new DiarioRepo();
    if ($repo->save($data, $testo)) {
        $_SESSION['success'] = "Voce salvata con successo.";
        header("Location: index.php");
        exit;
    } else {
        $_SESSION['error'] = "Errore durante il salvataggio.";
        header("Location: scrivi.php");
        exit;
    }
}

$title = 'Scrivi nuova voce';
require_once __DIR__ . '/../view/header.php';
?>

<h2>Scrivi nuova voce</h2>
<form method="post">
    <label>Data: <input type="date" name="data" required></label><br><br>
    <textarea name="testo" rows="10" cols="60" placeholder="Scrivi qui..." required></textarea><br><br>
    <button type="submit">Salva</button>
</form>
<a href="index.php">Torna all'elenco</a>

<?php require_once __DIR__ . '/../view/footer.php'; ?>
