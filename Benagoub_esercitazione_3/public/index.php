<?php
require_once __DIR__ . '/../src/ImageRepo.php';

session_start();

$repo = new ImageRepo();
$files = $repo->getAll();

$success = $_SESSION['success'] ?? '';
$error = $_SESSION['error'] ?? '';
unset($_SESSION['success'], $_SESSION['error']);

$title = 'Galleria Immagini';
require_once __DIR__ . '/../view/header.php';
?>

<h2>Galleria Immagini</h2>

<nav>
    <ul>
        <li><a href="logout.php">Logout</a></li>
    </ul>
</nav>

<form method="post" action="upload.php" enctype="multipart/form-data">
    <input type="file" name="immagine" accept=".jpg,.jpeg,.png" required>
    <button type="submit">Carica</button>
</form>

<?php if ($success): ?><p class="msg-success"><?= htmlspecialchars($success) ?></p><?php endif; ?>
<?php if ($error): ?><p class="msg-error"><?= htmlspecialchars($error) ?></p><?php endif; ?>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px;">
    <?php foreach ($files as $img): ?>
        <img src="../upload/<?= htmlspecialchars(basename($img)) ?>" style="max-width:100%; height:auto;">
    <?php endforeach; ?>
</div>

<?php require_once __DIR__ . '/../view/footer.php'; ?>
