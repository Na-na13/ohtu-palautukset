import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        # Luodaan pankille, viitegeneraattorille ja varastolle oma mock
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "voi", 3)
            if tuote_id == 3:
                return Tuote(3, "mehu", 4)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_tuotteen_ostokset_päättyvät_oikeaan_metodikutsuun(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # maito, 5e
        self.kauppa.lisaa_koriin(2) # voi, 3e
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 8)

    def test_kahden_saman_tuotteen_ostokset_päättyvät_oikeaan_metodikutsuun(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # maito, 5e
        self.kauppa.lisaa_koriin(1) # maito, 5e
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 10)

    def test_varastosta_loppunut_tuotte_ei_päädy_ostoksiin(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # maito, 5e
        self.kauppa.lisaa_koriin(3) # mehu, 4e
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)

    def test_aloita_asiointi_nollaa_ostoskorin(self):
        # aloitetaan ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # maito, 5e

        # aloitetaan ostokset alusta
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) # voi, 3e
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 3)

    def test_jokaisella_ostotapahtumalla_on_oma_viitenumero(self):
        # aloitetaan ensimmäiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan, että viitegeneraattorin metodia uusi on kutsuttu kerran
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        # aloitetaan toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan, että viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        # aloitetaan kolmannet ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan, että viitegeneraattorin metodia uusi on kutsuttu kolme kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_ostoskorista_poistettu_tuote_ei_näy_ostosten_summassa(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # maito, 5e
        self.kauppa.lisaa_koriin(2) # voi, 3e
        self.kauppa.poista_korista(1) # maito, 5e
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 3)