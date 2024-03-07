from repository.clientiRepository import ClientiRepository
from service.clientiService import ClientiService
from unittest import TestCase

class TestClientService(TestCase):

    def testAdaugaClientService(self):

        clientRepository = ClientiRepository()
        clientService = ClientiService(clientRepository)
        clientService.adauga(0, "Bogdan", 1234)

        clienti = clientService.getAllClienti()
        
        self.assertEqual (len(clienti), 1)
        self.assertEqual (clienti[0].getIdClient(), 0)

    def testModificaClientService(self):

        clientRepository = ClientiRepository()
        clientService = ClientiService(clientRepository)
        clientService.adauga(0, "Bogdan", 1234)

        clientService.modifica(0, "Sima", 5678)

        clienti = clientService.getAllClienti()

        self.assertEqual (clienti[0].getNume(), "Sima")

    def testStergeClientService(self):

        clientRepository = ClientiRepository()
        clientService = ClientiService(clientRepository)
        clientService.adauga(0, "Bogdan", 1234)

        clientService.sterge(0)

        clienti = clientService.getAllClienti()

        self.assertEqual (len(clienti), 0)
