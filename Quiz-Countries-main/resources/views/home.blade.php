@extends('welcome')

@section('content')
<div class="container py-5">
    <h1 class="mb-5 text-center">Scegli una modalità</h1>
    <div class="row justify-content-center g-4">
        <!-- Card Quiz -->
        <div class="col-md-5 col-lg-4">
            <div class="card h-100 text-center p-4">
                <div class="mb-3">
                    <i class="bi bi-question-circle display-3 text-primary"></i>
                </div>
                <h3 class="mb-2">Quiz</h3>
                <p class="mb-4">Metti alla prova le tue conoscenze sulle capitali e le bandiere! Scegli la difficoltà e inizia il quiz.</p>
                <button class="btn btn-main btn-lg w-100" data-bs-toggle="modal" data-bs-target="#quizModal">
                    <i class="bi bi-play-circle"></i> Inizia Quiz
                </button>
            </div>
        </div>
        <!-- Card Allenamento -->
        <div class="col-md-5 col-lg-4">
            <div class="card h-100 text-center p-4">
                <div class="mb-3">
                    <i class="bi bi-lightbulb display-3 text-warning"></i>
                </div>
                <h3 class="mb-2">Allenamento</h3>
                <p class="mb-4">Visualizza i dati dei paesi uno per uno per memorizzare bandiere, capitali e altro.</p>
                <a href="{{ route('training') }}" class="btn btn-main btn-lg w-100">
                    <i class="bi bi-arrow-right-circle"></i> Allenati ora
                </a>
            </div>
        </div>
        <!-- Card Quiz Bandiere -->
        <div class="col-md-5 col-lg-4">
            <div class="card h-100 text-center p-4">
                <div class="mb-3">
                    <i class="bi bi-flag display-3 text-danger"></i>
                </div>
                <h3 class="mb-2">Quiz Bandiere</h3>
                <p class="mb-4">Riconosci la bandiera e abbinala al paese corretto! Scegli la difficoltà e inizia il quiz.</p>
                <button class="btn btn-main btn-lg w-100" data-bs-toggle="modal" data-bs-target="#flagQuizModal">
                    <i class="bi bi-play-circle"></i> Inizia Quiz Bandiere
                </button>
            </div>
        </div>
        <!-- Card Memory Game -->
        <div class="col-md-5 col-lg-4">
            <div class="card h-100 text-center p-4">
                <div class="mb-3">
                    <i class="bi bi-grid-3x3-gap-fill display-3 text-success"></i>
                </div>
                <h3 class="mb-2">Memory Game</h3>
                <p class="mb-4">Accoppia bandiere e nomi dei paesi! Scegli la difficoltà e sfida la tua memoria.</p>
                <button class="btn btn-main btn-lg w-100" data-bs-toggle="modal" data-bs-target="#memoryModal">
                    <i class="bi bi-play"></i> Gioca ora
                </button>
            </div>
        </div>
        <!-- Card Placeholder per future modalità -->
        <div class="col-md-5 col-lg-4 d-none d-md-block">
            <div class="card h-100 text-center p-4 bg-light border-0" style="opacity:0.6;">
                <div class="mb-3">
                    <i class="bi bi-puzzle display-3 text-secondary"></i>
                </div>
                <h3 class="mb-2">Prossimamente...</h3>
                <p class="mb-4">Nuove modalità di gioco in arrivo!</p>
                <button class="btn btn-secondary btn-lg w-100" disabled>
                    <i class="bi bi-lock"></i> In arrivo
                </button>
            </div>
        </div>
    </div>

    <!-- Modal scelta difficoltà Quiz -->
    <div class="modal fade" id="quizModal" tabindex="-1" aria-labelledby="quizModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="quizModalLabel">Scegli la difficoltà</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Chiudi"></button>
                </div>
                <div class="modal-body text-center">
                    <form method="GET" action="{{ route('quiz.start') }}">
                        <button type="submit" name="difficulty" value="easy" class="btn btn-success btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-smile"></i> Semplice (solo Europa)
                        </button>
                        <button type="submit" name="difficulty" value="medium" class="btn btn-warning btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-neutral"></i> Media (Europa + Americhe)
                        </button>
                        <button type="submit" name="difficulty" value="hard" class="btn btn-danger btn-lg w-100">
                            <i class="bi bi-emoji-dizzy"></i> Difficile (Tutto il mondo)
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal scelta difficoltà Quiz Bandiere -->
    <div class="modal fade" id="flagQuizModal" tabindex="-1" aria-labelledby="flagQuizModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="flagQuizModalLabel">Scegli la difficoltà</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Chiudi"></button>
                </div>
                <div class="modal-body text-center">
                    <form method="GET" action="{{ route('flagquiz.start') }}">
                        <button type="submit" name="difficulty" value="easy" class="btn btn-success btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-smile"></i> Semplice (solo Europa)
                        </button>
                        <button type="submit" name="difficulty" value="medium" class="btn btn-warning btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-neutral"></i> Media (Europa + Americhe)
                        </button>
                        <button type="submit" name="difficulty" value="hard" class="btn btn-danger btn-lg w-100">
                            <i class="bi bi-emoji-dizzy"></i> Difficile (Tutto il mondo)
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal scelta difficoltà Memory Game -->
    <div class="modal fade" id="memoryModal" tabindex="-1" aria-labelledby="memoryModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="memoryModalLabel">Scegli la difficoltà</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Chiudi"></button>
                </div>
                <div class="modal-body text-center">
                    <form method="GET" action="{{ route('memorygame') }}">
                        <button type="submit" name="difficulty" value="easy" class="btn btn-success btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-smile"></i> Facile (3x4, 6 coppie)
                        </button>
                        <button type="submit" name="difficulty" value="medium" class="btn btn-warning btn-lg w-100 mb-3">
                            <i class="bi bi-emoji-neutral"></i> Medio (4x4, 8 coppie)
                        </button>
                        <button type="submit" name="difficulty" value="hard" class="btn btn-danger btn-lg w-100">
                            <i class="bi bi-emoji-dizzy"></i> Difficile (5x4, 10 coppie)
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection 