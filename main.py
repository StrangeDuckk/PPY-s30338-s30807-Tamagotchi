import tkinter as tk
import tkinter.ttk as ttk
from Tamagotchi import Tamagotchi

def main():
    #Init postaci
    postac = None

    #Stworzenie okna
    root = tk.Tk()
    root.geometry("600x600")
    root.title("PJATK Tamagotchi")

    #Wybor postaci
    tk.Label(root, text="PJATK Tamagotchi").pack()

    #Przyciski wyboru postaci
    tk.Button(root, text="Zwyczajniak", command=lambda: start("z")).pack()
    tk.Button(root, text="Grubas", command=lambda: start("g")).pack()
    tk.Button(root, text="Dzieciak", command=lambda: start("d")).pack()
    tk.Button(root, text="Biznesmen", command=lambda: start("b")).pack()

    #
    def start(wyborPostaci):
        nonlocal postac
        if wyborPostaci == "z":
            postac = Tamagotchi(100,100, "z");
            print("utworzone zwierzaka z")
        if wyborPostaci == "g":
            postac = Tamagotchi(150,100, "g");
            print("utworzone zwierzaka g")
        if wyborPostaci == "d":
            postac = Tamagotchi(100,100, "d");
            print("utworzone zwierzaka d")
        if wyborPostaci == "b":
            postac = Tamagotchi(100,100, "b");
            print("utworzone zwierzaka b")




    root.mainloop()

main()