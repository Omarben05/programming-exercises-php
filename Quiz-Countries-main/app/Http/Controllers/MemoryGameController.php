<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Country;

class MemoryGameController extends Controller
{
    public function index(Request $request)
    {
        $difficulty = $request->input('difficulty', 'hard');
        if ($difficulty === 'easy') {
            $pairs = 6; $cols = 4; $rows = 3;
        } elseif ($difficulty === 'medium') {
            $pairs = 8; $cols = 4; $rows = 4;
        } else {
            $pairs = 10; $cols = 5; $rows = 4;
        }
        $countries = Country::inRandomOrder()->limit($pairs)->get();
        $cards = [];
        foreach ($countries as $country) {
            $cards[] = [
                'type' => 'flag',
                'country_id' => $country->id,
                'content' => asset('bandiereIMG/' . strtolower($country->alpha2Code) . '.png'),
                'label' => $country->name
            ];
            $cards[] = [
                'type' => 'name',
                'country_id' => $country->id,
                'content' => $country->name,
                'label' => $country->name
            ];
        }
        shuffle($cards);
        return view('memory.index', [
            'cards' => $cards,
            'cols' => $cols,
            'rows' => $rows,
            'pairs' => $pairs,
            'difficulty' => $difficulty
        ]);
    }
} 