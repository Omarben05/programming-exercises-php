@extends('welcome')

@section('content')
<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card p-4 mt-4">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <span class="badge bg-info text-dark"><i class="bi bi-list-ol"></i> Domanda {{ $current }} / {{ $total }}</span>
                <span class="badge bg-success"><i class="bi bi-star-fill"></i> Punteggio: {{ $score }}</span>
            </div>
            <div class="text-center mb-3">
                <img src="{{ $question['flag'] }}" alt="Bandiera" style="width:120px; height:auto; border:1px solid #ccc;">
            </div>
            <h4 class="mb-4 text-center">{{ $question['question'] }}</h4>
            <form method="POST" action="{{ route('flagquiz.answer') }}">
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
                <button type="submit" class="btn btn-main btn-lg w-100 mt-3"><i class="bi bi-send"></i> Rispondi</button>
            </form>
        </div>
    </div>
</div>
@endsection 