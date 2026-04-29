<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Country;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\DB;

class CountriesTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $csv = fopen(database_path('querycountries.csv'), 'r');
        $header = fgetcsv($csv);
        while ($row = fgetcsv($csv)) {
            $data = array_combine($header, $row);
            \App\Models\Country::create([
                'alpha2Code' => $data['alpha2Code'],
                'alpha3Code' => $data['alpha3Code'],
                'name'       => $data['name'],
                'capital'    => $data['capital'],
                'region'     => $data['region'],
                'population' => $data['population'] ?? null,
                'nativeName' => $data['nativeName'] ?? null,
                'area'       => $data['area'] ?? null,
            ]);
        }
        fclose($csv);
    }
}
