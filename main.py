#todo -rozdzielic na klasy
#todo -zabawa
#todo - modyfikatyory do jedzenia i nudy
#todo - przegrana
#todo - random eventy
#todo - mystery treat



import tkinter as tk
import tkinter.ttk as ttk
from Tamagotchi import Tamagotchi

def main():
    #Init postaci
    postac = None

    #Stworzenie okna
    root = tk.Tk()
    root.geometry("400x400")
    root.title("PJATK Tamagotchi")


    def wyborPostaci():
        # Wybor postaci
        tk.Label(root, text="PJATK Tamagotchi", font=("Arial", 32)).grid(row=0, column=0,columnspan=4)

        # Przyciski wyboru postaci
        tk.Button(root, text="Zwyczajniak", command=lambda: start("z")).grid(row=1, column=0)
        tk.Button(root, text="Grubas", command=lambda: start("g")).grid(row=1, column=1)
        tk.Button(root, text="Dzieciak", command=lambda: start("d")).grid(row=1, column=2)
        tk.Button(root, text="Biznesmen", command=lambda: start("b")).grid(row=1, column=3)

    #Start gry po wybraniu postaci
    def start(wyborPostaci):
        #Przypisanie wybranej postaci
        nonlocal postac
        if wyborPostaci == "z":
            postac = Tamagotchi(100,100, "z")
            print("utworzone zwierzaka z")
        if wyborPostaci == "g":
            postac = Tamagotchi(150,100, "g")
            print("utworzone zwierzaka g")
        if wyborPostaci == "d":
            postac = Tamagotchi(100,100, "d")
            print("utworzone zwierzaka d")
        if wyborPostaci == "b":
            postac = Tamagotchi(100,100, "b")
            print("utworzone zwierzaka b")

        monety = postac.monety

        #Okno gry
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="PJATK Tamagotchi").grid(row=0, column=0,columnspan=4)

        #Pasek najedzenia
        najedzenie_label = ttk.Label(root, text="Najedzenie:")
        najedzenie_label.grid(column=0, row=1)

        najedzenie_progress = ttk.Progressbar(root, length=200, mode="determinate")
        najedzenie_progress.grid(column=1, row=1,columnspan=2)
        najedzenie_progress['value'] = 0

        #Pasek nudy
        nuda_label = ttk.Label(root, text="Nuda:")
        nuda_label.grid(column=0, row=2)

        nuda_progress = ttk.Progressbar(root, length=200, mode="determinate")
        nuda_progress.grid(column=1, row=2, columnspan=2)
        nuda_progress['value'] = 30

        #Monety
        tk.Label(root, text="Monety:"+str(postac.monety)).grid(row=3, column=0, columnspan=2)

        #Zmiana stanu najedzenia i nudy
        def updateNajedzenieNuda():
            postac.najedzenie = postac.najedzenie - 1
            najedzenie_progress['value'] = postac.najedzenie
            postac.nuda = postac.nuda + 1
            nuda_progress['value'] = postac.nuda
            root.after(3000, updateNajedzenieNuda)

        updateNajedzenieNuda()

        #Zmiana ilosci monet
        def updateMonety():
            postac.monety = postac.monety + 1
            tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)
            root.after(6000, updateMonety)

        updateMonety()

        #Sklep z zywnoscia
        tk.Label(root, text="Sklep:", font=("Arial", 26)).grid(row=4, column=0, columnspan=4)
        #Woda
        woda = tk.Button(root, text="Woda", command=lambda:nakarm("woda")).grid(row=5, column=0)

        #Chlep
        chlep = tk.Button(root, text="Chlep", command=lambda:nakarm("chlep")).grid(row=5, column=1)

        #Ryba
        ryba = tk.Button(root, text="Ryba", command=lambda:nakarm("ryba")).grid(row=5, column=2)

        #Mystery treat
        mysteryTreat = tk.Button(root, text="Mystery treat", command=lambda:nakarm("mystery treat")).grid(row=5, column=3)

        #Nakarmienie zwierzaka
        def nakarm(jedzenie):
            if jedzenie == "woda":
                postac.najedzenie = postac.najedzenie + 20
                najedzenie_progress['value'] = postac.najedzenie
            if jedzenie == "chlep":
                if postac.monety >= 10:
                    postac.monety = postac.monety - 10
                    tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)

                    postac.najedzenie = postac.najedzenie + 40
                    najedzenie_progress['value'] = postac.najedzenie
            if jedzenie == "ryba":
                if postac.monety >= 20:
                    postac.monety = postac.monety - 20
                    tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)

                    postac.najedzenie = postac.najedzenie + 60
                    najedzenie_progress['value'] = postac.najedzenie
            if jedzenie == "mystery treat": #todo
                if postac.monety >= 50:
                    postac.monety = postac.monety - 50
                    tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)

                    pass



    wyborPostaci()
    root.mainloop()

main()