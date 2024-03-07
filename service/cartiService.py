from domeniu.carte import Carte
from repository.carteRepository import CarteRepository
from repository.carteFileRepository import CarteFileRepository

class CartiService:

    def __init__(self, carteRepository: CarteRepository):

        self.__carteRepository = carteRepository
    
    def getAllCarti(self):

        '''
        
        returneaza lista de carti
        :return: o lista de obiecte de tipul Carte
        
        '''

        return self.__carteRepository.getAll()
    
    def adauga(self, idCarte, titlu, descriere, autor):

        '''
        
        adauga o carte
        :param titlu: string
        :param descriere: string
        :param autor: string
        :return:
        
        '''

        carte = Carte(idCarte, titlu, descriere, autor)
        self.__carteRepository.adaugaCarti(carte)

    def modifica(self, idCarte, titluNou, descriereNoua, autorNou):

        '''
        
        modifica o carte dupa id
        :param idCarte: int
        :param titluNou: string
        :param descriereNoua: string
        :param autorNou: string
        :return:
        
        '''

        carteNoua = Carte(idCarte, titluNou, descriereNoua, autorNou)
        self.__carteRepository.modificaCarti(idCarte, titluNou, descriereNoua, autorNou)
    
    def sterge(self, idCarte):

        '''
        
        sterge o carte dupa id
        :param idCarte: int
        :return:
        
        '''

        self.__carteRepository.stergeCarti(idCarte)
    
    def readFileCarteService(self):

        return self.__carteRepository.readFileCarteRepository()
    
    def modificaFileCarteService(self, idCarte, titlu, descriere, autor):

        return self.__carteRepository.modificaFileCarteRepository(idCarte, titlu, descriere, autor)

    #def save(self):
        #self.__repository.save()
    
    #def load(self):
        #self.__repository.load()
    
    def cautare(self, cheieCarte):

        carte = self.getAllCarti()

        lista = self.__carteRepository.cautareCarte(cheieCarte, carte)

        return lista