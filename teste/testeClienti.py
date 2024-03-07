from domeniu.clienti import Client
from unittest import TestCase
from domeniu.carte import Carte

class TestClient(TestCase):

    def setUp(self):
        self.client0 = Client(0, "Bogdan", 1123456789012)
        self.client1 = Client(1, "Emanuel", 3456789012345)
        self.client2 = Client(2, "Sima", 6789012345678)
        self.client3 = Client(3, "Sergiu", 9012345678901)
        self.client4 = Client(4, "Sebastian", 2345678901234)
    
    def tearDown(self):
        pass

    def test_getIdClient(self):

        self.assertEqual(self.client0.getIdClient(), 0)
        self.assertEqual(self.client1.getIdClient(), 1)
        self.assertEqual(self.client2.getIdClient(), 2)
        self.assertEqual(self.client3.getIdClient(), 3)
        self.assertEqual(self.client4.getIdClient(), 4)
    
    def test_getNume(self):

        self.assertEqual(self.client0.getNume(), "Bogdan")
        self.assertEqual(self.client1.getNume(), "Emanuel")
        self.assertEqual(self.client2.getNume(), "Sima")
        self.assertEqual(self.client3.getNume(), "Sergiu")
        self.assertEqual(self.client4.getNume(), "Sebastian")
    
    def test_getCNP(self):


        self.assertEqual(self.client0.getCNP(), 1123456789012)
        self.assertEqual(self.client1.getCNP(), 3456789012345)
        self.assertEqual(self.client2.getCNP(), 6789012345678)
        self.assertEqual(self.client3.getCNP(), 9012345678901)
        self.assertEqual(self.client4.getCNP(), 2345678901234)
    
    def test_getInchirieri(self):

        self.assertEqual(len(self.client0.getInchirieri()), 0)
    
    def test_setIdClient(self):

        self.client0.setIdClient(5)
        self.assertEqual(self.client0.getIdClient(), 5)
    
    def test_setNume(self):

        self.client0.setNume("Bodi")
        self.assertEqual(self.client0.getNume(), "Bodi")
    
    def test_setCNP(self):

        self.client0.setCNP(2234567890123)
        self.assertEqual(self.client0.getCNP(), 2234567890123)

    def test_addInchirieri(self):

        carte = Carte(0, "LOTR", "Middle-Earth" , "J R R Tolkien")
        self.client0.adaugaInchirieri(carte)
        self.assertEqual(len(self.client0.getInchirieri()), 1)
    
    def test_stergeInchirieri(self):

        carte = Carte(0, "LOTR", "Middle-Earth" , "J R R Tolkien")
        self.client0.adaugaInchirieri(carte)
        self.client0.stergeInchirieri(carte)
        self.assertEqual(len(self.client0.getInchirieri()), 0)
    
    def test___str__(self):

        self.assertEqual(str(self.client0), "Client: 0 Nume: Bogdan CNP: 1123456789012")

    


    '''

    def testCarte():

     carte = Carte("Ion", "Pamant", "Slavici")

     assert carte.getIdCarte() == 0
     assert carte.getTitlu() == "Ion"
     assert carte.getDescriere() == "Pamant"
        assert carte.getAutor() == "Slavici"

    def testCarteSetteri():

    carte = Carte("Ion", "Pamant", "Slavici")

        carte.setDescriere("Iubire")
        assert carte.getDescriere() == "Iubire"

        carte.setAutor("Ioan")
     assert carte.getAutor() == "Ion"

    '''


