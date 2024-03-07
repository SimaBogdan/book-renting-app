from domeniu.inchiriere import Inchiriere
from repository.inchiriereRepository import InchiriereRepository

class InchiriereFileRepository(InchiriereRepository):

    def __init__(self, numeFisier, clientRepository, inchiriereRepository):
        super().__init__(clientRepository, inchiriereRepository)
        self.__numeFisier = numeFisier
        self.citesteDinFisier
    
    def citesteDinFisier(self):

        try:

            with open(self.__numeFisier, 'r') as f:

                linie = f.readline().strip("\n")

                while linie != "":

                    listaAtribute = linie.split(",")
                    idInchiriere = int(listaAtribute[0])
                    idCarte = int(listaAtribute[1])
                    idClient = int(listaAtribute[2])
                    inchiriere = Inchiriere(idInchiriere, idCarte, idClient)
                    super().adauga(inchiriere)
                    linie = f.readline().strip("\n")
        
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)
        
    def scrieInFisier(self):

        try:

            with open(self.__numeFisier, 'w') as f:

                listaInchirieri = super().getAll()

                for inchiriere in listaInchirieri:

                    idInchiriere = inchiriere.getIdEntitate()
                    idCarte = inchiriere.getIdCarte()
                    idClient = inchiriere.getIdClient()
                    linie = str(idInchiriere) + "," + str(idCarte) + "," + str(idClient) + "\n"
                    f.write(linie)
        
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)
        
    def adaugaFileInchiriere(self, inchiriere):

        super().adauga(inchiriere)
        self.scrieInFisier
    
    def modificaFileInchiriere(self, inchiriere):

        super().modifica(inchiriere)
        self.scrieInFisier
    
    def stergeFileInchiriere(self, idInchiriere):

        super().sterge(idInchiriere)
        self.scrieInFisier()