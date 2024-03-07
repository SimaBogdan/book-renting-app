#from domeniu.entitate import Entitate
from dataclasses import dataclass, field

@dataclass
class Carte:

    idCarte: int
    titlu: str
    descriere: str
    autor: str
    nrInchirieri: int = 0

    def __str__(self):

        return f"Carte: {self.idCarte} Titlu: {self.titlu} Descriere: {self.descriere} Autor: {self.autor}"
        