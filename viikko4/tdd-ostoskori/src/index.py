# testikoodi tänne jos tarvetta
from tuote import Tuote
from ostoskori import Ostoskori

def main():
    
    maito = Tuote("maito", 3)
    voi = Tuote("voi", 4)
    kori = Ostoskori()

    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(voi)

    print(kori.tavaroita_korissa(), 3)
    print(kori.ostokset())

if __name__ == "__main__":
    main()