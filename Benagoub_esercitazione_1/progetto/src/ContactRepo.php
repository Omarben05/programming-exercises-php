<?php
require_once __DIR__ . '/database.php';

class ContactRepo {
    private $pdo;
    public function __construct() {
        $this->pdo = getPDO();
    }
    public function getAll() {
        $stmt = $this->pdo->query('SELECT * FROM contatti ORDER BY id DESC');
        return $stmt->fetchAll();
    }
    public function getById($id) {
        $stmt = $this->pdo->prepare('SELECT * FROM contatti WHERE id = ?');
        $stmt->execute([$id]);
        return $stmt->fetch();
    }
    public function add($nome, $cognome, $email, $telefono) {
        $stmt = $this->pdo->prepare('INSERT INTO contatti (nome, cognome, email, telefono) VALUES (?, ?, ?, ?)');
        return $stmt->execute([$nome, $cognome, $email, $telefono]);
    }
    public function update($id, $nome, $cognome, $email, $telefono) {
        $stmt = $this->pdo->prepare('UPDATE contatti SET nome=?, cognome=?, email=?, telefono=? WHERE id=?');
        return $stmt->execute([$nome, $cognome, $email, $telefono, $id]);
    }
    public function delete($id) {
        $stmt = $this->pdo->prepare('DELETE FROM contatti WHERE id=?');
        return $stmt->execute([$id]);
    }
}
