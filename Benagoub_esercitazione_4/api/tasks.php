<?php
session_start();
header('Content-Type: application/json');

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    echo json_encode(['status' => 'error', 'message' => 'Non autorizzato']);
    exit;
}

require_once __DIR__ . '/../config/db.php';
require_once __DIR__ . '/../src/TaskRepo.php';

$repo = new TaskRepo($pdo);
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        $tasks = $repo->getAll();
        echo json_encode(['status' => 'ok', 'data' => $tasks]);
        break;

    case 'POST':
        $data = json_decode(file_get_contents("php://input"), true);
        $titolo = strip_tags($data['titolo'] ?? '');
        $descrizione = strip_tags($data['descrizione'] ?? '');
        if ($titolo === '') {
            echo json_encode(['status' => 'error', 'message' => 'Titolo richiesto']);
            break;
        }
        $repo->create($titolo, $descrizione);
        echo json_encode(['status' => 'ok']);
        break;

    case 'PUT':
        parse_str(file_get_contents("php://input"), $data);
        $id = (int)($data['id'] ?? 0);
        $titolo = trim(strip_tags($data['titolo'] ?? ''));
        $descrizione = trim(strip_tags($data['descrizione'] ?? ''));

        if ($titolo !== '') {
            $repo->update($id, $titolo, $descrizione);
        } else {
            $repo->complete($id);
        }
        echo json_encode(['status' => 'ok']);
        break;

    case 'DELETE':
        parse_str(file_get_contents("php://input"), $data);
        $id = (int)($data['id'] ?? 0);
        $repo->delete($id);
        echo json_encode(['status' => 'ok']);
        break;

    default:
        echo json_encode(['status' => 'error', 'message' => 'Metodo non supportato']);
}
