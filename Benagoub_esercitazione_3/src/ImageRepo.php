<?php

class ImageRepo {
    private string $uploadDir;

    public function __construct() {
        $this->uploadDir = __DIR__ . '/../upload';
        if (!is_dir($this->uploadDir)) {
            mkdir($this->uploadDir, 0777, true);
        }
    }

    public function getAll(): array {
        return glob($this->uploadDir . '/*.{jpg,jpeg,png}', GLOB_BRACE);
    }

    public function save(array $file): bool|string {
        if ($file['error'] !== UPLOAD_ERR_OK) return false;

        $allowed = ['image/jpeg', 'image/png'];
        if (!in_array($file['type'], $allowed)) return false;

        if ($file['size'] > 2 * 1024 * 1024) return false;

        $ext = pathinfo($file['name'], PATHINFO_EXTENSION);
        $name = uniqid('img_', true) . '.' . $ext;
        $dest = $this->uploadDir . '/' . $name;

        if (move_uploaded_file($file['tmp_name'], $dest)) {
            return $name;
        }
        return false;
    }
}
