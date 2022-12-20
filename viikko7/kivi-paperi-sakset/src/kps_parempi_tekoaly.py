from tekoaly_parannettu import TekoalyParannettu
from kps_peli import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)
        self._aloitussiirto = True
        self._ekan_edellinen = ""

    def _ekan_siirto(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._ekan_edellinen = ekan_siirto
        if self._aloitussiirto == True:
            self._aloitussiirto == False
        return ekan_siirto

    def _tokan_siirto(self):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        if self._aloitussiirto == False:
            self._tekoaly.aseta_siirto(self._ekan_edellinen)
        return tokan_siirto
