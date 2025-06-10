import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import random

import events
from activities import activities
from boredom import updateBoredom
from food import updateFood
from models import Tamagotchi as t
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
        postac = t.Tamagotchi(150, 100, characterType.GRUBAS, mnoznikGlodu=3)#3 razy szybciej glodnieje
    elif characterType == characterType.DZIECIAK:
        postac = t.Tamagotchi(100, 100, characterType.DZIECIAK, mnoznikNudy = 5) #5 razy szybciej sie nudzi
    elif characterType == characterType.BIZNESMEN:
        postac = t.Tamagotchi(100, 100, characterType.BIZNESMEN, mnoznikMonet = 3) #3 razy szybciej zarabia z czasu

    #-----------------------------------------------------------------------

    #Display
    #Title
    tk.Label(root, text="PJATK Tamagotchi").grid(row=0, column=0, columnspan=4) #Width = 4 columns

    #Time & Points
    global seconds
    global minutes
    global points
    global frozen
    frozen = False
    global activity_happening
    activity_happening = False

    seconds, minutes, points, prev_second, prev_minute = 0, 0, 0, 0, 0

    time_label = (tk.Label(root, text=f"Time: {minutes} min : {seconds%60} s"))
    time_label.grid(row=0, column=5 )

    def updateTimeAndPointsAndInvokeRandomEvents(seconds, minutes):

        global frozen
        global points
        if not frozen:
            seconds = seconds + 1
            points = points + 1
            if seconds % 60 == 0:
                minutes = minutes + 1*postac.mnoznikMonet
                seconds = 0

            time_label.configure(text=f"Time: {minutes} min : {seconds%60} s")

            # Random events
            if seconds == 20 or seconds == 40 or seconds == 60:
                if random.random() < 0.7:
                    frozen = True
                    events.random_event(root, postac)


        root.after(1000, updateTimeAndPointsAndInvokeRandomEvents, seconds, minutes)

    updateTimeAndPointsAndInvokeRandomEvents(seconds, minutes)

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
        if not frozen:
            postac.monety = postac.monety + 1*postac.mnoznikMonet
            label_monety.configure(text="Monety:" + str(postac.monety))
            label_monety.grid(row=3, column=0, columnspan=2)
            if postac.monety <0:
                postac.czyZginalOdBankructwa = True
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

    #Check for Lose
    def lose_conditions():
        global frozen
        global points
        if not frozen:
            if postac.najedzenie < 0 or postac.najedzenie > postac.maxNajedzenie:
                frozen = True
                messagebox.showinfo('You Lost!', f'You are definitely dead :[ (fullness or emptiness)\nYour score is: {points}')
                startMainGameLoop(root,postac.rodzajPostaci)
            elif postac.CzyZginalOdEventu:
                frozen = True
                messagebox.showinfo('You Lost!', f'You are definitely dead :[ (event)\nYour score is: {points}')
                startMainGameLoop(root, postac.rodzajPostaci)
            elif postac.CzyZginalOdBankructwa:
                frozen = True
                messagebox.showinfo('You Lost!', f'You are definitely dead :[ (bankruptcy)\nYour score is: {points}')
            elif postac.CzyZginalZNudy:
                frozen = True
                messagebox.showinfo('You Lost!', f'You are definitely dead :[ (boredom or heart attack)\nYour score is: {points}')


        root.after(1000, lose_conditions)

    lose_conditions()