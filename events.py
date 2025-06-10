import tkinter as tk
from random import random
from tkinter import messagebox
import mainGameLoop
from characterType import characterType


def random_event(root, postac):
    r = random()
    # ------------- random eventy pozytywne --------------
    if r < 0.4:
        ran = random()
        if ran <=0.5:
            message = messagebox.showinfo('Random Event Pozytywny', 'Znalezienie 10 monet :3')
            postac.monety +=10
        elif 0.5 < ran <= 0.75:
            message = messagebox.showinfo('Random Event Pozytywny', 'Złamanie lapy zwierzaka \n(nuda + 20), ale chociaz 20 monet odszkodowania :/')
            postac.monety += 20
            postac.nuda += 20
        elif 0.75 < ran <= 0.90:
            ran2 = random()
            if ran2 <=0.5:
                message = messagebox.showinfo('Random Event Pozytywny', 'Znalezienie Grzybkow Halucynkow, \nokazalo sie ze zwierzak jest na nie uczulony, \ninstant smierc :|')
            else:
                message = messagebox.showinfo('Random Event Pozytywny', 'Znalezienie Grzybkow Halucynkow, zwierzak swietnie sie bawil z grzybkami, \nchce wiecej i staje sie uzalezniony, \njednak nie ma swojego dilera wiec szybko wraca do normy, \nnuda - 75% obecnego poziomu zabawy')
                postac.nuda -= postac.nuda*0.75
        else:
            message = messagebox.showinfo('Random Event Pozytywny','Zwierzak otrzymuje spadek od babci z Ameryki, \n+ 250 monet :D')
            postac.monety += 250
    # --------------------- random eventy negatywne ---------------------
    elif 0.4 <=r < 0.8:
        ran = random()
        if ran <=0.5:
            message = messagebox.showwarning('Random Event Negatywny','Otwarte zlamanie nogi i prywatna wizyta u lekarza, \nnuda + 25, \nmonety - 10, \n(jesli zwierze jest grubasem, instant smierc, i tak predzej umrze niz wyleczy ta lape wiec po co przedluzac jego cierpienie :) )')
            if postac.rodzajPostaci == characterType.GRUBAS:
                postac.CzyZginalOdEventu = True
            postac.monety -= 10
            postac.nuda += 25
        elif 0.5 < ran <= 0.75:
            ran2 = random()
            if ran2 <=0.5:
                message = messagebox.showwarning('Random Event Negatywny','Przejscie na czerwonym swietle, \nna szczescie nie bylo policji, \n\nale byl samochod,\ninstant smierc\nbylo uwazac na swiatlach')
                postac.CzyZginalOdEventu = True
            else:
                message = messagebox.showwarning('Random Event Negatywny','Przejscie na czerwonym swietle, \ntym razem trafila sie policja, bo oni zawsze sa tam gdzie ich nie potrzeba :/\nale zawsze mogl byc zamiast nich samochod\nmandat -20 moent')
                postac.monety -=20
        elif 0.75 < ran <= 0.90:
            ran2 = random()
            if ran2 <=0.5:
                message = messagebox.showwarning('Random Event Negatywny', 'Zwierzak wypil kociolek Panoramixa,\nprzydaloby sie skontrolowac jego znajomych, ale teraz to juz nei bedzie potrzebne\ninstant smierc')
                postac.CzyZginalOdEventu = True
            else:
                message = messagebox.showwarning('Random Event Negatywny', 'Zwierzak wypil kociolek Panoramixa,\nprzydaloby sie skontrolowac jego znajomych, moze sie jeszcze przydac, \nteraz zwierzak ma zatrucie pokamowe i trzeba dac taksowkarzowi na pranie tapicerki :|\njedzenie zwierzaka to 10% calkowitej wartosci\n-30 monet')
                postac.najedzenie = postac.maxNajedzenie*0.1
                postac.monety -= 30
        else:
            message = messagebox.showwarning('Random Event Negatywny','Dowod zwierzaka stracil waznosc a mial zaciagnieta pozyczke na 200 moent,\nbank dba o swoje interesy i chce natychmiastowego zwrotu pozyczki\n -200 monet')
            postac.monety -= 200
    # --------------------- apokalipsy ------------------------
    else:
        def apokalipsaZombie():
            ran2 = random()
            if ran2 <= 0.5:
                message = messagebox.showerror('Random Event Apokalipsy',
                                               'Nastapila Apokalipsa Zombie\nzwierzak wykazal sie wytrzymaloscia i anielska cierpliwoscia w szczegolnosci do Eugenea i pomogl im dostac sie Waszyngtonu\nzwierzak dostaje 100 moent za chronienie \'najmadrzejszego\' czlonka ekipy\nwszystko wraca do normy')
                postac.monety += 100
            else:
                message = messagebox.showerror('Random Event Apokalipsy',
                                               'Nastapila Apokalipsa Zombie\nzwierzak sie staral ale i tak zombie Grzesio staral sie bardziej\n zwierzak zostal zjedzony w bardzo brutalny sposob\n instant smierc')
                postac.CzyZginalOdEventu = True
        ran = random()
        if ran <=0.4:
            apokalipsaZombie()
        elif 0.4 < ran <= 0.6:
            ran2 = random()
            if ran2 <=0.5:
                apokalipsaZombie()
            else:
                message = messagebox.showerror('Random Event Atomowka',
                                               'Izrael wystrzelil nie ta bombe ktora chcial a nie oszukujmy sie\npo wybuchu bomby atomowej jaka oni dysponuja to zostaje nam tylko owinac sie w przescieradlo i czolgac sie w strone cmentarza\nnikt nie przezyl, a skoro nikt to zwierzak tym bardziej,\ninstant smierc')
                postac.CzyZginalOdEventu = True
        else:
            ran2 = random()
            if ran2<=0.5:
                message = messagebox.showerror('Random Event Sauron i Armia',
                                               'Sauron zaatakowal,\nwklad zwierzaka w kampanie majaca na celu zniszczenie pierscienia okazal sie nieoceniony\n(przeniosl go we wlasnym brzuchu po zjedzeniu go :| )\nw podziece elfy wyplacaja mu 100 monet (sknery)')
                postac.monety += 100
            else:
                message = messagebox.showerror('Random Event Sauron i Armia',
                                               'Sauron zaatakowal,\nwklad zwierzaka w kampanie majaca na celu zniszczenie pierscienia okazal sie nie istniec\nna samym poczatku marszu rozdeptal go randomowy ork\ninstant smierc')
                postac.CzyZginalOdEventu = True

    mainGameLoop.frozen = False