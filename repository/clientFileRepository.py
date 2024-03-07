from domeniu.clienti import Client
from repository.clientiRepository import ClientiRepository

class ClientFileRepository(ClientiRepository):

    def __init__(self, numeFisier):
        super().__init__()
        self.__numeFisier = numeFisier
    
    def citesteDinFisier(self):

        try:

            f = open(self.__numeFisier, 'r')
            linie = f.readline().strip("\n")

            while linie != "":

                listaAtribute = linie.split(",")
                idClient = int(listaAtribute[0])
                nume = listaAtribute[1]
                CNP = int(listaAtribute[2])
                client = Client(idClient, nume,  CNP)
                super().adauga(client)
                linie = f.readline().strip("\n")
            
            f.close()
        
        except IOError:

            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)
        
    def scrieInFisier(self):

        try:

            f = open(self.__numeFisier, "w")
            listaClienti = super().getAll()

            for client in listaClienti:

                idClient = client.getIdEntitate()
                nume = client.getNume()
                CNP = client.getCNP()
                linie = str(idClient) + "," + nume + "," + CNP + "\n"
                f.write(linie)
            
            f.close()

        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__numeFisier)
        
    def adaugaFileClient(self, client):

        super().adauga(client)
        self.scrieInFisier()
    
    def modificaFileClient(self, client):

        super().modifica(client)
        self.scrieInFisier()
    
    def stergeFileClient(self, idClient):
        
        super().sterge(idClient)
        self.scrieInFisier()
        