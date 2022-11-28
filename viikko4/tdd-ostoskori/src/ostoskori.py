from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.sisalto = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        tavaroita = 0
        for ostos in self.sisalto:
            tavaroita += ostos.lukumaara()
        
        return tavaroita

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        yhteishinta = 0
        for ostos in self.sisalto:
            yhteishinta += ostos.hinta()
        
        return yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        muutos = False
        i = 0
        while i < len(self.sisalto):
            if self.sisalto[i].tuote == lisattava:
                self.sisalto[i].muuta_lukumaaraa(1)
                muutos = True
                break
            i += 1
        if muutos == False:
            self.sisalto.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        i = 0
        while i < len(self.sisalto):
            if self.sisalto[i].tuote == poistettava:
                self.sisalto[i].muuta_lukumaaraa(-1)
                if self.sisalto[i].lukumaara() == 0:
                    self.sisalto.pop(i)
                break
            i += 1

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.sisalto = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        tuotteet = [(ostos.tuotteen_nimi(), ostos.lukumaara()) for ostos in self.sisalto]
        return tuotteet
