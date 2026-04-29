<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Quiz Geografico</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
        }
        .main-content {
            min-height: 80vh;
            padding-top: 40px;
        }
        .navbar {
            background: linear-gradient(90deg, #007bff 0%, #00c6ff 100%) !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        }
        .navbar-brand {
            font-size: 2rem;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .card {
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            border-radius: 1rem;
            transition: transform 0.15s;
        }
        .card:hover {
            transform: translateY(-4px) scale(1.01);
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        }
        .badge-custom {
            background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
            color: #fff;
            font-size: 1rem;
        }
        .btn-main {
            background: linear-gradient(90deg, #007bff 0%, #00c6ff 100%);
            color: #fff;
            border: none;
        }
        .btn-main:hover {
            background: linear-gradient(90deg, #0056b3 0%, #00aaff 100%);
            color: #fff;
        }
        footer {
            background: #222;
            color: #fff;
            padding: 18px 0 10px 0;
            font-size: 1rem;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center gap-2" href="{{ route('home') }}">
                <i class="bi bi-globe2"></i> Quiz Geografico
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ route('home') }}"><i class="bi bi-house-door"></i> Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ route('quiz.start') }}"><i class="bi bi-question-circle"></i> Quiz</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ route('training') }}"><i class="bi bi-lightbulb"></i> Allenamento</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <main class="main-content container">
        @yield('content')
    </main>
    <footer class="text-center mt-5">
        <div class="container">
            <small>&copy; {{ date('Y') }} Quiz Geografico. Powered by TommaFerre.</small>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
