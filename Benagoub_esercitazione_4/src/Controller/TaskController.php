<?php
 namespace OmarBenagoub\BenagoubEsercitazione4\Controller;;

use Src\Config\Database;
use PDO;

class TaskController {
    private $conn;

    public function __construct() {
        $database = new Database();
        $this->conn = $database->getConnection();
    }

    public function getAll() {
        $stmt = $this->conn->prepare("SELECT * FROM tasks");
        $stmt->execute();
        $tasks = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode(['status' => 'ok', 'data' => $tasks]);
    }

    public function create() {
        $input = json_decode(file_get_contents('php://input'), true);
        if (!isset($input['titolo'])) {
            echo json_encode(['status' => 'error', 'message' => 'Titolo mancante']);
            return;
        }
        $titolo = htmlspecialchars($input['titolo']);
        $descrizione = isset($input['descrizione']) ? htmlspecialchars($input['descrizione']) : '';
        $stmt = $this->conn->prepare("INSERT INTO tasks (titolo, descrizione) VALUES (:titolo, :descrizione)");
        $stmt->bindParam(':titolo', $titolo);
        $stmt->bindParam(':descrizione', $descrizione);
        if ($stmt->execute()) {
            echo json_encode(['status' => 'ok', 'data' => ['id' => $this->conn->lastInsertId()]]);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Errore inserimento']);
        }
    }

    public function update() {
        parse_str(file_get_contents("php://input"), $put_vars);
        if (!isset($put_vars['id']) || !isset($put_vars['completato'])) {
            echo json_encode(['status' => 'error', 'message' => 'Parametri mancanti']);
            return;
        }
        $id = (int)$put_vars['id'];
        $completato = (int)$put_vars['completato'];
        $stmt = $this->conn->prepare("UPDATE tasks SET completato = :completato WHERE id = :id");
        $stmt->bindParam(':completato', $completato, PDO::PARAM_INT);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        if ($stmt->execute()) {
            echo json_encode(['status' => 'ok', 'data' => ['id' => $id]]);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Errore aggiornamento']);
        }
    }

    public function delete() {
        parse_str(file_get_contents("php://input"), $del_vars);
        if (!isset($del_vars['id'])) {
            echo json_encode(['status' => 'error', 'message' => 'ID mancante']);
            return;
        }
        $id = (int)$del_vars['id'];
        $stmt = $this->conn->prepare("DELETE FROM tasks WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        if ($stmt->execute()) {
            echo json_encode(['status' => 'ok', 'data' => ['id' => $id]]);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Errore eliminazione']);
        }
    }
}
