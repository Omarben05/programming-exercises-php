#creazione della classe con gli attributi
class CMedico:
    __codice_fiscale_medico = ''
    __nome = ''
    __cognome = ''
    __campo = ''

# metodo costruttore
    def __init__(self, codice_fiscale_medico, nome, cognome, campo):
        self.codice_fiscale_medico = codice_fiscale_medico
        self.nome = nome
        self.cognome = cognome
        self.campo = campo

# imposto i get per poter richiamare i valori
    def get_codice_fiscale_medico(self):
        return self.codice_fiscale_medico
    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_campo(self):
        return self.campo
    