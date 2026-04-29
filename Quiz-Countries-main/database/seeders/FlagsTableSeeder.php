<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class FlagsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run()
    {
        $flagsPath = public_path('bandiereIMG');
        $files = scandir($flagsPath);

        $data = [];
        foreach ($files as $file) {
            if (in_array(pathinfo($file, PATHINFO_EXTENSION), ['png', 'jpg', 'jpeg', 'gif'])) {
                $countryCode = pathinfo($file, PATHINFO_FILENAME); // es: 'it'
                $data[] = [
                    'name' => strtoupper($countryCode),
                    'image' => 'bandiereIMG/' . $file
                ];
            }
        }

        DB::table('flags')->truncate(); // svuota la tabella prima di inserire
        DB::table('flags')->insert($data);
    }
}
