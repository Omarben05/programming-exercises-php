<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LibroController;
use App\Http\Controllers\EditoreController;
use App\Http\Controllers\PublisherController;
use App\Http\Controllers\AutoreController;

Route::get('/', function () {
        return view('welcome', ['titolo' => 'Welcome']);
        }) ->name('home');

Route::resource('libri', LibroController::class)->parameters(['libri' => 'libro']);

Route::resource('publishers', PublisherController::class);

Route::resource('editori', EditoreController::class);

// Route::get('editori/{editore}', EditoreController::class . '@show')->name('editori.show');

Route::resource('autori', AutoreController::class)->parameters(['autori' => 'autore']);


