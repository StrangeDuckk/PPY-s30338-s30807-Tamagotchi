
class Tamagotchi:
    def __init__(self, maxPoziomNajedzenia, maxPoziomNudy, rodzaj):
        self.najedzenie = maxPoziomNajedzenia//2 #poczatkowo ustawiamy na polowe najedzenia
        self.maxNajedzenie = maxPoziomNajedzenia
        self.nuda = maxPoziomNudy//2 #poczatkowo ustawiamy na polowe nudy
        self.maxNuda = maxPoziomNudy
        self.rodzajPostaci = rodzaj
        self.monety = 20
        self.punkty = 0
        self.zdjedzonePokarmy = []