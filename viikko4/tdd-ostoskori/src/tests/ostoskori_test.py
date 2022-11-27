import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote = Tuote("maito", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tavaroiden_maara_oikein_lisaamisen_jalkeen(self):
        self.kori.lisaa_tuote(self.tuote)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_ostoskorin_hinta_oikein_yhden_tuotteen_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.tuote)

        self.assertEqual(self.kori.hinta(), 3)
