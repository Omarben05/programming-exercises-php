<?php

namespace App\Http\Controllers;

use App\Models\Country;
use Illuminate\Http\Request;

class CountryController extends Controller
{
    public function index()
    {
        $countries = Country::paginate(10);
        return view('countries.index', compact('countries'));
    }

    public function show(Country $country)
    {
        return view('countries.show', compact('country'));
    }
}
