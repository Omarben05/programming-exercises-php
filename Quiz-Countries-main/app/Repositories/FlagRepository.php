<?php

namespace App\Repositories;

use App\Models\Flag;

class FlagRepository
{
    public function all()
    {
        return Flag::all();
    }

    public function getRandom($count = 1)
    {
        return Flag::inRandomOrder()->limit($count)->get();
    }
} 