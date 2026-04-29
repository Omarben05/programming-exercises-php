<?php

namespace App\Http\Controllers;

use App\Models\Book as Libro;
use Illuminate\Http\Request;

class LibroController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // recupera i libri dal modello
        $libri = Libro::all();
        $titolo = 'Libri';
        return view('libri', ['libri' => $libri, 'titolo' => $titolo]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Libro $libro)
    {
        $titolo = 'Dettagli del libro' . $libro->titolo;
        return view('libro', [
            'libro' => $libro,
            'titolo' => $titolo
        ]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Libro $libro)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Libro $libro)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Libro $libro)
    {
        //
    }
}
