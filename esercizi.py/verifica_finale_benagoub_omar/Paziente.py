#creazione della classe con gli attributi
class CPaziente:
    __codice_fiscale_paziente = ''
    __nome = ''
    __cognome = ''

# metodo costruttore
    def __init__(self, codice_fiscale_paziente, nome, cognome):
        self.codice_fiscale_paziente = codice_fiscale_paziente
        self.nome = nome
        self.cognome = cognome

# imposto i get per poter richiamare i valori
    def get_codice_fiscale_paziente(self):
        return self.codice_fiscale_paziente
    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome