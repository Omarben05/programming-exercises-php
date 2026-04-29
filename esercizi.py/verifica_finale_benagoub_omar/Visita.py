#creazione della classe con gli attributi
class CVisita:
    __idvisita = ''
    __cognome_paziente = ''
    __cognome_medico = ''

# metodo costruttore
    def __init__(self, idvisita, cognome_paziente, cognome_medico):
        self.idvisita = idvisita
        self.cognome_paziente = cognome_paziente
        self.cognome_medico = cognome_medico

# imposto i get per poter richiamare i valori
    def get_idvisita(self):
        return self.idvisita
    def get_cognome_paziente(self):
        return self.cognome_paziente
    def get_cognome_medico(self):
        return self.cognome_medico