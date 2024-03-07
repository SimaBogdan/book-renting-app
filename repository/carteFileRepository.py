from domeniu.carte import Carte
from repository.carteRepository import CarteRepository

class CarteFileRepository(CarteRepository):

    def __init__(self, numeFisier):
        super().__init__()
        self.__numeFisier = numeFisier
        self.citesteDinFisier()
    
    def citesteDinFisier(self):

        try:

            f = open(self.__numeFisier, 'r')
            linie = f.readline().strip("\n")

            while linie != "":

                listaAtribute = linie.split(",")
                idCarte = int(listaAtribute[0])
                titlu = listaAtribute[1]
                descriere = listaAtribute[2]
                autor = listaAtribute[3]
                carte = Carte(idCarte, titlu,  descriere, autor)
                super().adauga(carte)
                linie = f.readline().strip("\n")
            
            f.close()
        
        except IOError:

            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)

    def scrieInFisier(self):

        try:

            f = open(self.__numeFisier, "w")
            listaCarti = super().getAll()

            for carte in listaCarti:

                idCarte = carte.getIdEntitate()
                titlu = carte.getTitlu()
                descriere = carte.getDescriere()
                autor = carte.getAutor()
                linie = str(idCarte) + "," + titlu + "," + descriere + "," + autor + "\n"
                f.write(linie)
            
            f.close()

        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)
        
    def adaugaFileCarte(self, carte):

        super().adauga(carte)
        self.scrieInFisier()
    
    def modificaFileCarte(self, carte):

        super().modifica(carte)
        self.scrieInFisier()
    
    def stergeFileCarte(self, idCarte):
        
        super().sterge(idCarte)
        self.scrieInFisier()
        
