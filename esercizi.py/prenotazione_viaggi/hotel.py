class Hotel :
    __Nome = ''
    __indirizzo = ''
    __città = ''
    __numero_telefono = ''

    def __init__(self, Nome, indirizzo, città, numero_telefono):
        self.Nome = Nome
        self.indirizzo = indirizzo
        self.città = città
        self.numero_telefono = numero_telefono

    def get_nome(self):
         return self.Nome

    def get_indirizzo(self):
        return self.indirizzo
    
    def get_città(self):
        return self.città
    
    def get_numero_telefono(self):
        return self.numero_telefono