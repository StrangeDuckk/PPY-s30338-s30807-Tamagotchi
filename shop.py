import tkinter as tk
import food

def shop(root,postac,food_progress_bar,food_numeric,label_monety):
    # Sklep z zywnoscia
    tk.Label(root, text="Sklep:", font=("Arial", 26)).grid(row=4, column=0, columnspan=4)
    # Woda
    woda = tk.Button(root, text="Woda +20 -0g", command=lambda: food.feed("woda",postac,food_progress_bar,food_numeric,label_monety))
    woda.grid(row=5, column=0)

    # Chlep
    chlep = tk.Button(root, text="Chlep +40 -10g", command=lambda: food.feed("chlep",postac,food_progress_bar,food_numeric,label_monety))
    chlep.grid(row=5, column=1)

    # Ryba
    ryba = tk.Button(root, text="Ryba +60 -20g +5pkt", command=lambda: food.feed("ryba",postac,food_progress_bar,food_numeric,label_monety))
    ryba.grid(row=5, column=2)

    # Mystery treat
    mysteryTreat = tk.Button(root, text="Mystery treat -50g", command=lambda: food.feed("mystery treat",postac,food_progress_bar,food_numeric,label_monety))
    mysteryTreat.grid(row=5,column=3)