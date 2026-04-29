<?php

namespace App\Services;

use App\Repositories\CountryRepository;

class FlagQuizService
{
    protected $countryRepo;

    public function __construct(CountryRepository $countryRepo)
    {
        $this->countryRepo = $countryRepo;
    }

    public function generateFlagQuestion($difficulty = 'easy', $exclude = [])
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
        $options = $countries->pluck('name')->shuffle();
        $flagPath = asset('bandiereIMG/' . strtolower($correct->alpha2Code) . '.png');
        return [
            'question' => 'A quale paese appartiene questa bandiera?',
            'options' => $options,
            'answer' => $correct->name,
            'country_id' => $correct->id,
            'flag' => $flagPath,
            'country_name' => $correct->name,
        ];
    }
} 