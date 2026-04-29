@extends('welcome')

@section('content')
<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card p-4 mt-5 text-center">
            <h2 class="mb-4">Quiz Bandiere Terminato!</h2>
            <div class="alert {{ $score > 18 ? 'alert-success' : 'alert-warning' }} mt-2">
                @if($score > 18)
                    <h3><i class="bi bi-trophy-fill text-warning"></i> Congratulazioni! Ottimo risultato!</h3>
                @else
                    <h3><i class="bi bi-emoji-neutral"></i> Ritenta, puoi fare di meglio!</h3>
                @endif
                <div class="mt-2">
                    <span class="badge bg-success fs-5"><i class="bi bi-star-fill"></i> Punteggio finale: {{ $score }} / {{ $total * 2 }}</span>
                </div>
            </div>
            <form method="GET" action="{{ route('flagquiz.start') }}">
                <input type="hidden" name="restart" value="1">
                <button type="submit" class="btn btn-main btn-lg w-100 mt-3"><i class="bi bi-arrow-repeat"></i> Ricomincia Quiz</button>
            </form>
            <a href="{{ route('home') }}" class="btn btn-link mt-3"><i class="bi bi-house-door"></i> Torna alla Home</a>
        </div>
    </div>
</div>
@endsection 