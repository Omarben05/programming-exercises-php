class libri :
    def __init__(self, id , nome, autore , editore ):
        self.__id = id 
        self.__nome  = nome 
        self.__autore = autore
        self.__editore = editore

    def to_dict(self):
        return{"id": self.__id , "nome" : self.__nome , "autore": self.__autore, "editore": self.__editore }
        
    