from domeniu.inchiriere import *
from repository.repository import Repository

class InchiriereRepository(Repository):

    def __init__(self, cartiRepository, clientiRepository):

        #self.__inchirieri = []
        super().__init__()
        self.__cartiRepository = cartiRepository
        self.__clientiRepository = clientiRepository
    
    #def getAll(self):

        #return self.__inchirieri
    
    #def gasesteInchiriereDupaId(self, idInchiriere):

        #for i in range(0, len(self.__inchirieri)):

            #inchiriereCurenta = self.__inchirieri[i]

           # if inchiriereCurenta.getIdInchiriere() == idInchiriere:

                #return i

       # return -1
    
    def gasesteInchiriereDupaIdCarteSiIdClient(self, idCarte, idClient):

        for i in range(0, len(self.__entitati)):

            inchiriereCurenta = self.__entitati[i]

            if inchiriereCurenta.getIdCarte() == idCarte and inchiriereCurenta.getIdClient() == idClient:

                return i

        return -1
    
    def existaInchiriereCarte(self, idCarte):

        for i in range(0, len(self.__entitati)):

            inchiriereCurenta = self.__entitati[i]

            if inchiriereCurenta.getIdCarte() == idCarte:

                return True

        return False
    
    def adauga(self, inchiriere):

        #idInchiriere = inchiriere.getIdInchiriere(self)

        idCarte = inchiriere.getIdCarte()
        idClient = inchiriere.getIdClient()

        if self.__clientiRepository.gasesteDupaId(idClient) is None or self.__cartiRepository.gasesteDupaId(idCarte) is None:

            raise KeyError("Clientul sau cartea inchirierii nu exista!")
        
        elif self.gasesteInchiriereDupaIdCarteSiIdClient(idCarte, idClient) is not None:

            #idCarte = inchiriere.getCarteId()
            #idClient = inchiriere.getClientId()

            #if self.__cartiRepository.getCarteId(idCarte) == -1 or self.__clientiRepository.getClientId(idClient) != -1:

            raise KeyError("Clientul a inchiriat cartea!")
            
        #elif self.gasesteInchiriereDupaIdCarteSiIdClient(idCarte, idClient) != -1:

            #raise ValueError("Cartea este deja inchiriata de un client.")
            
        else:

            #self.__inchirieri.append(inchiriere)
            super().adauga(inchiriere)

    def stergeInchiriere(self, idCarte):

        i = 0

        while i < len(self.__entitati):

            inchirereCurenta = self.__entitati[i]

            if inchirereCurenta.getIdCarte() == idCarte:
                
                idInchiriere = inchirereCurenta.getIdEntitate()
                #self.__inchirieri.pop(i)
                super().sterge(idInchiriere)

                i -= 1
            
            i += 1