from domeniu.carte import Carte
from domeniu.clienti import Client
from domeniu.inchiriere import Inchiriere
from repository.inchiriereRepository import InchiriereRepository
from repository.carteRepository import CarteRepository
from repository.clientiRepository import ClientiRepository

class InchiriereService:

    def __init__(self, carteRepository: CarteRepository, clientRepository: ClientiRepository):

        #self.__inchirieriRepository = inchirieriRepository
        #self.__inchiriereRepository = inchirieriRepository
        self.__carteRepository = carteRepository
        self.__clientRepository = clientRepository
    
    #def getAll(self):
        #return self.__inchiriereRepository.getAll()

    def inchiriere(self, idCarte, idClient):

        carte = self.__carteRepository.getAll()[self.__carteRepository.getByIdCarti(idCarte)]
        client = self.__clientRepository.getAll()[self.__clientRepository.getByIdClienti(idClient)]

        return client.adaugaInchirieri(carte)
    
    def returnare(self, idCarte, idClient):

        carte = self.__carteRepository.getAll()[self.__carteRepository.getByIdCarti(idCarte)]
        client = self.__clientRepository.getAll()[self.__clientRepository.getByIdClienti(idClient)]

        return client.stergeInchirieri(carte)

    def ordonatAlfabetic(self, nrInchirieri):

        lista = []

        clienti = self.__clientRepository.getAll()

        for client in clienti:

            if len(client.inchirieri) == nrInchirieri:
                
                lista.append(client.nume)
        
        listaNoua = sorted(lista, key=lambda d: (d[1], d[0]))

        return listaNoua
    
    def celeMaiInchiriate(self):

        carti = self.__carteRepository.getAll()

        max = 0
        lista = []

        for carte in carti:

            if carte.nrInchirieri > max:

                max = carte.nrInchirieri
            
        for carte in carti:

            if carte.nrInchirieri == max:

                titlu = carte.titlu
                autor = carte.autor
                descriere = carte.descriere
                dictionar = {'titlu': titlu, 'autor': autor, 'descriere': descriere}
                lista.append(dictionar)

        return lista
    
    def clientiActivi(self):

        lista = []

        clienti = self.__clientRepository.getAll()

        for client in clienti:

            nume = client.nume
            cartiInchiriate = len(client.inchirieri)
            activ = {'nume': nume, 'cartiInchiriate': cartiInchiriate}
            lista.append(activ)
        
        listaNoua = sorted(lista, key=lambda d: d['cartiInchiriate'], reverse=True)
        activi = []
        lungime = int(len(listaNoua)*0.2)

        if(lungime == 0):
            lungime = 1
        
        i = 0

        for pers in listaNoua:

            activi.append(pers['nume'])
            i += 1

            if i >= lungime:
                break
        
        return activi



    '''
    def adauga(self, idCarte, idClient):

        inchiriere = Inchiriere(idCarte, idClient)

        self.__inchirieriRepository.adauga(inchiriere)
    
    def sterge(self, idInchiriere):

        self.__inchirieriRepository.stergeInchiriere(idInchiriere)
    '''
