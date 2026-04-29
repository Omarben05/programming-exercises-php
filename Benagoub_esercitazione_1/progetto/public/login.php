<?php
session_start();
if (isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true) {
    header('Location: index.php');
    exit;
}
$error = $_SESSION['error'] ?? '';
unset($_SESSION['error']);
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user = $_POST['username'] ?? '';
    $pass = $_POST['password'] ?? '';
    if ($user === 'admin' && $pass === '1234') {
        $_SESSION['logged_in'] = true;
        header('Location: index.php');
        exit;
    } else {
        $_SESSION['error'] = 'Credenziali non valide';
        header('Location: login.php');
        exit;
    }
}
$title = 'Login Rubrica';
require_once __DIR__ . '/../view/header.php';
echo '<h2>Login</h2>';
if ($error) {
    echo '<p class="msg-error">' . htmlspecialchars($error) . '</p>';
}
?>
<form method="post">
    <label>Utente:
        <input type="text" name="username" required>
    </label>
    <label>Password:
        <input type="password" name="password" required>
    </label>
    <button class="btn" type="submit">Login</button>
</form>
<?php require_once __DIR__ . '/../view/footer.php'; ?>
