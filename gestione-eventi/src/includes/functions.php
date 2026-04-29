<?php 

// Questo file contiene funzioni per gestire gli eventi:
// - caricare gli eventi da un file JSON
// - salvare gli eventi su file JSON
// - generare un ID univoco per ogni evento
// - cercare un evento per ID

// Carica tutti gli eventi dal file events.json e li restituisce come array associativo.
// Se il file non esiste, restituisce un array vuoto.
function load_events() {
    $file = 'events.json'; // Nome del file dove sono salvati gli eventi
    if (file_exists($file)) { // Controlla se il file esiste
        $json = file_get_contents($file); // Legge il contenuto del file come stringa
        return json_decode($json, true); // Converte la stringa JSON in array associativo
    }
    return []; // Se il file non esiste, restituisce un array vuoto
}

// Salva l'array di eventi passato come parametro nel file events.json.
// Sovrascrive il file con i nuovi dati.
function save_events($events) {
    $file = 'events.json'; // Nome del file dove salvare gli eventi
    file_put_contents($file, json_encode($events)); // Converte l'array in JSON e lo scrive nel file
}

// Cerca e restituisce un evento tramite il suo ID.
// Se non trova l'evento, restituisce null.
function get_event_by_id($id) {
    $events = load_events(); // Carica tutti gli eventi
    foreach ($events as $event) { // Scorre ogni evento
        if ($event['id'] == $id) { // Se l'ID corrisponde, restituisce l'evento
            return $event;
        }
    }
    return null; // Se non trova l'evento, restituisce null
}

// Genera un nuovo ID per un evento.
// L'ID è uguale al numero totale di eventi più uno.
function generate_id() {
    $events = load_events(); // Carica tutti gli eventi
    return count($events) + 1; // Restituisce il prossimo ID disponibile
}

