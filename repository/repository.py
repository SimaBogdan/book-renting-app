from domeniu.exceptii.duplicateError import DuplicateError
from repository.repositoryException import *

class Repository:

    def __init__(self):
        self.__entitati = []

    def getAll(self):
        return self.__entitati
    
    def getById(self, idEntitate):

        for i in range(0, len(self.__entitati)):

            entitateCurenta = self.__entitati[i]

            if entitateCurenta.getIdEntitate() == idEntitate:

                return entitateCurenta
        
        return None
    
    def gasesteDupaId(self, idEntitate):

        for i in range(0, len(self.__entitati)):

            entitateCurenta = self.__entitati[i]

            if entitateCurenta.getIdEntitate() == idEntitate:

                return i
            
        return None
    
    def adauga(self, entitate):

        if self.getById(entitate.getIdEntitate()) is not None:
            raise DuplicateError("Exista deja o entitate cu id-ul dat!")
        self.__entitati.append(entitate)
    
    def modifica(self, entitateNoua):

        idEntitateNoua = entitateNoua.getIdEntitate()

        if self.gasesteDupaId(idEntitateNoua) is None:
            raise InexistentIdException("Entitatea cu acest id nu exista!")
        else:
            index = self.gasesteDupaId(idEntitateNoua)
            self.__entitati[index] = entitateNoua
    
    def sterge(self, idEntitate):

        if self.gasesteDupaId(idEntitate) is None:
            raise InexistentIdException("Entitatea cu acest id nu exista!")
        else:
            index = self.gasesteDupaId(idEntitate)
            self.__entitati.pop(index)
