<?php
namespace Src\Config;

use PDO;
use PDOException;

class Database {
    private $host = 'localhost';
    private $db_name = 'taskmanager';
    private $username = 'root';  // Modifica se serve
    private $password = '';      // Modifica se serve
    public $conn;

    public function getConnection(): ?PDO {
        $this->conn = null;
        try {
            $this->conn = new PDO(
                "mysql:host={$this->host};dbname={$this->db_name};charset=utf8",
                $this->username,
                $this->password
            );
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
            exit;
        }
        return $this->conn;
    }
}
