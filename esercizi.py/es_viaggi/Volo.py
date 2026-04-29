class CVolo: 
    __partenza = ''
    __destinazione = ''
    __data = ''
    __ora = ''
    __prezzo = 0

    def __init__ (self, partenza, destinazione, data, ora, prezzo): 
        self.partenza = partenza
        self.destinazione = destinazione
        self.data = data
        self.ora = ora
        self.prezzo = prezzo

    def get_partenza(self):
        return self.partenza
    def get_destinazione(self):
        return self.destinazione
    def get_data(self):
        return self.data
    def get_ora(self):
        return self.ora
    def get_prezzo(self):
        return self.prezzo
    