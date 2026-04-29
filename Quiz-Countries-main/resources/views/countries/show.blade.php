@extends('layouts.app')

@section('content')
    <div class="card">
        <div class="card-body">
            <h1>{{ $country->name }}</h1>
            <div class="row mt-4">
                <div class="col-md-6">
                    <p><strong>Native Name:</strong> {{ $country->nativeName }}</p>
                    <p><strong>Capital:</strong> {{ $country->capital }}</p>
                    <p><strong>Region:</strong> {{ $country->region }}</p>
                    <p><strong>Population:</strong> {{ number_format($country->population) }}</p>
                    <p><strong>Area:</strong> {{ number_format($country->area) }} km²</p>
                    <p><strong>Alpha-2 Code:</strong> {{ $country->alpha2Code }}</p>
                    <p><strong>Alpha-3 Code:</strong> {{ $country->alpha3Code }}</p>
                </div>
            </div>
            <a href="{{ route('countries.index') }}" class="btn btn-primary">Back to List</a>
        </div>
    </div>
@endsection