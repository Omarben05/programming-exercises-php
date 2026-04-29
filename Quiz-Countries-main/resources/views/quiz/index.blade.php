@extends('welcome')

@section('content')
<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card p-4 mt-4">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <span class="badge bg-info text-dark"><i class="bi bi-list-ol"></i> Domanda {{ $current }} / {{ $total }}</span>
                <span class="badge bg-success"><i class="bi bi-star-fill"></i> Punteggio: {{ $score }}</span>
                <span class="badge bg-danger" id="timer-badge"><i class="bi bi-clock"></i> <span id="timer">15</span>s</span>
            </div>
            <div class="text-center mb-3">
                <img src="{{ $question['flag'] }}" alt="Bandiera di {{ $question['country_name'] }}" style="width:100px; height:auto; border:1px solid #ccc;">
            </div>
            <h4 class="mb-4 text-center">{{ $question['question'] }}</h4>
            <form method="POST" action="{{ route('quiz.answer') }}" id="quiz-form">
                @csrf
                @foreach($question['options'] as $option)
                    <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="answer" id="option_{{ $loop->index }}" value="{{ $option }}" required>
                        <label class="form-check-label" for="option_{{ $loop->index }}">
                            {{ $option }}
                        </label>
                    </div>
                @endforeach
                <input type="hidden" name="correct" value="{{ $question['answer'] }}">
                <input type="hidden" name="country_id" value="{{ $question['country_id'] }}">
                <input type="hidden" name="timeout" id="timeout-flag" value="0">
                <button type="submit" class="btn btn-main btn-lg w-100 mt-3"><i class="bi bi-send"></i> Rispondi</button>
            </form>
        </div>
    </div>
</div>
<script>
let timeLeft = 15;
const timerEl = document.getElementById('timer');
const form = document.getElementById('quiz-form');
const timeoutFlag = document.getElementById('timeout-flag');
const interval = setInterval(() => {
    timeLeft--;
    timerEl.textContent = timeLeft;
    if (timeLeft <= 5) {
        document.getElementById('timer-badge').classList.add('bg-warning');
        document.getElementById('timer-badge').classList.remove('bg-danger');
    }
    if (timeLeft <= 0) {
        clearInterval(interval);
        timeoutFlag.value = 1;
        form.submit();
    }
}, 1000);
form.addEventListener('submit', () => clearInterval(interval));
</script>
@endsection 