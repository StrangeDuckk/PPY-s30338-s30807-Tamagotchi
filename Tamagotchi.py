from abc import abstractmethod


class Tamagotchi:
    def __init__(self, maxPoziomNajedzenia, maxPoziomNudy, rodzaj):
        self.najedzenie = maxPoziomNajedzenia//2 #poczatkowo ustawiamy na polowe najedzenia
        self.maxNajedzenie = maxPoziomNajedzenia
        self.nuda = maxPoziomNudy//2 #poczatkowo ustawiamy na polowe nudy
        self.maxNuda = maxPoziomNudy
        self.rodzajPostaci = rodzaj

    @abstractmethod
    def specjalnaUmiejetnosc(self) ->None:
        pass

class ZwierzeDefault(Tamagotchi):
    def __init__(self):
        super().__init__(100, 100)

class ZwierzeGrubas(Tamagotchi):
    def __init__(self):
        super().__init__(150, 100)