<?php
require_once __DIR__ . '/../src/DiarioRepo.php';

session_start();
$nome = basename($_GET['file'] ?? '');
$repo = new DiarioRepo();

$contenuto = $repo->get($nome);
if ($contenuto === null) {
    $_SESSION['error'] = "Voce non trovata.";
    header("Location: index.php");
    exit;
}

$title = 'Voce del Diario';
require_once __DIR__ . '/../view/header.php';
?>

<h2>Voce del <?= htmlspecialchars(date("d/m/Y", strtotime($nome))) ?></h2>
<div style="white-space: pre-wrap; border:1px solid #ccc; padding:10px; background:#fff;">
    <?= nl2br(htmlspecialchars($contenuto)) ?>
</div>
<a href="index.php">← Torna all'elenco</a>

<?php require_once __DIR__ . '/../view/footer.php'; ?>
