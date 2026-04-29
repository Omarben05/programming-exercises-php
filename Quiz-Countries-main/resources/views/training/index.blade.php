@extends('welcome')

@section('content')
<div class="container mt-5">
    <h2>Modalità Allenamento</h2>
    <div class="card mt-4 text-center">
        <div class="card-body">
            <h4>{{ $country->name }}</h4>
            <div class="mb-3">
                <img src="{{ asset('bandiereIMG/' . strtolower($country->alpha2Code) . '.png') }}" alt="Bandiera di {{ $country->name }}" style="width:100px; height:auto; border:1px solid #ccc;">
            </div>
            <ul class="list-group list-group-flush text-start">
                <li class="list-group-item"><i class="bi bi-translate"></i> <strong>Nome nativo:</strong> <span class="badge badge-custom ms-2">{{ $country->nativeName ?? 'N/A' }}</span></li>
                <li class="list-group-item"><i class="bi bi-geo-alt"></i> <strong>Capitale:</strong> <span class="badge bg-info text-dark ms-2">{{ $country->capital }}</span></li>
                <li class="list-group-item"><i class="bi bi-people"></i> <strong>Popolazione:</strong> <span class="badge bg-success ms-2">{{ $country->population ? number_format($country->population, 0, ',', '.') : 'N/A' }}</span></li>
                <li class="list-group-item"><i class="bi bi-aspect-ratio"></i> <strong>Area:</strong> <span class="badge bg-secondary ms-2">{{ $country->area ? number_format($country->area, 0, ',', '.') . ' km²' : 'N/A' }}</span></li>
                <li class="list-group-item"><i class="bi bi-globe"></i> <strong>Regione:</strong> <span class="badge bg-warning text-dark ms-2">{{ $country->region ?? 'N/A' }}</span></li>
            </ul>
            <form method="GET" action="{{ route('training') }}" class="mt-4">
                <button type="submit" class="btn btn-main btn-lg"><i class="bi bi-arrow-right-circle"></i> Prossimo paese</button>
            </form>
            <a href="{{ route('home') }}" class="btn btn-link mt-2"><i class="bi bi-house-door"></i> Torna alla Home</a>
        </div>
    </div>
</div>
@endsection 