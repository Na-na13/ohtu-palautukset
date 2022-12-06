class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = []

    def miinus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self):
        self.tulos = self.edellinen.pop()
        
    #def aseta_arvo(self, arvo):
    #    self.tulos = arvo
