from pelitehdas import Pelitehdas

def main():
    pelitehdas = Pelitehdas()
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus in pelitehdas.pelit:
            pelitehdas.aloita_peli(vastaus)
        else:
            break

if __name__ == "__main__":
    main()
