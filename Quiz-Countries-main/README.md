
---

# Bandiere - Quiz e Giochi sulle Bandiere del Mondo


## Come avviare il progetto

1. **Clona il repository**
   ```bash
   git clone <repo-url>
   cd bandiere
   ```

2. **Installa le dipendenze PHP**
   ```bash
   composer install
   ```

3. **Installa le dipendenze JavaScript**
   ```bash
   npm install
   ```

4. **Configura l'ambiente**
   - Copia `.env.example` in `.env` e configura il database (puoi usare SQLite per test locale).
   - Genera la chiave dell'app:
     ```bash
     php artisan key:generate
     ```

5. **Esegui le migrazioni e i seeder**
   ```bash
   php artisan migrate --seed
   ```

6. **Avvia il server di sviluppo**
   ```bash
   php artisan serve
   ```

7. **Accedi all'applicazione**
   - Vai su [http://localhost:8000](http://localhost:8000)

## Caratteristiche

- **Quiz Classico**: Domande su capitali e bandiere, con scelta della difficoltà (Europa, Americhe, Mondo).
- **Quiz Bandiere**: Riconosci la bandiera e abbinala al paese corretto.
- **Allenamento**: Visualizza e memorizza dati di tutti i paesi (nome, capitale, regione, bandiera, ecc.).
- **Memory Game**: Accoppia bandiere e nomi dei paesi, con diversi livelli di difficoltà.
- **Elenco Bandiere**: Visualizza tutte le bandiere del mondo, con possibilità di ingrandirle.
- **Elenco Paesi**: Tabella con tutti i paesi, sigle, capitali e regioni.
- **Dati aggiornati**: Database popolato tramite seeder e CSV.
- **Frontend moderno**: UI responsive con Tailwind CSS.
- **Facile estensione**: Struttura a servizi e repository per aggiungere nuove modalità di gioco.

---



## Struttura del Progetto

```
├── app/
│   ├── Http/
│   │   └── Controllers/
│   │       ├── Controller.php
│   │       ├── CountryController.php
│   │       ├── FlagQuizController.php
│   │       ├── FlagsController.php
│   │       └── MemoryGameController.php
│   ├── Models/
│   │   ├── Country.php
│   │   ├── Flag.php
│   │   └── User.php
│   ├── Providers/
│   │   └── AppServiceProvider.php
│   ├── Repositories/
│   │   ├── CountryRepository.php
│   │   └── FlagRepository.php
│   └── Services/
│       ├── FlagQuizService.php
│       ├── QuizService.php
│       └── TrainingService.php
├── config/
│   ├── app.php
│   ├── auth.php
│   ├── cache.php
│   ├── database.php
│   ├── filesystems.php
│   ├── logging.php
│   ├── mail.php
│   ├── queue.php
│   ├── services.php
│   └── session.php
├── database/
│   ├── factories/
│   │   ├── CountryFactory.php
│   │   └── UserFactory.php
│   ├── migrations/
│   │   ├── 0001_01_01_000000_create_users_table.php
│   │   ├── 0001_01_01_000001_create_cache_table.php
│   │   ├── 0001_01_01_000002_create_jobs_table.php
│   │   ├── 2025_07_01_082010_create_flags_table.php
│   │   ├── 2025_07_01_104229_create_countries_table.php
│   │   └── 2025_07_13_110657_add_population_native_name_area_to_countries_table.php
│   ├── seeders/
│   │   ├── CountriesTableSeeder.php
│   │   ├── DatabaseSeeder.php
│   │   └── FlagsTableSeeder.php
│   ├── database.sqlite
│   ├── query.sql
│   └── querycountries.csv
├── public/
│   ├── bandiereIMG/
│   │   └── ... (tutte le immagini delle bandiere)
│   ├── .htaccess
│   ├── favicon.ico
│   ├── index.php
│   └── robots.txt
├── resources/
│   ├── css/
│   │   └── app.css
│   ├── js/
│   │   ├── app.js
│   │   └── bootstrap.js
│   └── views/
│       ├── home.blade.php
│       ├── welcome.blade.php
│       ├── countries/
│       │   └── index.blade.php
│       ├── flagquiz/
│       │   ├── feedback.blade.php
│       │   ├── index.blade.php
│       │   └── result.blade.php
│       ├── flags/
│       │   └── index.blade.php
│       ├── memory/
│       │   └── index.blade.php
│       ├── quiz/
│       │   ├── feedback.blade.php
│       │   ├── index.blade.php
│       │   └── result.blade.php
│       └── training/
│           └── index.blade.php
├── routes/
│   ├── console.php
│   └── web.php
├── storage/
│   ├── app/
│   ├── framework/
│   │   ├── cache/
│   │   ├── sessions/
│   │   ├── testing/
│   │   └── views/
│   └── logs/
├── tests/
│   ├── Feature/
│   │   └── ExampleTest.php
│   ├── Unit/
│   │   └── ExampleTest.php
│   └── TestCase.php
├── artisan
├── composer.json
├── composer.lock
├── package.json
├── phpunit.xml
├── vite.config.js
└── README.md
```