<?php
declare(strict_types=1);

require __DIR__ . '/../vendor/autoload.php';

use OmarBenagoub\BenagoubEsercitazione4\Controller\TaskController;


header('Content-Type: application/json');

$method = $_SERVER['REQUEST_METHOD'];
$controller = new TaskController();

switch ($method) {
    case 'GET':
        $controller->getAll();
        break;
    case 'POST':
        $controller->create();
        break;
    case 'PUT':
        $controller->update();
        break;
    case 'DELETE':
        $controller->delete();
        break;
    default:
        http_response_code(405);
        echo json_encode(['status' => 'error', 'message' => 'Metodo non consentito']);
}
