class Prodotti:
    def __init__(self, codice_prodotto, nome, prezzo, quantita):
        self.codice_prodotto = codice_prodotto
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def get_codice_prodotto(self):
        return self.codice_prodotto

    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo

    def get_quantita(self):
        return self.quantita
