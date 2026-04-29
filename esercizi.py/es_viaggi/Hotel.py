class CHotel: 
    __nome = ''
    __citta = ''
    __stelle = 0
    __prezzo = 0



    def __init__(self, nome, citta, stelle, prezzo):
        self.nome = nome
        self.citta = citta
        self.stelle = stelle
        self.prezzo = prezzo

    def get_nome(self):
        return self.nome
    def get_citta(self):
        return self.citta
    def get_stelle(self):
        return self.stelle
    def get_prezzo(self):
        return self.prezzo