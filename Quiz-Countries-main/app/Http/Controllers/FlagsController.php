<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Flag;

class FlagsController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $flags = Flag::all();
        return view('flags.index', ['Flags' => $flags]);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('flags.create');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required|max:100',
            'url' => 'required|max:100'
        ]);

        $Flag = new Flag();

        $Flag->title = $request->input('title');
        $Flag->url = $request->input('url');

        $Flag->save();

        return redirect()->route('flags.index')->with('success', 'Flag added successfully');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Flag  $Flag
     * @return \Illuminate\Http\Response
     */
    public function show(Flag $Flag)
    {
        $data = [
            "Flag" => $Flag
        ];

        return view('flags.show', $data);
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Flag  $Flag
     * @return \Illuminate\Http\Response
     */
    public function edit(Flag $Flag)
    {
        $data = [
            "Flag" => $Flag
        ];
  
        return view('flags.edit', $data);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Flag  $Flag
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Flag $Flag)
    {
        $request->validate([
            'title' => 'required|max:100',
            'url' => 'required|max:100'
        ]);
                
        $Flag->title = $request->input('title');
        $Flag->url = $request->input('url');

        $Flag->save();

        return redirect()->route('flags.index')->with('success', 'Flag saved successfully'); 
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Flag  $Flag
     * @return \Illuminate\Http\Response
     */
    public function destroy(Flag $Flag)
    {
        $Flag->delete();

        return redirect()->route('flags.index')->with('success', 'Flag removed successfully'); 
    }
}
