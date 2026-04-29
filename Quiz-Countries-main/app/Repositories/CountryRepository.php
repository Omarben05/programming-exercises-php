<?php

namespace App\Repositories;

use App\Models\Country;

class CountryRepository
{
    public function all()
    {
        return Country::all();
    }

    public function getRandom($count = 1)
    {
        return Country::inRandomOrder()->limit($count)->get();
    }
} 