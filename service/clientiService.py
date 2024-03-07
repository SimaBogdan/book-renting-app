from domeniu.clienti import Client
from repository.clientiRepository import ClientiRepository
from repository.clientFileRepository import ClientFileRepository

class ClientiService:

    def __init__(self, clientRepository: ClientiRepository):

        self.__clientRepository = clientRepository
    
    def getAllClienti(self):

        '''
        
        returneaza lista de clienti
        :return: o lista de obiecte de tipul Client
        
        '''

        return self.__clientRepository.getAll()
    
    def adauga(self, idClient, nume, CNP):

        '''
        
        adauga un client
        :param nume: string
        :param CNP: int
        :return:
        
        '''

        client = Client(idClient, nume, CNP)
        self.__clientRepository.adaugaClienti(client)

    def modifica(self, idClient, numeNou, CNPNou):

        '''
        
        modifica un client dupa id
        :param idClient: int
        :param numeNou: string
        :param CNPNou: int
        :return:
        
        '''

        clientNou = Client(idClient, numeNou, CNPNou)
        self.__clientRepository.modificaClienti(idClient, numeNou, CNPNou)
    
    def sterge(self, idClient):

        '''
        
        sterge un client dupa id
        :param idClient: int
        :return:
        
        '''

        self.__clientRepository.stergeClienti(idClient)
    
    def readFileClientService(self):

        return self.__clientRepository.readFileClientRepository()
    
    def modificaFileClientService(self, idClient, nume, CNP):

        return self.__clientRepository.modificaFileClientRepository(idClient, nume, CNP)
    
    #def save(self):
       # self.__repository.save()
    
    #def load(self):
        #self.__repository.load()
    
    def cautare(self, cheieClient):

        client = self.getAllClienti()

        lista = self.__clientRepository.cautareClient(cheieClient, client)

        return lista