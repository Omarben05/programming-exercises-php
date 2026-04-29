<?php
require_once __DIR__ . '/../src/DiarioRepo.php';

session_start();
$success = $_SESSION['success'] ?? '';
$error = $_SESSION['error'] ?? '';
unset($_SESSION['success'], $_SESSION['error']);

$repo = new DiarioRepo();
$voci = $repo->getAll();

$title = 'Elenco Voci';
require_once __DIR__ . '/../view/header.php';
?>

<h2>Diario di Bordo</h2>

<nav>
    <ul>
        <li><a href="logout.php">Logout</a></li>
        <li><a href="scrivi.php">Scrivi nuova voce</a></li>
    </ul>
</nav>

<?php if ($success): ?><p class="msg-success"><?= htmlspecialchars($success) ?></p><?php endif; ?>
<?php if ($error): ?><p class="msg-error"><?= htmlspecialchars($error) ?></p><?php endif; ?>

<?php if (empty($voci)): ?>
    <p>Nessuna voce trovata.</p>
<?php else: ?>
    <table>
        <thead><tr><th>Data</th><th>Azioni</th></tr></thead>
        <tbody>
            <?php foreach ($voci as $data): ?>
                <tr>
                    <td><?= htmlspecialchars(date("d/m/Y", strtotime($data))) ?></td>
                    <td>
                        <a href="leggi.php?file=<?= urlencode($data) ?>">Leggi</a> |
                        <a href="delete.php?file=<?= urlencode($data) ?>" onclick="return confirm('Sei sicuro di voler eliminare questa voce?');">Elimina</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
<?php endif; ?>

<?php require_once __DIR__ . '/../view/footer.php'; ?>
