"""
klasa odpowiadajaca za uruchomienie okna gry i wyswietlanie oraz komunikacje z uzytkownikiem
"""

import tkinter as tk
import tkinter.ttk as ttk
from models import Tamagotchi as t
from logic import petMechanics

def start():
    # Init postaci
    postac = None

    # Stworzenie okna
    root = tk.Tk()
    root.geometry("500x400")
    root.title("PJATK Tamagotchi")

    def wyborPostaci():
        # Wybor postaci
        tk.Label(root, text="PJATK Tamagotchi", font=("Arial", 32)).grid(row=0, column=0, columnspan=4)

        # Przyciski wyboru postaci
        tk.Button(root, text="Zwyczajniak", command=lambda: start("z")).grid(row=1, column=0)
        tk.Button(root, text="Grubas", command=lambda: start("g")).grid(row=1, column=1)
        tk.Button(root, text="Dzieciak", command=lambda: start("d")).grid(row=1, column=2)
        tk.Button(root, text="Biznesmen", command=lambda: start("b")).grid(row=1, column=3)

    # Start gry po wybraniu postaci
    def start(wyborPostaci):
        # Przypisanie wybranej postaci
        nonlocal postac
        if wyborPostaci == "z":
            postac = t.Tamagotchi(100, 100, "z")
            print("utworzone zwierzaka z")
        if wyborPostaci == "g":
            postac = t.Tamagotchi(150, 100, "g")
            print("utworzone zwierzaka g")
        if wyborPostaci == "d":
            postac = t.Tamagotchi(100, 100, "d")
            print("utworzone zwierzaka d")
        if wyborPostaci == "b":
            postac = t.Tamagotchi(100, 100, "b")
            print("utworzone zwierzaka b")

        monety = postac.monety

        # Okno gry
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="PJATK Tamagotchi").grid(row=0, column=0, columnspan=4)

        # Pasek najedzenia
        najedzenie_label = ttk.Label(root, text="Najedzenie:")  #napis
        najedzenie_label.grid(column=0, row=1)

        najedzenie_progress = ttk.Progressbar(root, length=200, mode="determinate") #pasek
        najedzenie_progress.grid(column=1, row=1, columnspan=2)
        najedzenie_progress['value'] = postac.najedzenie

        najedzenie_numer = tk.Label(root, text=f"{postac.najedzenie} / {postac.maxNajedzenie}")   #numerycznie
        najedzenie_numer.grid(column=3, row=1)

        # Pasek nudy
        nuda_label = ttk.Label(root, text="Nuda:") #napis
        nuda_label.grid(column=0, row=2)

        nuda_progress = ttk.Progressbar(root, length=200, mode="determinate") #pasek
        nuda_progress.grid(column=1, row=2, columnspan=2)
        nuda_progress['value'] = postac.nuda

        nuda_numer = tk.Label(root, text=f"{postac.nuda} / {postac.maxNuda}")   #numerycznie
        nuda_numer.grid(column=3, row=2)

        # Monety
        label_monety = tk.Label(root, text="Monety:" + str(postac.monety))
        label_monety.grid(row=3, column=0, columnspan=2)

        # Zmiana stanu najedzenia i nudy
        def updateNajedzenieNuda():
            postac.najedzenie = postac.najedzenie - 1
            najedzenie_progress['value'] = postac.najedzenie
            najedzenie_numer.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")
            postac.nuda = postac.nuda + 1
            nuda_progress['value'] = postac.nuda
            nuda_numer.configure(text=f"{postac.nuda} / {postac.maxNuda}")
            root.after(3000, updateNajedzenieNuda)

        updateNajedzenieNuda()

        # Zmiana ilosci monet
        def updateMonety():
            postac.monety = postac.monety + 1
            label_monety.configure(text="Monety:" + str(postac.monety))
            label_monety.grid(row=3, column=0, columnspan=2)
            # tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)
            root.after(6000, updateMonety)

        updateMonety()

        # Sklep z zywnoscia
        tk.Label(root, text="Sklep:", font=("Arial", 26)).grid(row=4, column=0, columnspan=4)
        # Woda
        woda = tk.Button(root, text="Woda +20 -0g", command=lambda: petMechanics.nakarm("woda",postac,najedzenie_progress,label_monety))
        woda.grid(row=5, column=0)

        # Chlep
        chlep = tk.Button(root, text="Chlep +40 -10g", command=lambda: petMechanics.nakarm("chlep",postac,najedzenie_progress,label_monety))
        chlep.grid(row=5, column=1)

        # Ryba
        ryba = tk.Button(root, text="Ryba +60 -20g +5pkt", command=lambda: petMechanics.nakarm("ryba",postac,najedzenie_progress,label_monety))
        ryba.grid(row=5, column=2)

        # Mystery treat
        mysteryTreat = tk.Button(root, text="Mystery treat -50g", command=lambda: petMechanics.nakarm("mystery treat",postac,najedzenie_progress,label_monety))
        mysteryTreat.grid(row=5,column=3)


        #Zabawa
        tk.Label(root, text="Zabawa:", font=("Arial", 26)).grid(row=6, column=0, columnspan=4)
        # Woda
        woda = tk.Button(root, text="Spacer -10nudy",
                         command=lambda: petMechanics.nakarm("woda", postac, najedzenie_progress, label_monety))
        woda.grid(row=7, column=0)

        # Chlep
        chlep = tk.Button(root, text="Zbieranie kasztanów -20nudy",
                          command=lambda: petMechanics.nakarm("chlep", postac, najedzenie_progress, label_monety))
        chlep.grid(row=7, column=1)

        # Ryba
        ryba = tk.Button(root, text="Jazda konno -40nudy",
                         command=lambda: petMechanics.nakarm("ryba", postac, najedzenie_progress, label_monety))
        ryba.grid(row=7, column=2)


    wyborPostaci()
    root.mainloop()