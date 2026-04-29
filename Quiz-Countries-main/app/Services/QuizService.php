<?php

namespace App\Services;

use App\Repositories\CountryRepository;
use App\Repositories\FlagRepository;

class QuizService
{
    protected $countryRepo;
    protected $flagRepo;

    public function __construct(CountryRepository $countryRepo, FlagRepository $flagRepo)
    {
        $this->countryRepo = $countryRepo;
        $this->flagRepo = $flagRepo;
    }

    // Esempio: genera una domanda sulla capitale
    public function generateCapitalQuestion($difficulty = 'easy', $exclude = [])
    {
        $query = $this->countryRepo->all();
        // Filtra per difficoltà
        if ($difficulty === 'easy') {
            $query = $query->where('region', 'Europe');
        } elseif ($difficulty === 'medium') {
            $query = $query->whereIn('region', ['Europe', 'Americas']);
        }
        if (!empty($exclude)) {
            $query = $query->whereNotIn('id', $exclude);
        }
        $countries = $query->shuffle()->take(3);
        $correct = $countries->first();
        $options = $countries->pluck('capital')->shuffle();
        // Percorso bandiera (assumendo flag_code = codice ISO2 minuscolo)
        $flagPath = asset('bandiereIMG/' . strtolower($correct->alpha2Code) . '.png');
        return [
            'question' => "Qual è la capitale di {$correct->name}?",
            'options' => $options,
            'answer' => $correct->capital,
            'country_id' => $correct->id,
            'flag' => $flagPath,
            'country_name' => $correct->name,
        ];
    }
} 