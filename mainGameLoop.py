import tkinter as tk
import tkinter.ttk as ttk

from activities import activities
from boredom import updateBoredom
from food import updateFood
from models import Tamagotchi as t
from logic import petMechanics
from shop import shop


def clearWindow(root):
    for widget in root.winfo_children():
        widget.destroy()

def startMainGameLoop(root,characterType):
    clearWindow(root)

    #Character Init
    global postac

    if characterType == characterType.ZWYCZAJNIAK:
        postac = t.Tamagotchi(100, 100, characterType.ZWYCZAJNIAK)
    elif characterType == characterType.GRUBAS:
        postac = t.Tamagotchi(150, 100, characterType.GRUBAS)
    elif characterType == characterType.DZIECIAK:
        postac = t.Tamagotchi(100, 100, characterType.DZIECIAK)
    elif characterType == characterType.BIZNESMEN:
        postac = t.Tamagotchi(100, 100, characterType.BIZNESMEN)

    #-----------------------------------------------------------------------

    #Display
    #Title
    tk.Label(root, text="PJATK Tamagotchi").grid(row=0, column=0, columnspan=4) #Width = 4 columns

    #Food Display
    #Text
    food_text = ttk.Label(root, text="Najedzenie:")  # napis
    food_text.grid(column=0, row=1)

    #Progress Bar
    food_progress_bar = ttk.Progressbar(root, length=200, mode="determinate") #pasek
    food_progress_bar.grid(column=1, row=1, columnspan=2)
    food_progress_bar['value'] = postac.najedzenie

    #Numeric display
    food_numeric = tk.Label(root, text=f"{postac.najedzenie} / {postac.maxNajedzenie}")  # numerycznie
    food_numeric.grid(column=3, row=1)

    #-----------------------------------------------------------------------

    #Boredom Display
    #Text
    boredom_text = ttk.Label(root, text="Nuda:") #napis
    boredom_text.grid(column=0, row=2)

    #Boredom Bar
    boredom_progress_bar = ttk.Progressbar(root, length=200, mode="determinate") #pasek
    boredom_progress_bar.grid(column=1, row=2, columnspan=2)
    boredom_progress_bar['value'] = postac.nuda

    #Numeric display
    boredom_numeric = tk.Label(root, text=f"{postac.nuda} / {postac.maxNuda}")  # numerycznie
    boredom_numeric.grid(column=3, row=2)

    #-----------------------------------------------------------------------

    #Money Display
    label_monety = tk.Label(root, text="Monety:" + str(postac.monety))
    label_monety.grid(row=3, column=0, columnspan=2)

    # Update money
    def updateMonety():
        postac.monety = postac.monety + 1
        label_monety.configure(text="Monety:" + str(postac.monety))
        label_monety.grid(row=3, column=0, columnspan=2)
        root.after(6000, updateMonety)

    updateMonety()

    #-----------------------------------------------------------------------

    #Update Food
    updateFood(root,postac,food_progress_bar,food_numeric)

    #Update Boredom
    updateBoredom(root,postac,boredom_progress_bar,boredom_numeric)


    #Shop
    shop(root,postac,food_progress_bar,food_numeric,label_monety)

    #Activities
    activities(root,postac,boredom_progress_bar,boredom_numeric)
