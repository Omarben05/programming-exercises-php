<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\FlagQuizService;
use Illuminate\Support\Facades\Session;
use App\Models\Country;

class FlagQuizController extends Controller
{
    protected $flagQuizService;

    public function __construct(FlagQuizService $flagQuizService)
    {
        $this->flagQuizService = $flagQuizService;
    }

    public function start(Request $request)
    {
        if (!$request->session()->has('flagquiz') || $request->input('restart')) {
            $request->session()->put('flagquiz', [
                'score' => 0,
                'current' => 1,
                'done' => [],
                'difficulty' => $request->input('difficulty', 'easy'),
            ]);
        }
        $quiz = $request->session()->get('flagquiz');
        $question = $this->flagQuizService->generateFlagQuestion($quiz['difficulty'], $quiz['done']);
        $quiz['last_question'] = $question['country_id'];
        $request->session()->put('flagquiz', $quiz);
        return view('flagquiz.index', [
            'question' => $question,
            'difficulty' => $quiz['difficulty'],
            'score' => $quiz['score'],
            'current' => $quiz['current'],
            'total' => 15
        ]);
    }

    public function answer(Request $request)
    {
        $quiz = $request->session()->get('flagquiz');
        $selected = $request->input('answer');
        $correct = $request->input('correct');
        $country_id = $request->input('country_id');
        $quiz['done'][] = $country_id;
        $isCorrect = ($selected === $correct);
        if ($isCorrect) {
            $quiz['score'] += 2;
        }
        $quiz['current']++;
        $request->session()->put('flagquiz', $quiz);
        $country = Country::find($country_id);
        $flagPath = asset('bandiereIMG/' . strtolower($country->alpha2Code) . '.png');
        if ($quiz['current'] > 15) {
            return view('flagquiz.result', [
                'score' => $quiz['score'],
                'total' => 15
            ]);
        }
        return view('flagquiz.feedback', [
            'isCorrect' => $isCorrect,
            'selected' => $selected,
            'correct' => $correct,
            'country' => $country,
            'flag' => $flagPath,
            'score' => $quiz['score'],
            'current' => $quiz['current'] - 1,
            'total' => 15
        ]);
    }
} 