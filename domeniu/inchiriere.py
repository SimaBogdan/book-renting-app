from domeniu.entitate import Entitate

class Inchiriere(Entitate):

    #idInchiriere = 0

    def __init__(self, idInchiriere, idCarte, idClient):

        #self.__idInchiriere = Inchiriere.idInchiriere
        super().__init__(idInchiriere)
        self.__idCarte = idCarte
        self.__idClient = idClient
        #Inchiriere.idInchiriere += 1
    
    #def getIdInchiriere(self):
        #return self.__idInchiriere
    
    def getIdCarte(self):
        return self.__idCarte
    
    def getIdClient(self):
        return self.__idClient
    
    #def setIdInchiriere(self, idInchiriereNou):
        #self.__idInchiriere = idInchiriereNou
    
    def setIdCarte(self, idCarteNoua):
        self.__idCarte = idCarteNoua
    
    def setIdClient(self, idClientNou):
        self.__idCarte  = idClientNou
    
    def __str__(self):
        return f"Inchiriere: {str(self.getIdEntitate())} IdCarte: {str(self.getIdCarte())} IdClient {str(self.getIdClient())}"