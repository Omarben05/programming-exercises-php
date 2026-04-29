@extends('welcome')

@section('content')
<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card p-4 mt-4 text-center">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <span class="badge bg-info text-dark"><i class="bi bi-list-ol"></i> Domanda {{ $current }} / {{ $total }}</span>
                <span class="badge bg-success"><i class="bi bi-star-fill"></i> Punteggio: {{ $score }}</span>
            </div>
            <div class="mb-3">
                <img src="{{ $flag }}" alt="Bandiera" style="width:120px; height:auto; border:1px solid #ccc;">
            </div>
            <h3 class="mb-3">
                @if($isCorrect)
                    <span class="text-success"><i class="bi bi-emoji-smile"></i> Risposta corretta!</span>
                @else
                    <span class="text-danger"><i class="bi bi-emoji-frown"></i> Risposta sbagliata!</span>
                @endif
            </h3>
            <div class="mb-3">
                <strong>La bandiera appartiene a: <span class="badge bg-info text-dark">{{ $correct }}</span></strong>
            </div>
            <form method="GET" action="{{ route('flagquiz.start') }}">
                <button type="submit" class="btn btn-main btn-lg w-100 mt-3"><i class="bi bi-arrow-right-circle"></i> Prossima domanda</button>
            </form>
        </div>
    </div>
</div>
@endsection 