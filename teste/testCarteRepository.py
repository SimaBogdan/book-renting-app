from domeniu.carte import Carte
from repository.carteRepository import CarteRepository
from unittest import TestCase

class TestCarteRepository(TestCase):

    def testAdaugaCarte(self):

        carteRepository = CarteRepository()
        carte = Carte(0, "Ion", "Pamant", "Slavici")

        carteRepository.adaugaCarti(carte)
        carti = carteRepository.getAll()

        self.assertEqual(len(carti),  1)
        self.assertEqual(carti[0].getIdCarte(), 0)

    def testModificaCarte(self):

        carteRepository = CarteRepository()
        carte = Carte(0, "Ion", "Pamant", "Slavici")
        carteNoua = Carte(0, "LOTR", "Inel", "Tolkien")
        carteRepository.adaugaCarti(carte)

        carteRepository.modificaCarti(0, "LOTR", "Inel", "Tolkien")
        carti = carteRepository.getAll()

        self.assertEqual(carti[0].getTitlu(), "LOTR")

    def testStergeCarte(self):

        carteRepository = CarteRepository()
        carte = Carte(0, "Ion", "Pamant", "Slavici")
        carteRepository.adaugaCarti(carte)
        
        carteRepository.stergeCarti(0)

        self.assertEqual (len(carteRepository.getAll()), 0)

'''
    carte1 = Carte("Ion", "Pamant", "Slavici")
    carte2 = Carte("Da", "Nu", "DeCe")
    repo = CarteRepository()
    repo.adaugaCarti(carte1)
    repo.adaugaCarti(carte2)
    assert (len(repo.getAll()) == 2)
'''