import tkinter as tk

from mainGameLoop import startMainGameLoop
from models import Tamagotchi as t

from characterType import characterType

def characterSelectionWindow():
    # Window creation
    root = tk.Tk()
    root.geometry("700x400")
    root.title("PJATK Tamagotchi")

    global postac
    # Buttons
    tk.Button(root, text="Zwyczajniak", command=lambda: startMainGameLoop(root,characterType.ZWYCZAJNIAK)).grid(row=1, column=0)
    tk.Button(root, text="Grubas", command=lambda: startMainGameLoop(root,characterType.GRUBAS)).grid(row=1, column=1)
    tk.Button(root, text="Dzieciak", command=lambda: startMainGameLoop(root,characterType.DZIECIAK)).grid(row=1, column=2)
    tk.Button(root, text="Biznesmen", command=lambda: startMainGameLoop(root,characterType.BIZNESMEN)).grid(row=1, column=3)

    root.mainloop()