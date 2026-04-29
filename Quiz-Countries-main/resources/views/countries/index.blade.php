@extends('layouts.app')

@section('content')
    <h1>Countries List</h1>
    <div class="row">
        @foreach($countries as $country)
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ $country->name }}</h5>
                        <p class="card-text">
                            Capital: {{ $country->capital }}<br>
                            Region: {{ $country->region }}<br>
                            Population: {{ number_format($country->population) }}
                        </p>
                        <a href="{{ route('countries.show', $country) }}" class="btn btn-primary">Details</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
    {{ $countries->links() }}
@endsection