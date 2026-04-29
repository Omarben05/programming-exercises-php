@extends('app')


@section('content')


<article>
    <h2>{{ $autore-> nome }} {{ $autore-> cognome }}</h2>
    <h4>Nazionalità : {{$autore -> nazionalita}}</h4>
</article>


@endsection