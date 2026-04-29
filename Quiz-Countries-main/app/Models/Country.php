<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Country extends Model
{
    /** @use HasFactory<\Database\Factories\CountryFactory> */
    use HasFactory;
    protected $fillable = [
        'alpha2Code',
        'alpha3Code',
        'name',
        'capital',
        'region',
        'population',
        'nativeName',
        'area',
    ];
}
