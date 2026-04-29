<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header('Location: login.php');
    exit;
}
require_once __DIR__ . '/../src/ContactRepo.php';
$repo = new ContactRepo();
$id = $_GET['id'] ?? null;
if ($id) {
    if ($repo->delete($id)) {
        $_SESSION['success'] = 'Contatto eliminato con successo!';
    } else {
        $_SESSION['error'] = 'Errore durante la cancellazione.';
    }
} else {
    $_SESSION['error'] = 'ID non valido.';
}
header('Location: index.php');
exit;
