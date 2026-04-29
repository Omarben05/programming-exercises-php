import sqlite3
import string

# Creazione della classe Database per la gestione del database
class Database:
    def __init__(self, db_name="biblioteca.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crea_tabelle()

    def crea_tabelle(self): 
        """Crea le tabelle nel database se non esistono."""
        self.cursor.execute("""   
        CREATE TABLE IF NOT EXISTS libri (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT UNIQUE,
            autore TEXT,
            disponibile INTEGER DEFAULT 1
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS membri (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE
        )
        """)
        self.conn.commit()

        # Verifica che la tabella sia stata creata
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='libri';")
        if not self.cursor.fetchall():
            print("Errore: La tabella 'libri' non è stata creata correttamente.")
        else:
            print("La tabella 'libri' è stata creata correttamente.")

    def esegui_query(self, query, params=()):
        """Esegue una query sul database."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def leggi_query(self, query, params=()):
        """Legge i dati dal database e restituisce i risultati."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def inserisci_dati_predefiniti(self):
        """Inserisce dati predefiniti (libri e membri) se non esistono già."""
        libri = [
            ("Il nome della rosa", "Umberto Eco"),
            ("1984", "George Orwell"),
            ("Harry Potter e la pietra filosofale", "J.K. Rowling"),
            ("Il Signore degli Anelli", "J.R.R. Tolkien")
        ]
        for titolo, autore in libri:
            try:
                self.esegui_query("INSERT INTO libri (titolo, autore) VALUES (?, ?)", (titolo, autore))
            except sqlite3.IntegrityError:
                pass  # Il libro esiste già, lo ignora

        membri = [
            "Mario Rossi",
            "Luca Bianchi",
            "Giulia Verdi"
        ]
        for nome in membri:
            try:
                self.esegui_query("INSERT INTO membri (nome) VALUES (?)", (nome,))
            except sqlite3.IntegrityError:
                pass  # Il membro esiste già, lo ignora


def check_ridondanza(valore):
    """Verifica se un libro esiste già nel database"""
    conn = sqlite3.connect('biblioteca.db')
    cur = conn.cursor()
    cur.execute("SELECT titolo FROM libri")
    lista = [title[0].lower() for title in cur.fetchall()]
    conn.close()
    
    return valore.lower() not in lista


class Biblioteca:
    def __init__(self):
        self.db = Database()  # Crea il database
        self.db.inserisci_dati_predefiniti()  # Inserisce i dati predefiniti all'avvio

    def aggiungi_libro(self, titolo, autore):
        if not check_ridondanza(titolo):         
            print("Errore: Il libro esiste già.")
        else:
            self.db.esegui_query("INSERT INTO libri (titolo, autore) VALUES (?, ?)", (titolo, autore))
            print(f"Libro '{titolo}' aggiunto con successo.")

    def restituisci_libro(self, titolo):
        libro = self.db.leggi_query("SELECT id FROM libri WHERE titolo = ?", (titolo,))
        if not libro:
            print("Errore: Il libro non esiste.")
            return

        self.db.esegui_query("UPDATE libri SET disponibile = 1 WHERE titolo = ?", (titolo,))
        print(f"Libro '{titolo}' restituito con successo.")

    def registra_membro(self, nome):
        try:
            self.db.esegui_query("INSERT INTO membri (nome) VALUES (?)", (nome,))
            print(f"Membro '{nome}' registrato con successo.")
        except sqlite3.IntegrityError:
            print("Errore: Il membro esiste già.")

    def presta_libro(self, titolo, nome_membro):
        libro = self.db.leggi_query("SELECT id, disponibile FROM libri WHERE titolo = ?", (titolo,))
        if not libro:
            print("Errore: Il libro non esiste.")
            return
        if libro[0][1] == 0:
            print("Errore: Il libro è già in prestito.")
            return
        membro = self.db.leggi_query("SELECT id FROM membri WHERE nome = ?", (nome_membro,))
        if not membro:
            print("Errore: Membro non registrato.")
            return

        self.db.esegui_query("UPDATE libri SET disponibile = 0 WHERE titolo = ?", (titolo,))
        print(f"Libro '{titolo}' prestato a {nome_membro}.")

    def mostra_libri(self):
        libri = self.db.leggi_query("SELECT titolo, autore, disponibile FROM libri")
        print("\nLista dei libri:")
        for titolo, autore, disponibile in libri:
            stato = "Disponibile" if disponibile else "In prestito"
            print(f"- {titolo} di {autore} [{stato}]")

    def mostra_membri(self):
        membri = self.db.leggi_query("SELECT nome FROM membri")
        print("\nLista dei membri:")
        for (nome,) in membri:
            print(f"- {nome}")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Gestione Biblioteca ---")
        print("1. Aggiungi un libro")
        print("2. Registra un membro")
        print("3. Presta un libro")
        print("4. Restituisci un libro")
        print("5. Mostra libri")
        print("6. Mostra membri")
        print("7. Esci")

        scelta = input("Scegli un'opzione: ").strip().translate(str.maketrans("", "", string.punctuation)).translate(str.maketrans("", "", string.ascii_letters))

        if scelta == "1":
            titolo = input("Titolo del libro: ")
            autore = input("Autore del libro: ")
            biblioteca.aggiungi_libro(titolo, autore)
        elif scelta == "2":
            nome = input("Nome del membro: ")
            biblioteca.registra_membro(nome)
        elif scelta == "3":
            titolo = input("Titolo del libro: ")
            nome_membro = input("Nome del membro: ")
            biblioteca.presta_libro(titolo, nome_membro)
        elif scelta == "4":
            titolo = input("Titolo del libro: ")
            biblioteca.restituisci_libro(titolo)
        elif scelta == "5":
            biblioteca.mostra_libri()
        elif scelta == "6":
            biblioteca.mostra_membri()
        elif scelta == "7":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")


if __name__ == "__main__":
    menu()
