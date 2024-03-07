from domeniu.clienti import Client
from repository.repository import Repository
from domeniu.carte import Carte

class ClientiRepository:

    def __init__(self):

        self.__clienti = []
        #super().__init__()
    
    def getAll(self):

        '''
        
        returneaza lista de clienti
        :return: o lista de obiecte de tipul Client
        
        '''
        
        return self.__clienti
    
    def getByIdClienti(self, idClient):

        '''
        
        returneaza clientul cu id-ul dat
        :param idClient: int
        :return: un obiect de tipul Client, daca exista unul cu id-ul dat, altfel None
        
        '''
        
        for i in range(0, len(self.__clienti)):

            clientCurent = self.__clienti[i]

            if clientCurent.idClient == idClient:

                return i
        
        return None
        

        #for idc in self.__clienti:

            #if idc.getIdClient() == idClient:

                #return True

        #return False
    
    def adaugaClienti(self, client):

        '''
        
        adauga un client in lista
        :param client: obiect de tipul Client
        :return:
        
        '''

        if self.getByIdClienti(client.idClient) == True:

            raise ValueError("Id duplicat")

        self.__clienti.append(client)
    
    def modificaClienti(self, idClient, numeNou, CNPNou):

        '''
        
        modifica un client dupa id
        :param idClient: int
        :param numeNou: string
        :param CNPNou: int
        :return
        
        '''

        if self.getByIdClienti(idClient) is not None:

            index = self.getByIdClienti(idClient)
            carte = self.__clienti[index]
            carte.nume = numeNou
            carte.CNP = CNPNou
        
        else:

            raise ValueError("Nu exista acest id.")

    #def refreshIdClienti(self):

        '''
        
        da refresh la id-urile listei de obiecte de tipul Client, daca au fost sterse
        :return:
        
        '''

       # for idc in range(0, len(self.__clienti)):

            #self.__clienti[idc].setIdClient(idc)
        
        #Client.id = len(self.__clienti)
    
    def stergeClienti(self, idClient):

        '''
        
        sterge un client dupa id
        :param idClient: int
        :return:
        
        '''

        del self.__clienti[idClient]
       # self.refreshIdClienti()
    
    def __str__(self):

        '''
        
        formeaza elementele din lista intr-un string ordonat
        :return: un sir de stringuri cu fiecare obiect
        
        '''

        str = ""

        for c in self.__clienti:

            str += c.__str__() + " "
        
        return str
    
    def cautareClient(self, cheieClient, client):

        rezultateClient = []

        for client in self.__clienti:

            if cheieClient in str(client.idClient) or cheieClient in client.nume or cheieClient in str(client.CNP):

                rezultateClient.append(client)
        
        return rezultateClient
    
    def readFileClientRepository(self):

        with open("client.txt", 'r') as f:

            client = f.read()
            #print(carte)
        
        return client

    def modificaFileClientRepository(self, idClient, nume, CNP):

        with open("client.txt", 'a')as f:

            f.write(idClient + "," + nume + "," + CNP + "\n")
            client = f.read()
        
        return client
        
    '''
    def saveClient(self):

        listaSave = []

        for client in self.__clienti:
            inchirieri = [carte.__dict__ for carte in client.getInchirieri()]
            clientSave = client.__dict__
            clientSave["_Client__inchiriere"] = inchirieri
            listaSave.append(clientSave)
        
        saveFile = open("client.txt")
        saveFile.write(str(listaSave))
    
    def loadClient(self):
        saveFile = open("client.txt", 'r')
        listaLoad = list(eval(saveFile.read()))
        self.__clienti = []

        for loadedClient in listaLoad:
            client = Client(int(loadedClient["_Client__id"]), loadedClient["_Client__nume"], loadedClient["_Client__CNP"])

            for loadedCarte in loadedClient["_Client__inchiriere"]:

                carte = Carte(int(loadedCarte["_Carte__id"]), loadedCarte["_Carte__autor"], loadedCarte["_Carte__descriere"], loadedCarte["_Carte__titlu"])
                client.adaugaInchirieri(carte)
        
        self.__clienti.append(client)
    '''