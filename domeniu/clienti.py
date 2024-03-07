from domeniu.carte import Carte
#from domeniu.entitate import Entitate
from dataclasses import dataclass, field

@dataclass
class Client:
    
    idClient: int
    nume: str
    CNP: int
    inchirieri: list = field(default_factory=lambda: []) 

    #idClient = 0

    #def __init__(self, idClient, nume, CNP):

        #self.__idClient = idClient
        #super().__init__(idClient)
       # self.__nume = nume
        #self.__CNP = CNP
        #self.__inchirieri = []
        #Client.idClient += 1
    '''
    def getIdClient(self):
        return self.__idClient

    def getNume(self):
        return self.__nume
    
    def getCNP(self):
        return self.__CNP
    
    def getInchirieri(self):
        return self.__inchirieri

    def setIdClient(self, idClientNou):
        self.__idClient = idClientNou
    
    def setNume(self, numeNou):
        self.__nume = numeNou
    
    def setCNP(self, CNPNou):
        self.__CNP = CNPNou
    '''
    def __str__(self):

        return f"Client: {self.idClient} Nume: {self.nume} CNP: {self.CNP}"
    
    def adaugaInchirieri(self, carte):

        self.inchirieri.append(carte)
        carte.nrInchirieri = carte.nrInchirieri + 1
        #print(carte.nrInchirieri)
        return carte.nrInchirieri
    
    def stergeInchirieri(self, carteSters):

        self.inchirieri = [carte for carte in self.inchirieri if carte.idCarte != carteSters.idCarte]
        carteSters.nrInchirieri = carteSters.nrInchirieri - 1
        return carteSters.nrInchirieri