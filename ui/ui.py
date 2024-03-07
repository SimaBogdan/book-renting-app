from service.cartiService import CartiService
from service.clientiService import ClientiService
from service.inchiriereService import InchiriereService
from domeniu.carteValidation import CarteValidator

class UI:

    def __init__(self, cartiService: CartiService, clientiService: ClientiService, inchirieriService: InchiriereService):

        self.__cartiService = cartiService
        self.__clientiService = clientiService
        self.__inchirieriService = inchirieriService
        self.__carteValidator = CarteValidator
    
    def adaugaCarte(self):

        try:

            idCarte = int(input("Dati id carte: "))
            titlu = input("Dati titlut cartii: ")
            descriere = input("Dati descrierea cartii: ")
            autor = input("Dati numele autorului cartii: ")
            self.__cartiService.adauga(idCarte, titlu, descriere, autor)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
    
    def adaugaClient(self):

        try:

            idClient = int(input("Dati id client: "))
            nume = input("Dati numele clientului: ")
            CNP = int(input("Dati CNP-ul clientului: "))
            self.__clientiService.adauga(idClient, nume, CNP)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def modificaCarte(self):

        try:

            idCarte = int(input("Dati id-ul cartii: "))
            titluNou = input("Dati titlul nou al cartii: ")
            descriereNoua = input("Dati noua descriere a cartii: ")
            autorNou = input("Dati noul autor al cartii: ")
            self.__cartiService.modifica(idCarte, titluNou, descriereNoua, autorNou)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
    
    def modificaClient(self):

        try:

            idClient = int(input("Dati id-ul clientului: "))
            numeNou = input("Dati noul nume al clientului: ")
            CNPNou = int(input("Dati noul CNP al clientului: "))
            self.__clientiService.modifica(idClient, numeNou, CNPNou)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def stergeCarte(self):

        try:

            idCarte = int(input("Dati id-ul cartii de sters: "))
            self.__cartiService.sterge(idCarte)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
    
    def stergeClient(self):

        try:

            idClient = int(input("Dati id-ul clientului de sters: "))
            self.__clientiService.sterge(idClient)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def cautaCarte(self):

        try:

            cheieCarte = input("Dati id/titlu/descriere/autor pentru cartea pe care o cautati: ")
            return self.__cartiService.cautare(cheieCarte)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def cautaClient(self):

        try:

            cheieClient = input("Dati id/nume/CNP pentru cartea pe care o cautati: ")
            return self.__clientiService.cautare(cheieClient)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
    
    def adaugaInchirieri(self):
        
        try:

            idCarte = int(input("Dati id-ul cartii pe care doriti sa o inchiriati: "))
            idClient = int(input("Dati id-ul clientului care inchiriaza cartea: "))
            return self.__inchirieriService.inchiriere(idCarte, idClient)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
    
    def stergeInchiriere(self):

        try:

            idCarte = int(input("Dati id-ul cartii pe care doriti sa o returnati: "))
            idClient = int(input("Dati id-ul clientului care returneaza cartea: "))
            return self.__inchirieriService.returnare(idCarte, idClient)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def celeMaiInchiriate(self):

        clienti = self.__inchirieriService.celeMaiInchiriate()

        for client in clienti:

            print(client)
    
    def ordonareClienti(self):

        try:

            nrInchirieri = int(input("Numarul de inchirieri: "))
            clienti = self.__inchirieriService.ordonatAlfabetic(nrInchirieri)
            print(clienti)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def clientiActivi(self):

        clienti = self.__inchirieriService.clientiActivi()

        print(clienti)

    def afiseazaCarti(self):

        for entitate in self.__cartiService.getAllCarti():

            print(entitate)
        
    def afseazaClienti(self):

        for entitate in self.__clientiService.getAllClienti():
            print(entitate)

    def afiseazaCartiCautate(self, listaCarte):

        for entitate in listaCarte:

            print(str(entitate))
        
    def afiseazaClientiCautati(self, listaClient):

        for entitate in listaClient:

            print(str(entitate))
        
    def readFileCarte(self):

        carte = self.__cartiService.readFileCarteService()
        print(carte)
    
    def modificaFileCarte(self):

        try:

            idCarte = input("Dati id-ul cartii pe care doriti sa o adaugati fisierului de carti: ")
            titlu = input("Dati titlut cartii: ")
            descriere = input("Dati descrierea cartii: ")
            autor = input("Dati autorul cartii: ")
            self.__cartiService.modificaFileCarteService(idCarte, titlu, descriere, autor)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    def readFileClient(self):

        client = self.__clientiService.readFileClientService()
        print(client)
    
    def modificaFileClient(self):

        try:

            idClient = input("Dati id-ul clientului pe care doriti sa il adaugati fisierului de clienti: ")
            nume = input("Dati numele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            self.__clientiService.modificaFileClientService(idClient, nume, CNP)
        
        except KeyError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
    #def salvare(self):
        #self.__clientiService.save()
        #self.__cartiService.save()

    #def incarcare(self):
        #self.__cartiService.load()
        #self.__clientiService.load()
    '''
    def afiseazaInchirieri(self):

        for entitate in self.__inchirieriService.getAll():

            print(entitate)
        '''
    def printMenu(self):

        print("1. Adauga Carte")
        print("2. Adauga Client")
        print("3. Modifica Carte")
        print("4. Modifica Client")
        print("5. Sterge Carte")
        print("6. Sterge Client")
        print("7. Cauta Carte")
        print("8. Cauta Client")
        print("9. Adauga Inchiriere")
        print("10. Sterge Inchiriere")
        print("11. Cele mai inchiriate")
        print("12. Clienti ordonati alfabetic")
        print("13. Primii 20 la suta clienti activi")
        print("14. Citeste fisier carte")
        print("15. Modifica fisierul de carti")
        print("16. Citeste fisier clienti")
        print("17. Modificati fisierul de clienti")
        print("a. Afiseaza Cartile")
        print("b. Afiseaza Clientii")
        #print("c. Afiseaza Inchirierile")
        print("x. Iesire")
    
    def meniu(self):

        while True:

            self.printMenu()
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.adaugaCarte()
            elif optiune == "2":
                self.adaugaClient()
            elif optiune == "3":
                self.modificaCarte()
            elif optiune == "4":
                self.modificaClient()
            elif optiune == "5":
                self.stergeCarte()
            elif optiune == "6":
                self.stergeClient()
            elif optiune == '7':
               listaCarte = self.cautaCarte()
               self.afiseazaCartiCautate(listaCarte)
            elif optiune == '8':
                listaClient = self.cautaClient()
                self.afiseazaClientiCautati(listaClient)
            elif optiune == '9':
                print(self.adaugaInchirieri())
            elif optiune == '10':
                self.stergeInchiriere()
            elif optiune == '11':
                self.celeMaiInchiriate()
            elif optiune == '12':
                self.ordonareClienti()
            elif optiune == '13':
                self.clientiActivi()
            elif optiune == '14':
                self.readFileCarte()
                #self.salvare()
            elif optiune == '15':
                self.modificaFileCarte()
                #self.incarcare()
            elif optiune == '16':
                self.readFileClient()
            elif optiune == '17':
                self.modificaFileClient()
            elif optiune == "a":
                self.afiseazaCarti()
            elif optiune == "b":
                self.afseazaClienti()
           # elif optiune == 'c':
                #self.afiseazaInchirieri()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati.")