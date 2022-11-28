import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("maito", 3)
        self.voi = Tuote("voi", 4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tavaroiden_maara_oikein_lisaamisen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_ostoskorin_hinta_oikein_yhden_tuotteen_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisays_muuttaa_tavaramaaraa_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.voi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisays_muuttaa_yhteishintaa_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.voi)

        self.assertEqual(self.kori.hinta(), 7)

    def test_kahden_saman_tuotteen_lisays_muuttaa_tavaramaaraa_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisays_muuttaa_yhteishintaa_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()[0]

        self.assertEqual(ostokset[0], "maito")
        self.assertEqual(ostokset[1], 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.voi)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_ostoksen_poiston_jalkeen_ostosten_maara_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0][1], 2)

        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0][1], 1)
