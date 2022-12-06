class Operaatio:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote

    def suorita(self):
        print("operaatio")

class Summa(Operaatio):
    def __init__(self, sovellus, syote):
        super().__init__(sovellus, syote)
    
    def suorita(self):
        try:
            syote = int(self._syote())
            self._sovellus.plus(syote)
        except ValueError:
            pass

class Erotus(Operaatio):
    def __init__(self, sovellus, syote):
        super().__init__(sovellus, syote)

    def suorita(self):
        try:
            syote = int(self._syote())
            self._sovellus.miinus(syote)
        except ValueError:
            pass

class Nollaus(Operaatio):
    def __init__(self, sovellus, syote):
        super().__init__(sovellus, syote)

    def suorita(self):
        self._sovellus.nollaa()

class Kumoa(Operaatio):
    def __init__(self, sovellus, syote):
        super().__init__(sovellus, syote)

    def suorita(self):
        pass