<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bandiere degli Stati</title>
    <!-- PicoCSS CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css">
    <style>
        /* Modal styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 9999;
            left: 0; top: 0; width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.7);
            justify-content: center;
            align-items: center;
        }
        .modal img {
            max-width: 98vw;
            max-height: 95vh;
            border: 4px solid #fff;
            border-radius: 8px;
            background: #fff;
            box-shadow: 0 0 32px #000a;
            /* Aumenta la dimensione base */
            width: 10vw;
            height: auto;
        }
        .modal.active {
            display: flex;
        }
        .modal-close {
            position: absolute;
            top: 2rem;
            right: 2rem;
            font-size: 2rem;
            color: #fff;
            cursor: pointer;
            background: none;
            border: none;
        }
    </style>
</head>
<body>
<main class="container">
    <h1>Bandiere degli Stati</h1>
    <p>Clicca su una bandiera per ingrandirla.</p>
    <table>
        <thead>
            <tr>
                <th>Nome Stato</th>
                <th>Bandiera</th>
                <th>Sigla</th>
            </tr>
        </thead>
        <tbody>
        @php
            $nomiStati = [
                'AD' => 'Andorra',
                'AE' => 'Emirati Arabi Uniti',
                'AF' => 'Afghanistan',
                'AG' => 'Antigua e Barbuda',
                'AI' => 'Anguilla',
                'AL' => 'Albania',
                'AM' => 'Armenia',
                'AO' => 'Angola',
                'AQ' => 'Antartide',
                'AR' => 'Argentina',
                'AS' => 'Samoa Americane',
                'AT' => 'Austria',
                'AU' => 'Australia',
                'AW' => 'Aruba',
                'AX' => 'Isole Åland',
                'AZ' => 'Azerbaigian',
                'BA' => 'Bosnia ed Erzegovina',
                'BB' => 'Barbados',
                'BD' => 'Bangladesh',
                'BE' => 'Belgio',
                'BF' => 'Burkina Faso',
                'BG' => 'Bulgaria',
                'BH' => 'Bahrein',
                'BI' => 'Burundi',
                'BJ' => 'Benin',
                'BL' => 'Saint-Barthélemy',
                'BM' => 'Bermuda',
                'BN' => 'Brunei',
                'BO' => 'Bolivia',
                'BQ' => 'Paesi Bassi caraibici',
                'BR' => 'Brasile',
                'BS' => 'Bahamas',
                'BT' => 'Bhutan',
                'BV' => 'Isola Bouvet',
                'BW' => 'Botswana',
                'BY' => 'Bielorussia',
                'BZ' => 'Belize',
                'CA' => 'Canada',
                'CC' => 'Isole Cocos (Keeling)',
                'CD' => 'Repubblica Democratica del Congo',
                'CF' => 'Repubblica Centrafricana',
                'CG' => 'Congo',
                'CH' => 'Svizzera',
                'CI' => 'Costa d’Avorio',
                'CK' => 'Isole Cook',
                'CL' => 'Cile',
                'CM' => 'Camerun',
                'CN' => 'Cina',
                'CO' => 'Colombia',
                'CR' => 'Costa Rica',
                'CU' => 'Cuba',
                'CV' => 'Capo Verde',
                'CW' => 'Curaçao',
                'CX' => 'Isola di Christmas',
                'CY' => 'Cipro',
                'CZ' => 'Repubblica Ceca',
                'DE' => 'Germania',
                'DJ' => 'Gibuti',
                'DK' => 'Danimarca',
                'DM' => 'Dominica',
                'DO' => 'Repubblica Dominicana',
                'DZ' => 'Algeria',
                'EC' => 'Ecuador',
                'EE' => 'Estonia',
                'EG' => 'Egitto',
                'EH' => 'Sahara Occidentale',
                'ER' => 'Eritrea',
                'ES' => 'Spagna',
                'ET' => 'Etiopia',
                'FI' => 'Finlandia',
                'FJ' => 'Figi',
                'FK' => 'Isole Falkland',
                'FM' => 'Micronesia',
                'FO' => 'Isole Faroe',
                'FR' => 'Francia',
                'GA' => 'Gabon',
                'GB' => 'Regno Unito',
                'GD' => 'Grenada',
                'GE' => 'Georgia',
                'GF' => 'Guyana Francese',
                'GG' => 'Guernsey',
                'GH' => 'Ghana',
                'GI' => 'Gibilterra',
                'GL' => 'Groenlandia',
                'GM' => 'Gambia',
                'GN' => 'Guinea',
                'GP' => 'Guadalupa',
                'GQ' => 'Guinea Equatoriale',
                'GR' => 'Grecia',
                'GS' => 'Georgia del Sud e Sandwich Australi',
                'GT' => 'Guatemala',
                'GU' => 'Guam',
                'GW' => 'Guinea-Bissau',
                'GY' => 'Guyana',
                'HK' => 'Hong Kong',
                'HM' => 'Isola Heard e Isole McDonald',
                'HN' => 'Honduras',
                'HR' => 'Croazia',
                'HT' => 'Haiti',
                'HU' => 'Ungheria',
                'ID' => 'Indonesia',
                'IE' => 'Irlanda',
                'IL' => 'Israele',
                'IM' => 'Isola di Man',
                'IN' => 'India',
                'IO' => 'Territorio britannico dell’Oceano Indiano',
                'IQ' => 'Iraq',
                'IR' => 'Iran',
                'IS' => 'Islanda',
                'IT' => 'Italia',
                'JE' => 'Jersey',
                'JM' => 'Giamaica',
                'JO' => 'Giordania',
                'JP' => 'Giappone',
                'KE' => 'Kenya',
                'KG' => 'Kirghizistan',
                'KH' => 'Cambogia',
                'KI' => 'Kiribati',
                'KM' => 'Comore',
                'KN' => 'Saint Kitts e Nevis',
                'KP' => 'Corea del Nord',
                'KR' => 'Corea del Sud',
                'KW' => 'Kuwait',
                'KY' => 'Isole Cayman',
                'KZ' => 'Kazakhstan',
                'LA' => 'Laos',
                'LB' => 'Libano',
                'LC' => 'Santa Lucia',
                'LI' => 'Liechtenstein',
                'LK' => 'Sri Lanka',
                'LR' => 'Liberia',
                'LS' => 'Lesotho',
                'LT' => 'Lituania',
                'LU' => 'Lussemburgo',
                'LV' => 'Lettonia',
                'LY' => 'Libia',
                'MA' => 'Marocco',
                'MC' => 'Monaco',
                'MD' => 'Moldavia',
                'ME' => 'Montenegro',
                'MF' => 'Saint-Martin (Parte francese)',
                'MG' => 'Madagascar',
                'MH' => 'Isole Marshall',
                'MK' => 'Macedonia del Nord',
                'ML' => 'Mali',
                'MM' => 'Myanmar',
                'MN' => 'Mongolia',
                'MO' => 'Macao',
                'MP' => 'Isole Marianne Settentrionali',
                'MQ' => 'Martinica',
                'MR' => 'Mauritania',
                'MS' => 'Montserrat',
                'MT' => 'Malta',
                'MU' => 'Mauritius',
                'MV' => 'Maldive',
                'MW' => 'Malawi',
                'MX' => 'Messico',
                'MY' => 'Malesia',
                'MZ' => 'Mozambico',
                'NA' => 'Namibia',
                'NC' => 'Nuova Caledonia',
                'NE' => 'Niger',
                'NF' => 'Isola Norfolk',
                'NG' => 'Nigeria',
                'NI' => 'Nicaragua',
                'NL' => 'Paesi Bassi',
                'NO' => 'Norvegia',
                'NP' => 'Nepal',
                'NR' => 'Nauru',
                'NU' => 'Niue',
                'NZ' => 'Nuova Zelanda',
                'OM' => 'Oman',
                'PA' => 'Panamá',
                'PE' => 'Perù',
                'PF' => 'Polinesia Francese',
                'PG' => 'Papua Nuova Guinea',
                'PH' => 'Filippine',
                'PK' => 'Pakistan',
                'PL' => 'Polonia',
                'PM' => 'Saint Pierre e Miquelon',
                'PN' => 'Pitcairn',
                'PR' => 'Porto Rico',
                'PS' => 'Territori Palestinesi',
                'PT' => 'Portogallo',
                'PW' => 'Palau',
                'PY' => 'Paraguay',
                'QA' => 'Qatar',
                'RE' => 'Riunione',
                'RO' => 'Romania',
                'RS' => 'Serbia',
                'RU' => 'Russia',
                'RW' => 'Ruanda',
                'SA' => 'Arabia Saudita',
                'SB' => 'Isole Solomon',
                'SC' => 'Seychelles',
                'SD' => 'Sudan',
                'SE' => 'Svezia',
                'SG' => 'Singapore',
                'SH' => 'Sant’Elena',
                'SI' => 'Slovenia',
                'SJ' => 'Svalbard e Jan Mayen',
                'SK' => 'Slovacchia',
                'SL' => 'Sierra Leone',
                'SM' => 'San Marino',
                'SN' => 'Senegal',
                'SO' => 'Somalia',
                'SR' => 'Suriname',
                'SS' => 'Sud Sudan',
                'ST' => 'São Tomé e Príncipe',
                'SV' => 'El Salvador',
                'SX' => 'Sint Maarten',
                'SY' => 'Siria',
                'SZ' => 'Eswatini',
                'TC' => 'Isole Turks e Caicos',
                'TD' => 'Ciad',
                'TF' => 'Territori Francesi del Sud',
                'TG' => 'Togo',
                'TH' => 'Thailandia',
                'TJ' => 'Tagikistan',
                'TK' => 'Tokelau',
                'TL' => 'Timor Est',
                'TM' => 'Turkmenistan',
                'TN' => 'Tunisia',
                'TO' => 'Tonga',
                'TR' => 'Turchia',
                'TT' => 'Trinidad e Tobago',
                'TV' => 'Tuvalu',
                'TW' => 'Taiwan',
                'TZ' => 'Tanzania',
                'UA' => 'Ucraina',
                'UG' => 'Uganda',
                'UM' => 'Isole minori degli USA',
                'US' => 'Stati Uniti',
                'UY' => 'Uruguay',
                'UZ' => 'Uzbekistan',
                'VA' => 'Città del Vaticano',
                'VC' => 'Saint Vincent e Grenadine',
                'VE' => 'Venezuela',
                'VG' => 'Isole Vergini Britanniche',
                'VI' => 'Isole Vergini USA',
                'VN' => 'Vietnam',
                'VU' => 'Vanuatu',
                'WF' => 'Wallis e Futuna',
                'WS' => 'Samoa',
                'YE' => 'Yemen',
                'YT' => 'Mayotte',
                'ZA' => 'Sud Africa',
                'ZM' => 'Zambia',
                'ZW' => 'Zimbabwe',
                'EU' => 'Europa',
                'GB-ENG' => 'Inghilterra',
                'GB-NIR' => 'Regno Unito',
                'GB-SCT' => 'Scozia',
                'GB-WLS' => 'Galles',
            ];
        @endphp
        @foreach($Flags as $flag)
            <tr>
                <td>{{ $nomiStati[$flag->name] ?? $flag->name }}</td>
                <td>
                    <img src="{{ asset($flag->image) }}" alt="{{ $flag->name }}" style="width: 48px; height: auto; cursor:pointer;" class="flag-img" data-img="{{ asset($flag->image) }}">
                </td>
                <td>{{ $flag->name }}</td>
            </tr>
        @endforeach
        </tbody>
    </table>
    <!-- Modal -->
    <div class="modal" id="flagModal">
        <button class="modal-close" id="closeModal" aria-label="Chiudi">&times;</button>
        <img src="" alt="Bandiera ingrandita" id="modalImg">
    </div>
</main>
<script>
    document.querySelectorAll('.flag-img').forEach(img => {
        img.addEventListener('click', function() {
            document.getElementById('modalImg').src = this.dataset.img;
            document.getElementById('flagModal').classList.add('active');
        });
    });
    document.getElementById('closeModal').onclick = function() {
        document.getElementById('flagModal').classList.remove('active');
    };
    document.getElementById('flagModal').onclick = function(e) {
        if(e.target === this) this.classList.remove('active');
    };
</script>
</body>
</html>