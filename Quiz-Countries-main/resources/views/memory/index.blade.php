@extends('welcome')

@section('content')
<div class="container py-4">
    <h2 class="mb-2 text-center">Memory Game: Accoppia bandiera e paese</h2>
    <div class="mb-3 text-center">
        <span class="badge bg-primary">Difficoltà: 
            @if($difficulty==='easy') Facile @elseif($difficulty==='medium') Medio @else Difficile @endif
        </span>
        <span class="badge bg-secondary ms-2">Coppie: {{ $pairs }}</span>
    </div>
    <div class="row justify-content-center mb-3">
        <div class="col-auto">
            <span class="badge bg-success fs-5" id="score-badge"><i class="bi bi-star-fill"></i> Punteggio: <span id="score">0</span></span>
        </div>
        <div class="col-auto">
            <span class="badge bg-info text-dark fs-5"><i class="bi bi-arrow-repeat"></i> Tentativi: <span id="moves">0</span></span>
        </div>
    </div>
    <div class="memory-board row row-cols-{{ $cols }} g-3 justify-content-center">
        @foreach($cards as $i => $card)
            <div class="col">
                <div class="memory-card" data-type="{{ $card['type'] }}" data-id="{{ $card['country_id'] }}" tabindex="0">
                    <div class="memory-card-inner">
                        <div class="memory-card-front"></div>
                        <div class="memory-card-back text-center p-2">
                            @if($card['type'] === 'flag')
                                <img src="{{ $card['content'] }}" alt="Bandiera {{ $card['label'] }}" style="width:60px; height:auto;">
                            @else
                                <span class="fw-bold">{{ $card['content'] }}</span>
                            @endif
                        </div>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
    <div class="text-center mt-4">
        <button class="btn btn-main btn-lg" onclick="window.location.reload()"><i class="bi bi-arrow-clockwise"></i> Nuova partita</button>
        <a href="{{ route('home') }}" class="btn btn-link ms-2"><i class="bi bi-house-door"></i> Torna alla Home</a>
    </div>
    <div id="memory-data" data-pairs="{{ $pairs }}" data-difficulty="{{ $difficulty }}"></div>
</div>
<style>
.memory-card {
    perspective: 800px;
    cursor: pointer;
    outline: none;
}
.memory-card-inner {
    position: relative;
    width: 100%;
    height: 90px;
    transition: transform 0.4s;
    transform-style: preserve-3d;
}
.memory-card.flipped .memory-card-inner {
    transform: rotateY(180deg);
}
.memory-card-front, .memory-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 0.5rem;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
}
.memory-card-front {
    background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
}
.memory-card-back {
    transform: rotateY(180deg);
    font-size: 1.1rem;
}
.memory-card.matched .memory-card-inner {
    opacity: 0.5;
    pointer-events: none;
}
</style>
<script>
const dataDiv = document.getElementById('memory-data');
const PAIRS = parseInt(dataDiv.dataset.pairs);
const DIFFICULTY_RAW = dataDiv.dataset.difficulty;
function capitalize(str) { return str.charAt(0).toUpperCase() + str.slice(1); }
const DIFFICULTY = capitalize(DIFFICULTY_RAW);
let firstCard = null, secondCard = null, lock = false, score = 0, moves = 0, matched = 0;
const cards = document.querySelectorAll('.memory-card');
const scoreEl = document.getElementById('score');
const movesEl = document.getElementById('moves');

function resetTurn() {
    firstCard = null;
    secondCard = null;
    lock = false;
}

function updateUI() {
    scoreEl.textContent = score;
    movesEl.textContent = moves;
}

cards.forEach(card => {
    card.addEventListener('click', function() {
        if (lock || this.classList.contains('flipped') || this.classList.contains('matched')) return;
        this.classList.add('flipped');
        if (!firstCard) {
            firstCard = this;
        } else {
            secondCard = this;
            lock = true;
            moves++;
            if (firstCard.dataset.id === secondCard.dataset.id && firstCard.dataset.type !== secondCard.dataset.type) {
                // Match
                setTimeout(() => {
                    firstCard.classList.add('matched');
                    secondCard.classList.add('matched');
                    score += 2;
                    matched++;
                    if (matched === PAIRS) {
                        setTimeout(() => {
                            alert('Complimenti! Hai completato il memory!\nPunteggio: ' + score + '\nTentativi: ' + moves + '\nDifficoltà: ' + DIFFICULTY);
                        }, 400);
                    }
                    updateUI();
                    resetTurn();
                }, 600);
            } else {
                // No match
                setTimeout(() => {
                    firstCard.classList.remove('flipped');
                    secondCard.classList.remove('flipped');
                    score = Math.max(0, score - 1);
                    updateUI();
                    resetTurn();
                }, 900);
            }
            updateUI();
        }
    });
    card.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') this.click();
    });
});
</script>
@endsection 