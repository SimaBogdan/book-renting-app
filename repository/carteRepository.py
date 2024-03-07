from domeniu.carte import Carte
from repository.repository import Repository

class CarteRepository(Carte):

    def __init__(self):

        self.__carti = []
        #super.__init__()
    '''
    def getCarteDupaTitlu(self, titlu):

        for i in range(0, len(self.__entitati)):

            carteCurenta = self.__entitati[i]

            if carteCurenta.getTitlu() == titlu:

                return carteCurenta
        
        return None
    '''
    
    def getAll(self):

        '''
        
        returneaza lista de carti
        :return: o lista de obiecte de tipul Carte
        
        '''
        
        return self.__carti
    
    def getByIdCarti(self, idCarte):

        '''
        
        returneaza cartea cu id-ul dat
        :param idCarte: int
        :return: un obiect de tipul Carte, daca exista unul cu id-ul dat, altfel None
        
        '''

        #for idc in self.__carti:

            #if idc.idCarte == idCarte:

                #return True

        #return False

        for i in range(0, len(self.__carti)):

            carteCurenta = self.__carti[i]

            if carteCurenta.idCarte == idCarte:
                return i
            
        return None
    
    def adaugaCarti(self, carte):

        '''
        
        adauga o carte in lista
        :param carte: obiect de tipul Carte
        :return:
        
        '''

        if self.getByIdCarti(carte.idCarte) == True:

            raise ValueError("Id duplicat")

        self.__carti.append(carte)
    
    def modificaCarti(self, idCarte, titluNou, descriereNoua, autorNou):

        '''
        
        modifica o carte dupa id
        :param idCarte: int
        :param titluNou: string
        :param descriereNoua: string
        :param autorNou: string
        :return:
        
        '''

        if self.getByIdCarti(idCarte) is not None:

            #self.__carti[idCarte].setTitlu(titluNou)
            #self.__carti[idCarte].setDescriere(descriereNoua)
            #self.__carti[idCarte].setAutor(autorNou)

            index = self.getByIdCarti(idCarte)
            carte = self.__carti[index]
            carte.titlu = titluNou
            carte.descriere = descriereNoua
            carte.autor = autorNou
        
        else:

            raise ValueError("Nu exista acest id.")

    
   # def refreshIdCarti(self):

        '''
        
        da refresh la id-urile listei de obiecte de tipul Carte, daca au fost sterse
        :return:
        
        '''

        #for idc in range(0, len(self.__carti)):

            #self.__carti[idc].setIdCarte(idc)
        
        #Carte.id = len(self.__carti)
    
    def stergeCarti(self, idCarte):

        '''
        
        sterge o carte dupa id
        :param idCarte: int
        :return:
        
        '''

        del self.__carti[idCarte]
        #self.refreshIdCarti()
    
    def __str__(self):

        '''
        
        formeaza elementele din lista intr-un string ordonat
        :return: un sir de stringuri cu fiecare obiect 
        
        '''

        str = ""

        for c in self.__carti:

            str += c.__str__() + " "
        
        return str
        
    def cautareCarte(self, cheieCarte, carte):

        rezultateCarti = []

        for carte in self.__carti:

            if cheieCarte in str(carte.idCarte) or cheieCarte in carte.titlu or cheieCarte in carte.descriere or cheieCarte in carte.autor:

                rezultateCarti.append(carte)
        
        return rezultateCarti
    
    def readFileCarteRepository(self):

        with open("carte.txt", 'r') as f:

            carte = f.read()
            #print(carte)
        
        return carte

    def modificaFileCarteRepository(self, idCarte, titlu, descriere, autor):

        with open("carte.txt", 'a')as f:

            f.write(idCarte + "," + titlu + "," + descriere + "," + autor + "\n")
            carte = f.read()
        
        return carte
            
    '''   
    def saveCarte(self):

        listaSave = [carte.__dict__ for carte in self.__carti]
        saveFile = open("carte.txt")
        saveFile.write(str(listaSave))
    
    def loadCarte(self):
        saveFile = open("carte.txt", 'r')
        listaLoad = list(eval(saveFile.read()))
        self.__carti = []

        for loadedCarte in listaLoad:
            carte = Carte(int(loadedCarte["_Carte__id"]), loadedCarte["_Carte__autor"], loadedCarte["_Carte__descriere"], loadedCarte["_Carte__titlu"])
            carte.setNrInchirieri(int(loadedCarte["_Carte__nrInchirieri"]))
            self.__carti.append(carte)
    '''