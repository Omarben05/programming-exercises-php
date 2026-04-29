<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header('Location: login.php');
    exit;
}
require_once __DIR__ . '/../src/ContactRepo.php';
$repo = new ContactRepo();
$id = $_GET['id'] ?? null;
if (!$id) {
    $_SESSION['error'] = 'ID non valido.';
    header('Location: index.php');
    exit;
}
$contatto = $repo->getById($id);
if (!$contatto) {
    $_SESSION['error'] = 'Contatto non trovato.';
    header('Location: index.php');
    exit;
}
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = htmlspecialchars(trim($_POST['nome'] ?? ''));
    $cognome = htmlspecialchars(trim($_POST['cognome'] ?? ''));
    $email = htmlspecialchars(trim($_POST['email'] ?? ''));
    $telefono = htmlspecialchars(trim($_POST['telefono'] ?? ''));
    if ($nome && $cognome && $email && $telefono) {
        if ($repo->update($id, $nome, $cognome, $email, $telefono)) {
            $_SESSION['success'] = 'Contatto modificato con successo!';
            header('Location: index.php');
            exit;
        } else {
            $error = 'Errore durante la modifica.';
        }
    } else {
        $error = 'Tutti i campi sono obbligatori.';
    }
}
$title = 'Modifica Contatto';
require_once __DIR__ . '/../view/header.php';
echo '<h2>Modifica Contatto</h2>';
if ($error) {
    echo '<p class="msg-error">' . htmlspecialchars($error) . '</p>';
}
?>
<form method="post">
    <label>Nome:
        <input type="text" name="nome" value="<?= htmlspecialchars($contatto['nome']) ?>" required>
    </label>
    <label>Cognome:
        <input type="text" name="cognome" value="<?= htmlspecialchars($contatto['cognome']) ?>" required>
    </label>
    <label>Email:
        <input type="email" name="email" value="<?= htmlspecialchars($contatto['email']) ?>" required>
    </label>
    <label>Telefono:
        <input type="text" name="telefono" value="<?= htmlspecialchars($contatto['telefono']) ?>" required>
    </label>
    <button class="btn" type="submit">Salva Modifiche</button>
</form>
<p><a href="index.php">Torna alla rubrica</a></p>
<?php require_once __DIR__ . '/../view/footer.php'; ?>
