<?php

use App\Http\Controllers\CountryController;
use Illuminate\Support\Facades\Route;

Route::get('/', [CountryController::class, 'index'])->name('countries.index');
Route::get('/countries/{country}', [CountryController::class, 'show'])->name('countries.show');
Route::get('/quiz', [App\Http\Controllers\CountryController::class, 'startQuiz'])->name('quiz.start');
Route::get('/training', [App\Http\Controllers\CountryController::class, 'training'])->name('training');
Route::post('/quiz/answer', [App\Http\Controllers\CountryController::class, 'answerQuiz'])->name('quiz.answer');
Route::get('/flagquiz', [App\Http\Controllers\FlagQuizController::class, 'start'])->name('flagquiz.start');
Route::post('/flagquiz/answer', [App\Http\Controllers\FlagQuizController::class, 'answer'])->name('flagquiz.answer');
Route::get('/memorygame', [App\Http\Controllers\MemoryGameController::class, 'index'])->name('memorygame');

