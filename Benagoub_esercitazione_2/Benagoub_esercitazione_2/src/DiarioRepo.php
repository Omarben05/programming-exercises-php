<?php

class DiarioRepo {
    private string $directory;

    public function __construct(string $directory = __DIR__ . '/../diario') {
        $this->directory = $directory;
        if (!is_dir($this->directory)) {
            mkdir($this->directory, 0755, true);
        }
    }

    public function getAll(): array {
        $files = glob($this->directory . '/*.txt');
        usort($files, fn($a, $b) => strcmp($b, $a));
        return array_map(fn($file) => basename($file, '.txt'), $files);
    }

    public function get(string $date): ?string {
        $filename = $this->directory . '/' . basename($date) . '.txt';
        return file_exists($filename) ? file_get_contents($filename) : null;
    }

    public function save(string $date, string $text): bool {
        $filename = $this->directory . '/' . basename($date) . '.txt';
        $cleanText = strip_tags($text);
        return file_put_contents($filename, $cleanText) !== false;
    }

    public function delete(string $date): bool {
        $filename = $this->directory . '/' . basename($date) . '.txt';
        return file_exists($filename) ? unlink($filename) : false;
    }

    public function exists(string $date): bool {
        $filename = $this->directory . '/' . basename($date) . '.txt';
        return file_exists($filename);
    }

    
}
