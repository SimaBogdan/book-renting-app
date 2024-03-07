#from domeniu.entitate import Entitate
from dataclasses import dataclass, field

@dataclass
class Carte:

    idCarte: int
    titlu: str
    descriere: str
    autor: str
    nrInchirieri: int = 0
    #idCarte = 0

    #def __init__(self, idCarte, titlu, descriere, autor):

        #self.__idCarte = idCarte
        #super().__init__(idCarte)
        #self.__titlu = titlu
        #self.__descriere = descriere
        #self.__autor = autor
       # self.__nrInchirieri = 0
        #Carte.idCarte += 1
    '''
    def getIdCarte(self):
        return self.__idCarte

    def getTitlu(self):
        return self.__titlu
    
    def getDescriere(self):
        return self.__descriere
    
    def getAutor(self):
        return self.__autor
    
    def getNrInchirieri(self):
        return self.__nrInchirieri

    def setIdCarte(self, idCarteNou):
        self.__idCarte = idCarteNou
    
    def setTitlu(self, titlu):
        self.__titlu = titlu
    
    def setDescriere(self, descriere):
        self.__descriere = descriere
    
    def setAutor(self, autor):
        self.__autor = autor
    
    def setNrInchirieri(self, inchirieri):
        self.__nrInchirieri = inchirieri
    '''
    def __str__(self):

        return f"Carte: {self.idCarte} Titlu: {self.titlu} Descriere: {self.descriere} Autor: {self.autor}"
        