<?php

namespace App\Services;

use App\Repositories\CountryRepository;

class TrainingService
{
    protected $countryRepo;

    public function __construct(CountryRepository $countryRepo)
    {
        $this->countryRepo = $countryRepo;
    }

    public function getRandomCountry()
    {
        return $this->countryRepo->getRandom(1)->first();
    }
} 