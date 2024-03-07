from domeniu.carte import Carte
#from domeniu.entitate import Entitate
from dataclasses import dataclass, field

@dataclass
class Client:
    
    idClient: int
    nume: str
    CNP: int
    inchirieri: list = field(default_factory=lambda: [])

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