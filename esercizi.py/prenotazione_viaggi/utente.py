class Utenti :
    __nome = ''
    __cognome = ''
    __numero_telefono = ''

    def __init__(self, nome, cognome, numero_telefono):
        self.nome = nome
        self.cognome = cognome
        self.numero_telefono = numero_telefono

    def get_nome(self):
         return self.nome

    def get_cognome(self):
        return self.cognome
    
    def get_numero_telefono(self):
        return self.numero_telefono
