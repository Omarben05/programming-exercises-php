<?php

namespace App\Http\Controllers;

use App\Models\Autor as Autore;
use Illuminate\Http\Request;

class AutoreController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $autori = Autore::all();
        $titolo = 'Autori';

        return view('autori', compact('autori', 'titolo'));
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
    public function show(Autore $autore)
    {
        $titolo = 'Dettagli dell\'autore: ' . $autore->nome;

        return view('autore', [
            'autore' => $autore,
            'titolo' => $titolo
        ]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Autore $autore)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Autore $autore)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Autore $autore)
    {
        //
    }
}
