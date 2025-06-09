import tkinter as tk
import boredom

def activities(root,postac,boredom_progress_bar,boredom_numeric):
    tk.Label(root, text="Zabawa:", font=("Arial", 26)).grid(row=6, column=0, columnspan=4)
    # Woda
    woda = tk.Button(root, text="Spacer -10nudy 10s",
                     command=lambda: boredom.play("spacer", postac, boredom_progress_bar, boredom_numeric, buttons,root))
    woda.grid(row=7, column=0)

    # Chlep
    chlep = tk.Button(root, text="Zbieranie kasztanów -20nudy 20s",
                      command=lambda: boredom.play("kasztany", postac, boredom_progress_bar, boredom_numeric, buttons,root))
    chlep.grid(row=7, column=1)

    # Ryba
    ryba = tk.Button(root, text="Jazda konno -40nudy 40s",
                     command=lambda: boredom.play("konie", postac, boredom_progress_bar, boredom_numeric, buttons,root))
    ryba.grid(row=7, column=2)

    buttons = [woda, chlep, ryba]
    return buttons