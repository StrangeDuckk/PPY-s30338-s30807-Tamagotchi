class Tamagotchi:
    def __init__(self, poziomNajedzenia, poziomNudy):
        self.najedzenie = poziomNajedzenia//2 #poczatkowo ustawiamy na polowe najedzenia
        self.maxNajedzenie = poziomNajedzenia
        self.nuda = poziomNudy//2 #poczatkowo ustawiamy na polowe nudy
        self.maxNuda = poziomNudy