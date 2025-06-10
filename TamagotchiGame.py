import sys
import random

from PIL import Image, ImageTk
import tkinter as tk
import tkinter.ttk as ttk
from characterType import characterType
from models import Tamagotchi as t
from tkinter import messagebox

class TamagotchiGame:
    def __init__(self, root):
        """
        Inicjalizujemy grę, ustawiamy roota, rozmiar okna, wczytujemy i ustawiamymy tekstury.
        :param root:
        """
        self.postac = None
        self.root = root
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.load_images()
        self.set_textures()
        self.frozen=False
        self.activity_happening=False

    def load_images(self):
        """
        Wczytuje tekstury. Tekstury przechowujemy w zmiennych klasowych np. self.nazwa_image.
        :return:
        """
        self.bg_image = Image.open("textures/background.png").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.zwyczajniak_image = Image.open("textures/pythonZwyczajniak.png").resize((200, 200))
        self.zwyczajniak_photo = ImageTk.PhotoImage(self.zwyczajniak_image)

        self.dzieciak_image = Image.open("textures/pythonDzieciakjpg.png").resize((200, 200))
        self.dzieciak_photo = ImageTk.PhotoImage(self.dzieciak_image)

        self.grubas_image = Image.open("textures/pythonGrubas.png").resize((200, 200))
        self.grubas_photo = ImageTk.PhotoImage(self.grubas_image)

        self.biznesmen_image = Image.open("textures/pythonBiznesmen.png").resize((200, 200))
        self.biznesmen_photo = ImageTk.PhotoImage(self.biznesmen_image)

    def set_textures(self):
        """
        Ustawia teksturę tła i przycisku startu gry. Teksturę postaci ustawiamy w funkcji start_game, po wyborze klasy.
        :return:
        """
        # Background
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Przycisk start
        self.start_button = tk.Button(self.root, text="Nowa gra", bg="purple", fg="white",font=("Arial",20,"bold"), command=self.show_character_selection, borderwidth=0)
        self.start_button.pack(pady=250)

    def show_character_selection(self):
        """
        Metoda wyświetlająca okno z wyborem postaci.
        :return:
        """
        # Usunięcie przycisku startu
        self.root.winfo_children()[1].destroy()

        #Wyświetlenie napisu
        label = tk.Label(self.root, text="Wybierz swoją postać", font=("Arial", 26, "bold"), bg='white')
        label.pack(pady=30) #pack ustawia wsztstko na środku

        # Przyciski wyboru klasy
        btn1 = tk.Button(self.root, text="Zwyczajniak", bg="purple", fg="white",font=("Arial",20,"bold"), command=lambda: self.start_game(characterType.ZWYCZAJNIAK))
        btn2 = tk.Button(self.root, text="Grubas", bg="purple", fg="white",font=("Arial",20,"bold"), command=lambda: self.start_game(characterType.GRUBAS))
        btn3 = tk.Button(self.root, text="Dzieciak", bg="purple", fg="white",font=("Arial",20,"bold"), command=lambda: self.start_game(characterType.DZIECIAK))
        btn4 = tk.Button(self.root, text="Biznesmen", bg="purple", fg="white",font=("Arial",20,"bold"), command=lambda: self.start_game(characterType.BIZNESMEN))
        btn1.pack(pady=25)
        btn2.pack(pady=25)
        btn3.pack(pady=25)
        btn4.pack(pady=25)

    def start_game(self, characterType):
        """
        Metoda, która na podstawie otrzymanego typu, utworzy zwierzaka i wyświetli go na ekranie.
        Wyswietli paski progresu, sklep i aktywności.
        Następnie uruchomi główną pętlę gry.
        :param characterType:
        :return:
        """
        self.clear_frame()
        # -----------------------------------------------------------------------

        # Background
        # Ustawienia głównego kontenera (np. root)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Umieszczenie label jako tło
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # -----------------------------------------------------------------------

        # Wyświetl zwierzaka
        if characterType == characterType.ZWYCZAJNIAK:
            self.postac = t.Tamagotchi(100, 100, characterType.ZWYCZAJNIAK)
            pet_label = tk.Label(self.root, image=self.zwyczajniak_photo)
            pet_label.pack(pady=25)
        if characterType == characterType.DZIECIAK:
            self.postac = t.Tamagotchi(100, 100, characterType.DZIECIAK, mnoznikNudy=5)
            pet_label = tk.Label(self.root, image=self.dzieciak_photo)
            pet_label.pack(pady=25)
        if characterType == characterType.GRUBAS:
            self.postac = t.Tamagotchi(150, 100, characterType.GRUBAS, mnoznikGlodu=5)
            pet_label = tk.Label(self.root, image=self.grubas_photo)
            pet_label.pack(pady=25)
        if characterType == characterType.BIZNESMEN:
            self.postac = t.Tamagotchi(100, 100, characterType.BIZNESMEN, mnoznikMonet=5)
            pet_label = tk.Label(self.root, image=self.biznesmen_photo)
            pet_label.pack(pady=25)

        # -----------------------------------------------------------------------

        # Styl dla napisow
        style = ttk.Style()
        style.configure("FioletBial.TLabel",
                        background="#800080",  # fioletowe tło
                        foreground="white",  # białe napisy
                        font=("Arial", 16, "bold"))

        # -----------------------------------------------------------------------
        # Display
        stats_frame = tk.Frame(root)
        stats_frame.pack(pady=5)

        # -----------------------------------------------------------------------

        # Food Display
        food_frame = tk.Frame(stats_frame)
        food_frame.pack(side=tk.LEFT,padx=10)

        # Text
        food_text = ttk.Label(food_frame, text="Najedzenie:", style="FioletBial.TLabel")
        food_text.pack(pady=5)

        # Progress Bar
        self.food_progress_bar = ttk.Progressbar(food_frame, length=200, mode="determinate")  # pasek
        self.food_progress_bar.pack(pady=5)
        self.food_progress_bar['value'] = self.postac.najedzenie

        # Numeric display
        self.food_numeric = ttk.Label(food_frame, text=f"{self.postac.najedzenie} / {self.postac.maxNajedzenie}", style="FioletBial.TLabel")  # numerycznie
        self.food_numeric.pack(pady=5)

        # -----------------------------------------------------------------------

        # Boredom Display
        boredom_frame = tk.Frame(stats_frame)
        boredom_frame.pack(side=tk.LEFT,padx=10)

        # Text
        boredom_text = ttk.Label(boredom_frame, text="Nuda:", style="FioletBial.TLabel")  # napis
        boredom_text.pack(pady=5)

        # Boredom Bar
        self.boredom_progress_bar = ttk.Progressbar(boredom_frame, length=200, mode="determinate")  # pasek
        self.boredom_progress_bar.pack(pady=5)
        self.boredom_progress_bar['value'] = self.postac.nuda

        # Numeric display
        self.boredom_numeric = ttk.Label(boredom_frame, text=f"{self.postac.nuda} / {self.postac.maxNuda}", style="FioletBial.TLabel")  # numerycznie
        self.boredom_numeric.pack(pady=5)

        #-----------------------------------------------------------------------

        # Money Display
        self.label_monety = ttk.Label(root, text="Monety:" + str(self.postac.monety), style="FioletBial.TLabel")
        self.label_monety.pack(pady=10)

        # -----------------------------------------------------------------------

        #Shop
        shop_frame = tk.Frame(root)
        shop_frame.pack(pady=5)

        #Text
        tk.Label(shop_frame, text="Sklep:", font=("Arial", 26)).pack()

        # Woda
        woda = tk.Button(shop_frame, text="Woda +20 -0g",
                         command=lambda: self.feed("woda"))
        woda.pack(side=tk.LEFT)

        # Chlep
        chlep = tk.Button(shop_frame, text="Chlep +40 -10g",
                          command=lambda: self.feed("chlep",))
        chlep.pack(side=tk.LEFT)

        # Ryba
        ryba = tk.Button(shop_frame, text="Ryba +60 -20g +5pkt",
                         command=lambda: self.feed("ryba"))
        ryba.pack(side=tk.LEFT)

        # Mystery treat
        mysteryTreat = tk.Button(shop_frame, text="Mystery treat -50g",
                                 command=lambda: self.feed("mystery treat"))
        mysteryTreat.pack(side=tk.LEFT)

        #-----------------------------------------------------------------------

        # Activities
        activities_frame = tk.Frame(root)
        activities_frame.pack(pady=5)

        tk.Label(activities_frame, text="Zabawa:", font=("Arial", 26)).pack()
        # Woda
        woda = tk.Button(activities_frame, text="Spacer -10nudy 10s",
                         command=lambda: self.play("spacer"))
        woda.pack(side=tk.LEFT)

        # Chlep
        chlep = tk.Button(activities_frame, text="Zbieranie kasztanów -20nudy 20s",
                          command=lambda: self.play("kasztany"))
        chlep.pack(side=tk.LEFT)

        # Ryba
        ryba = tk.Button(activities_frame, text="Jazda konno -40nudy 40s",
                         command=lambda: self.play("konie"))
        ryba.pack(side=tk.LEFT)

        self.buttons = [woda, chlep, ryba]

        #-----------------------------------------------------------------------

        #Time and points
        time_and_points_frame = tk.Frame(root)
        time_and_points_frame.pack()

        self.seconds = 0
        self.minutes = 0
        self.points = 0

        self.time_label = (tk.Label(time_and_points_frame, text=f"Time: {self.minutes} min : {self.seconds % 60} s"))
        self.time_label.pack(side=tk.LEFT)

        self.points_label = (tk.Label(time_and_points_frame, text=f"current Points: {self.postac.punkty} points"))
        self.points_label.pack(side=tk.LEFT)


        #Główna pętla gry
        self.game_loop()

    def game_loop(self):
        """
        Uruchamia wszystie funkcje odpowiedziane za aktualizowanie jedzenia, poziomu nudy, czasu, sprawdzania przegranej, monet.
        :return:
        """
        self.updateFood()
        self.updateBoredom()
        self.updateMonety()
        self.lose_conditions()
        self.updateTimeAndPoints()

    def updateTimeAndPoints(self):
        """
        Aktualizuje czas i punkty co 1 sekundę.
        :return:
        """
        if not self.frozen:
            self.seconds = self.seconds + 1
            self.postac.punkty += 1
            if self.seconds % 60 == 0:
                self.minutes = self.minutes + 1 * self.postac.mnoznikMonet
                self.seconds = 0

            self.time_label.configure(text=f"Time: {self.minutes} min : {self.seconds%60} s")
            self.points_label.configure(text=f"current Points: {self.postac.punkty} points")

            # Random events
            if self.seconds == 20 or self.seconds == 40 or self.seconds == 59:
                if random.random() < 0.7:
                    self.frozen = True
                    self.random_event()
        root.after(1000, self.updateTimeAndPoints)

    def updateFood(self):
        """
        Aktualizuje jedzenie.
        :return:
        """
        if not self.frozen:
            self.postac.najedzenie = self.postac.najedzenie - 1 * self.postac.mnoznikGlodu
            self.food_progress_bar['value'] = self.postac.najedzenie
            self.food_numeric.configure(text=f"{self.postac.najedzenie} / {self.postac.maxNajedzenie}")
            if self.postac.najedzenie > self.postac.maxNajedzenie or self.postac.najedzenie < 0:
                self.postac.CzyZginalZGlodu = True
        self.root.after(3000, self.updateFood)

    def updateBoredom(self):
        """
        Aktualizuje poziom nudy.
        :return:
        """
        if not self.frozen:
            self.postac.nuda = self.postac.nuda + 1 * self.postac.mnoznikNudy
            self.boredom_progress_bar['value'] = self.postac.nuda
            self.boredom_numeric.configure(text=f"{self.postac.nuda} / {self.postac.maxNuda}")
            if self.postac.nuda > self.postac.maxNuda or self.postac.nuda < 0:
                self.postac.CzyZginalZNudy = True
        self.root.after(3000, self.updateBoredom)

    def updateMonety(self):
        """
        Aktualizuje monety.
        :return:
        """
        if not self.frozen:
            self.postac.monety = self.postac.monety + 1* self.postac.mnoznikMonet
            self.label_monety.configure(text="Monety:" + str(self.postac.monety))
            if self.postac.monety <0:
                self.postac.CzyZginalOdBankructwa = True
        root.after(6000, self.updateMonety)

    def feed(self,food_type):
        """
            Na podstawie wciśniętego przyciusku karmimy zwierzaka odpowiednim jedzeniem.

            zwierzak musi miec zroznicowana diete, wiec po pierwszym posileniu zapoznawczym
            nie mozna mu dac do jedzenia tego co jadl w poprzednim posilku i dwa posilki temu
            (np: przy zjedzeniu: woda, woda, chlep nie mozna mu dac znow ani wody ani chlepka bo jedzenie jest za malo zroznicowane
            trzeba dac mu albo rybe albo mystery treat, wtedy:
            woda, woda, chlep, ryba mozna znow dac albo wode albo mystery treat
            """

        if food_type == "woda":
            if len(self.postac.zjedzonePokarmy) >= 2:
                if self.postac.zjedzonePokarmy[-1] != "woda" and self.postac.zjedzonePokarmy[-2] != "woda":
                    self.postac.najedzenie += 20
                    self.postac.zjedzonePokarmy.append("woda")
                    print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
                else:
                    print(
                        f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{self.postac.zjedzonePokarmy[-2]}, {self.postac.zjedzonePokarmy[-1]}")
            else:
                self.postac.najedzenie += 20
                self.postac.zjedzonePokarmy.append("woda")
                print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
        elif food_type == "chlep":
            if self.postac.monety >= 10:
                if len(self.postac.zjedzonePokarmy) >= 2:
                    if self.postac.zjedzonePokarmy[-1] != "chlep" and self.postac.zjedzonePokarmy[-2] != "chlep":
                        self.postac.monety -= 10
                        self.postac.najedzenie += 40
                        self.postac.zjedzonePokarmy.append("chlep")
                        print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
                    else:
                        print(
                            f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{self.postac.zjedzonePokarmy[-2]}, {self.postac.zjedzonePokarmy[-1]}")
                else:
                    self.postac.monety -= 10
                    self.postac.najedzenie += 40
                    self.postac.zjedzonePokarmy.append("chlep")
                    print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
        elif food_type == "ryba":
            if self.postac.monety >= 20:
                if len(self.postac.zjedzonePokarmy) >= 2:
                    if self.postac.zjedzonePokarmy[-1] != "ryba" and self.postac.zjedzonePokarmy[-2] != "ryba":
                        self.postac.monety -= 20
                        self.postac.najedzenie += 60
                        self.postac.punkty += 5
                        self.postac.zjedzonePokarmy.append("ryba")
                        print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
                    else:
                        print(
                            f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{self.postac.zjedzonePokarmy[-2]}, {self.postac.zjedzonePokarmy[-1]}")
                else:
                    self.postac.monety -= 20
                    self.postac.najedzenie += 60
                    self.postac.punkty += 5
                    self.postac.zjedzonePokarmy.append("ryba")
                    print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
        else:
            if self.postac.monety >= 50:
                if len(self.postac.zjedzonePokarmy) >= 2:
                    if self.postac.zjedzonePokarmy[-1] != "mystery treat" and self.postac.zjedzonePokarmy[-2] != "mystery treat":
                        self.postac.monety -= 50
                        self.postac.zjedzonePokarmy.append("mystery treat")
                        print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
                        self.random_event()
                    else:
                        print(
                            f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{self.postac.zjedzonePokarmy[-2]}, {self.postac.zjedzonePokarmy[-1]}")
                else:
                    self.postac.monety -= 50
                    self.postac.zjedzonePokarmy.append("mystery treat")
                    print(f"zwierzak zjadl: {self.postac.zjedzonePokarmy[-1]}")
                    self.random_event()

        if not self.frozen:
            self.postac.najedzenie = self.postac.najedzenie - 1
            self.food_progress_bar['value'] = self.postac.najedzenie
            self.food_numeric.configure(text=f"{self.postac.najedzenie} / {self.postac.maxNajedzenie}")

        self.label_monety.config(text=f"Monety: {self.postac.monety}")

    def play(self,activityType):
        """
        Na podstawie naciśniętego przycisku rozpoczynamy zabawę na odgórnie określony czas.
        W trakcie zabawy nie można rozpocząć innej zabawy.
        :param activityType:
        :return:
        """
        if self.activity_happening:
            return  # ignorowanie nacisniecia

        if activityType == "spacer":
            duration = 10000
            self.postac.nuda -= 10
        if activityType == "kasztany":
            duration = 20000
            self.postac.nuda -= 20
        if activityType == "konie":
            duration = 40000
            self.postac.nuda -= 40

        if not self.frozen:
            self.postac.nuda = self.postac.nuda + 1
            self.boredom_progress_bar['value'] = self.postac.nuda
            self.boredom_numeric.configure(text=f"{self.postac.nuda} / {self.postac.maxNuda}")

        for button in self.buttons:  # wyszarzenie przyciskow
            button.configure(state=tk.DISABLED)

        self.activity_happening = True

        def end_activity():
            for button in self.buttons:
                button.configure(state=tk.NORMAL)
            self.activity_happening = False

        root.after(duration, end_activity)

    def random_event(self):
        """
        Jeśli na zegarze jest 20, 40 albo 49 sekund, istnieje 70% szans,że wydarzy się losowy event. Może być pozytywny jak i negatywny.
        :return:
        """
        r = random.random()
        # ------------- random eventy pozytywne --------------
        if r < 0.4:
            ran = random.random()
            if ran <= 0.5:
                message = messagebox.showinfo('Random Event Pozytywny', 'Znalezienie 10 monet :3')
                self.postac.monety += 10
            elif 0.5 < ran <= 0.75:
                message = messagebox.showinfo('Random Event Pozytywny',
                                              'Złamanie lapy zwierzaka \n(nuda + 20), ale chociaz 20 monet odszkodowania :/')
                self.postac.monety += 20
                self.postac.nuda += 20
            elif 0.75 < ran <= 0.90:
                ran2 = random.random()
                if ran2 <= 0.5:
                    message = messagebox.showinfo('Random Event Pozytywny',
                                                  'Znalezienie Grzybkow Halucynkow, \nokazalo sie ze zwierzak jest na nie uczulony, \ninstant smierc :|')
                else:
                    message = messagebox.showinfo('Random Event Pozytywny',
                                                  'Znalezienie Grzybkow Halucynkow, zwierzak swietnie sie bawil z grzybkami, \nchce wiecej i staje sie uzalezniony, \njednak nie ma swojego dilera wiec szybko wraca do normy, \nnuda - 75% obecnego poziomu zabawy')
                    self.postac.nuda -= self.postac.nuda * 0.75
            else:
                message = messagebox.showinfo('Random Event Pozytywny',
                                              'Zwierzak otrzymuje spadek od babci z Ameryki, \n+ 250 monet :D')
                self.postac.monety += 250
        # --------------------- random eventy negatywne ---------------------
        elif 0.4 <= r < 0.8:
            ran = random.random()
            if ran <= 0.5:
                message = messagebox.showwarning('Random Event Negatywny',
                                                 'Otwarte zlamanie nogi i prywatna wizyta u lekarza, \nnuda + 25, \nmonety - 10, \n(jesli zwierze jest grubasem, instant smierc, i tak predzej umrze niz wyleczy ta lape wiec po co przedluzac jego cierpienie :) )')
                if self.postac.rodzajPostaci == characterType.GRUBAS:
                    self.postac.CzyZginalOdEventu = True
                self.postac.monety -= 10
                self.postac.nuda += 25
            elif 0.5 < ran <= 0.75:
                ran2 = random.random()
                if ran2 <= 0.5:
                    message = messagebox.showwarning('Random Event Negatywny',
                                                     'Przejscie na czerwonym swietle, \nna szczescie nie bylo policji, \n\nale byl samochod,\ninstant smierc\nbylo uwazac na swiatlach')
                    self.postac.CzyZginalOdEventu = True
                else:
                    message = messagebox.showwarning('Random Event Negatywny',
                                                     'Przejscie na czerwonym swietle, \ntym razem trafila sie policja, bo oni zawsze sa tam gdzie ich nie potrzeba :/\nale zawsze mogl byc zamiast nich samochod\nmandat -20 moent')
                    self.postac.monety -= 20
            elif 0.75 < ran <= 0.90:
                ran2 = random.random()
                if ran2 <= 0.5:
                    message = messagebox.showwarning('Random Event Negatywny',
                                                     'Zwierzak wypil kociolek Panoramixa,\nprzydaloby sie skontrolowac jego znajomych, ale teraz to juz nei bedzie potrzebne\ninstant smierc')
                    self.postac.CzyZginalOdEventu = True
                else:
                    message = messagebox.showwarning('Random Event Negatywny',
                                                     'Zwierzak wypil kociolek Panoramixa,\nprzydaloby sie skontrolowac jego znajomych, moze sie jeszcze przydac, \nteraz zwierzak ma zatrucie pokamowe i trzeba dac taksowkarzowi na pranie tapicerki :|\njedzenie zwierzaka to 10% calkowitej wartosci\n-30 monet')
                    self.postac.najedzenie = self.postac.maxNajedzenie * 0.1
                    self.postac.monety -= 30
            else:
                message = messagebox.showwarning('Random Event Negatywny',
                                                 'Dowod zwierzaka stracil waznosc a mial zaciagnieta pozyczke na 200 moent,\nbank dba o swoje interesy i chce natychmiastowego zwrotu pozyczki\n -200 monet')
                self.postac.monety -= 200
        # --------------------- apokalipsy ------------------------
        else:
            def apokalipsaZombie():
                ran2 = random.random()
                if ran2 <= 0.5:
                    message = messagebox.showerror('Random Event Apokalipsy',
                                                   'Nastapila Apokalipsa Zombie\nzwierzak wykazal sie wytrzymaloscia i anielska cierpliwoscia w szczegolnosci do Eugenea i pomogl im dostac sie Waszyngtonu\nzwierzak dostaje 100 moent za chronienie \'najmadrzejszego\' czlonka ekipy\nwszystko wraca do normy')
                    self.postac.monety += 100
                else:
                    message = messagebox.showerror('Random Event Apokalipsy',
                                                   'Nastapila Apokalipsa Zombie\nzwierzak sie staral ale i tak zombie Grzesio staral sie bardziej\n zwierzak zostal zjedzony w bardzo brutalny sposob\n instant smierc')
                    self.postac.CzyZginalOdEventu = True

            ran = random.random()
            if ran <= 0.4:
                apokalipsaZombie()
            elif 0.4 < ran <= 0.6:
                ran2 = random.random()
                if ran2 <= 0.5:
                    apokalipsaZombie()
                else:
                    message = messagebox.showerror('Random Event Atomowka',
                                                   'Izrael wystrzelil nie ta bombe ktora chcial a nie oszukujmy sie\npo wybuchu bomby atomowej jaka oni dysponuja to zostaje nam tylko owinac sie w przescieradlo i czolgac sie w strone cmentarza\nnikt nie przezyl, a skoro nikt to zwierzak tym bardziej,\ninstant smierc')
                    self.postac.CzyZginalOdEventu = True
            else:
                ran2 = random.random()
                if ran2 <= 0.5:
                    message = messagebox.showerror('Random Event Sauron i Armia',
                                                   'Sauron zaatakowal,\nwklad zwierzaka w kampanie majaca na celu zniszczenie pierscienia okazal sie nieoceniony\n(przeniosl go we wlasnym brzuchu po zjedzeniu go :| )\nw podziece elfy wyplacaja mu 100 monet (sknery)')
                    self.postac.monety += 100
                else:
                    message = messagebox.showerror('Random Event Sauron i Armia',
                                                   'Sauron zaatakowal,\nwklad zwierzaka w kampanie majaca na celu zniszczenie pierscienia okazal sie nie istniec\nna samym poczatku marszu rozdeptal go randomowy ork\ninstant smierc')
                    self.postac.CzyZginalOdEventu = True

        self.frozen = False

    # Check for Lose
    def lose_conditions(self):
        """
        Metoda sprawdzająca czy stworek powinien nie żyć.
        :return:
        """
        if not self.frozen:
            if self.postac.CzyZginalZGlodu:
                self.frozen = True
                if self.postac.maxWynikSesja < self.postac.punkty:
                    self.postac.zapisMaxWynikSesja()
                messagebox.showinfo('You Lost!',
                                    f'You are definitely dead :[ (fullness or emptiness)\nYour score is: {self.postac.punkty}\nlast best score: {self.postac.maxWynikSesja}')

                sys.exit()
            elif self.postac.CzyZginalOdEventu:
                self.frozen = True
                if self.postac.maxWynikSesja < self.postac.punkty:
                    self.postac.zapisMaxWynikSesja()
                messagebox.showinfo('You Lost!',
                                    f'You are definitely dead :[ (event)\nYour score is: {self.postac.punkty}\nlast best score: {self.postac.maxWynikSesja}')
                sys.exit()
            elif self.postac.CzyZginalOdBankructwa:
                self.frozen = True
                if self.postac.maxWynikSesja < self.postac.punkty:
                    self.postac.zapisMaxWynikSesja()
                messagebox.showinfo('You Lost!',
                                    f'You are definitely dead :[ (bankruptcy)\nYour score is: {self.postac.punkty}\nlast best score: {self.postac.maxWynikSesja}')
                sys.exit()
            elif self.postac.CzyZginalZNudy:
                self.frozen = True
                if self.postac.maxWynikSesja < self.postac.punkty:
                    self.postac.zapisMaxWynikSesja()
                messagebox.showinfo('You Lost!',
                                    f'You are definitely dead :[ (boredom or heart attack)\nYour score is: {self.postac.punkty}\nlast best score: {self.postac.maxWynikSesja}')
                sys.exit()
        root.after(1000, self.lose_conditions)

    def clear_frame(self):
        """
        Metoda czyszcząca okno.
        :return:
        """
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagotchiGame(root)
    root.mainloop()