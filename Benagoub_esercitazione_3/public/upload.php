<?php
require_once __DIR__ . '/../src/ImageRepo.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $repo = new ImageRepo();
    $file = $_FILES['immagine'] ?? null;

    if (!$file) {
        $_SESSION['error'] = "Nessun file selezionato.";
    } else {
        $result = $repo->save($file);
        if ($result) {
            $_SESSION['success'] = "Immagine caricata con successo.";
        } else {
            $_SESSION['error'] = "Errore: formato non valido o dimensione eccessiva.";
        }
    }
    header("Location: index.php");
    exit;
}
