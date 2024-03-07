from domeniu.carte import Carte
from unittest import TestCase

class TestCarte(TestCase):

    def setUp(self):
        self.carte0 = Carte(0, "LOTR", "Middle-Earth" , "J R R Tolkien")
        self.carte1 = Carte(1, "Metro 2033", "Post-apocaliptic", "Dmitri Gluhovski")
        self.carte2 = Carte(2, "A wheel of time", "Fantasy", "Robert Jordan")
        self.carte3 = Carte(3, "The Way of Kings", "Trilogie", "Brandon Sanderson")
        self.carte4 = Carte(4, "Game of Thrones", "Grimdark", "George R R Martin")
    
    def tearDown(self):
        pass

    def test_getIdCarte(self):

        self.assertEqual(self.carte0.idCarte, 0)
        self.assertEqual(self.carte1.idCarte, 1)
        self.assertEqual(self.carte2.idCarte, 2)
        self.assertEqual(self.carte3.idCarte, 3)
        self.assertEqual(self.carte4.idCarte, 4)
    
    def test_getTitlu(self):

        self.assertEqual(self.carte0.titlu, "LOTR")
        self.assertEqual(self.carte1.titlu, "Metro 2033")
        self.assertEqual(self.carte2.titlu, "A wheel of time")
        self.assertEqual(self.carte3.titlu, "The Way of Kings")
        self.assertEqual(self.carte4.titlu, "Game of Thrones")
    
    def test_getDescriere(self):


        self.assertEqual(self.carte0.descriere, "Middle-Earth")
        self.assertEqual(self.carte1.descriere, "Post-apocaliptic")
        self.assertEqual(self.carte2.descriere, "Fantasy")
        self.assertEqual(self.carte3.descriere, "Trilogie")
        self.assertEqual(self.carte4.descriere, "Grimdark")
    
    def test_getAutor(self):

        self.assertEqual(self.carte0.autor, "J R R Tolkien")
        self.assertEqual(self.carte1.autor, "Dmitri Gluhovski")
        self.assertEqual(self.carte2.autor, "Robert Jordan")
        self.assertEqual(self.carte3.autor, "Brandon Sanderson")
        self.assertEqual(self.carte4.autor, "George R R Martin")
    
    def test_getNrInchirieri(self):

        self.assertEqual(self.carte0.nrInchirieri, 0)
    
    def test_setIdCarte(self):

        self.carte0.idCarte(5)
        self.assertEqual(self.carte0.getIdCarte(), 5)
    
    def test_setTitlu(self):

        self.carte0.setTitlu("Lord of the Rings")
        self.assertEqual(self.carte0.getTitlu(), "Lord of the Rings")
    
    def test_setDescriere(self):

        self.carte0.setDescriere("Inel")
        self.assertEqual(self.carte0.getDescriere(), "Inel")
    
    def test_setAutor(self):
        
        self.carte0.setAutor("Tolkien")
        self.assertEqual(self.carte0.getAutor(), "Tolkien")
    
    def test_setNrInchirieri(self):

        self.carte0.setNrInchirieri(5)
        self.assertEqual(self.carte0.getNrInchirieri(), 5)
    
    def test___str__(self):

        self.assertEqual(str(self.carte0), "Carte: 0 Titlu: LOTR Descriere: Middle-Earth Autor: J R R Tolkien")

    


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


