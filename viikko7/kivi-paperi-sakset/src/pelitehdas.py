from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelitehdas:
    def __init__(self):
        self.pelit = {
            'a' : KPSPelaajaVsPelaaja(),
            'b': KPSTekoaly(),
            'c': KPSParempiTekoaly()
        }

    def aloita_peli(self, peli):
        if peli in self.pelit:
            self.pelit[peli].pelaa()
