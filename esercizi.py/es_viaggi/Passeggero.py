class CPasseggero:
    __nome = ''
    __cognome = ''


    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome