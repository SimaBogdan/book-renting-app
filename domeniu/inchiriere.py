from domeniu.entitate import Entitate

class Inchiriere(Entitate):

    def __init__(self, idInchiriere, idCarte, idClient):

        super().__init__(idInchiriere)
        self.__idCarte = idCarte
        self.__idClient = idClient

    
    def getIdCarte(self):
        return self.__idCarte
    
    def getIdClient(self):
        return self.__idClient
    
    def setIdCarte(self, idCarteNoua):
        self.__idCarte = idCarteNoua
    
    def setIdClient(self, idClientNou):
        self.__idCarte  = idClientNou
    
    def __str__(self):
        return f"Inchiriere: {str(self.getIdEntitate())} IdCarte: {str(self.getIdCarte())} IdClient {str(self.getIdClient())}"