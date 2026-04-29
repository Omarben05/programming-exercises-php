<?php
require_once __DIR__ . '/../src/DiarioRepo.php';

session_start();

$file = basename($_GET['file'] ?? '');
$repo = new DiarioRepo();

if ($repo->delete($file)) {
    $_SESSION['success'] = "Voce eliminata con successo.";
} else {
    $_SESSION['error'] = "Errore durante l'eliminazione.";
}

header("Location: index.php");
exit;
