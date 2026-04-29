<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header('Location: login.php');
    exit;
}
require_once __DIR__ . '/../src/ContactRepo.php';
$repo = new ContactRepo();
$contatti = $repo->getAll();
$success = $_SESSION['success'] ?? '';
$error = $_SESSION['error'] ?? '';
unset($_SESSION['success'], $_SESSION['error']);
$title = 'Rubrica Contatti';
require_once __DIR__ . '/../view/header.php';
?>
<h2>Rubrica Contatti</h2>
<nav>
  <ul>
    <li><a href="logout.php">Logout</a></li>
    <li><a href="add.php">Aggiungi Contatto</a></li>
  </ul>
</nav>
<?php if ($success): ?><p class="msg-success"><?= htmlspecialchars($success) ?></p><?php endif; ?>
<?php if ($error): ?><p class="msg-error"><?= htmlspecialchars($error) ?></p><?php endif; ?>
<table>
    <thead>
    <tr><th>Nome</th><th>Cognome</th><th>Email</th><th>Telefono</th><th>Azioni</th></tr>
    </thead>
    <tbody>
    <?php foreach ($contatti as $c): ?>
    <tr>
        <td><?= htmlspecialchars($c['nome']) ?></td>
        <td><?= htmlspecialchars($c['cognome']) ?></td>
        <td><?= htmlspecialchars($c['email']) ?></td>
        <td><?= htmlspecialchars($c['telefono']) ?></td>
        <td>
            <a href="edit.php?id=<?= $c['id'] ?>">Modifica</a> |
            <a href="delete.php?id=<?= $c['id'] ?>" onclick="return confirm('Sicuro di voler cancellare?');">Elimina</a>
        </td>
    </tr>
    <?php endforeach; ?>
    </tbody>
</table>
<?php require_once __DIR__ . '/../view/footer.php'; ?>
