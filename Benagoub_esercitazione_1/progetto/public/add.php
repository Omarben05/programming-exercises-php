<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header('Location: login.php');
    exit;
}
require_once __DIR__ . '/../src/ContactRepo.php';
$repo = new ContactRepo();
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = htmlspecialchars(trim($_POST['nome'] ?? ''));
    $cognome = htmlspecialchars(trim($_POST['cognome'] ?? ''));
    $email = htmlspecialchars(trim($_POST['email'] ?? ''));
    $telefono = htmlspecialchars(trim($_POST['telefono'] ?? ''));
    if ($nome && $cognome && $email && $telefono) {
        if ($repo->add($nome, $cognome, $email, $telefono)) {
            $_SESSION['success'] = 'Contatto aggiunto con successo!';
            header('Location: index.php');
            exit;
        } else {
            $error = 'Errore durante l\'inserimento.';
        }
    } else {
        $error = 'Tutti i campi sono obbligatori.';
    }
}
$title = 'Aggiungi Contatto';
require_once __DIR__ . '/../view/header.php';
echo '<h2>Aggiungi Contatto</h2>';
if ($error) {
    echo '<p class="msg-error">' . htmlspecialchars($error) . '</p>';
}
?>
<form method="post">
    <label>Nome:
        <input type="text" name="nome" required>
    </label>
    <label>Cognome:
        <input type="text" name="cognome" required>
    </label>
    <label>Email:
        <input type="email" name="email" required>
    </label>
    <label>Telefono:
        <input type="text" name="telefono" required>
    </label>
    <button class="btn" type="submit">Aggiungi</button>
</form>
<p><a href="index.php">Torna alla rubrica</a></p>
<?php require_once __DIR__ . '/../view/footer.php'; ?>
