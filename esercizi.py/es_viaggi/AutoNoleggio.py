class CAutoNoleggio:
    __marca = ""
    __modello = ""

    def __init__ (self, marca, modello): 
        self.marca = marca
        self.modello = modello


    def get_marca(self):
        return self.marca
    def get_modello(self):
        return self.modello
    
    