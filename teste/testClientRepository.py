from domeniu.clienti import Client
from repository.clientiRepository import ClientiRepository
from unittest import TestCase

class TestClientRepository(TestCase):

    def testAdaugaClient(self):

        clientRepository = ClientiRepository()
        client = Client(0, "Bogdan", 1234)

        clientRepository.adaugaClienti(client)
        clienti = clientRepository.getAll()

        self.assertEqual (len(clienti), 1)
        self.assertEqual (clienti[0].getIdClient(), 0)

    def testModificaClient(self):

        clientRepository = ClientiRepository()
        client = Client(0, "Bogdan", 1234)
        clientNou = Client(0, "Sima", 5678)
        clientRepository.adaugaClienti(client)

        clientRepository.modificaClienti(0, "Sima", 5678)
        clienti = clientRepository.getAll()

        self.assertEqual (clienti[0].getNume(), "Sima")

    def testStergeClient(self):

        clientRepository = ClientiRepository()
        client = Client(0, "Bogdan", 1234)
        clientRepository.adaugaClienti(client)
        
        clientRepository.stergeClienti(0)

        self.assertEqual (len(clientRepository.getAll()), 0)