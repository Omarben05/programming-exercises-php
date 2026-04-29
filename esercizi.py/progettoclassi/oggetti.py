#oggetti_sondaggio 

class prof:
    def __init__(self, nome, età, altezza, sposato, materie): 
        self.__nome= nome
        self.__età= età
        self.__altezza= altezza
        self.__sposato= sposato
        self.__materie= materie

    def get_nome(self):
        return self.__nome
    def get_età(self):
        return self.__età
    def get_altezza(self):
        return self.__altezza
    def get_sposato(self):
        return self.__sposato
    def get_materie(self):
        return self.__materie 
    
    