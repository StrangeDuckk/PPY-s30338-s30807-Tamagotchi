
class Tamagotchi:
    def __init__(self, maxPoziomNajedzenia, maxPoziomNudy, rodzaj, mnoznikMonet=1, mnoznikGlodu=1,mnoznikNudy=1):
        self.najedzenie = maxPoziomNajedzenia//2 #poczatkowo ustawiamy na polowe najedzenia
        self.maxNajedzenie = maxPoziomNajedzenia
        self.nuda = maxPoziomNudy//2 #poczatkowo ustawiamy na polowe nudy
        self.maxNuda = maxPoziomNudy
        self.rodzajPostaci = rodzaj
        self.monety = 20
        self.punkty = 0
        self.mnoznikMonet = mnoznikMonet
        self.mnoznikGlodu = mnoznikGlodu
        self.mnoznikNudy = mnoznikNudy
        self.zjedzonePokarmy = []
        self.CzyZginalZGlodu = False
        self.CzyZginalOdEventu = False
        self.CzyZginalOdBankructwa = False
        self.CzyZginalZNudy = False
        self.maxWynikSesja = self.odczytMaxWynikSesja()

    def odczytMaxWynikSesja(self):
        with open("maxWynik.txt") as f:
            return int(f.readline())

    def zapisMaxWynikSesja(self):
        with open("maxWynik.txt", "w") as f:
            f.write(str(self.punkty))