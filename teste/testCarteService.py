from repository.carteRepository import CarteRepository
from service.cartiService import CartiService
from unittest import TestCase

class TestCarteService(TestCase):

    def testAdaugaCarteService(self):

        carteRepository = CarteRepository()
        carteService = CartiService(carteRepository)
        carteService.adauga(0, "Ion", "Pamant", "Slavici")

        carti = carteService.getAllCarti()
        
        self.assertEqual (len(carti), 1)
        self.assertEqual (carti[0].getIdCarte(), 0)

    def testModificaCarteService(self):

        carteRepository = CarteRepository()
        carteService = CartiService(carteRepository)
        carteService.adauga(0, "Ion", "Pamant", "Slavici")

        carteService.modifica(0, "LOTR", "Inel", "Tolkien")

        carti = carteService.getAllCarti()

        self.assertEqual (carti[0].getTitlu(), "LOTR")

    def testStergeCarteService(self):

        carteRepository = CarteRepository()
        carteService = CartiService(carteRepository)
        carteService.adauga(0, "Ion", "Pamant", "Slavici")

        carteService.sterge(0)

        carti = carteService.getAllCarti()

        self.assertEqual (len(carti), 0)
