from domeniu.exceptii.validationError import ValidationError
from domeniu.carte import Carte

class CarteValidator:

    def valideaza(self, carte: Carte):

        erori = []

        if len(carte.getTitlu()) == 0:
            erori.append("Cartea nu are titlu!")
        
        if len(carte.getAutor()) == 0:
            erori.append("Cartea nu are autor!")
        
        if len(carte.getDescriere()) == 0:
            erori.append("Cartea nu are descriere!")
        
        if len(erori) > 0:
            raise ValidationError(erori)
