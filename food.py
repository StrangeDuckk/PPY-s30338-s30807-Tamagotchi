import mainGameLoop
from events import random_event

def updateFood(root,postac,food_progress_bar,food_numeric):
    if not mainGameLoop.frozen:
        postac.najedzenie = postac.najedzenie - 1*postac.mnoznikGlodu
        food_progress_bar['value'] = postac.najedzenie/postac.maxNajedzenie*100#todo przypomniec
        food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")
    root.after(3000, lambda: updateFood(root,postac,food_progress_bar,food_numeric))    #lambda bo updateFood potrzebuje root a nie jest w mainGameLoop

def refreshFood(postac,food_progress_bar,food_numeric):
    food_progress_bar['value'] = postac.najedzenie/postac.maxNajedzenie*100
    food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")

def feed(foodType,postac,food_progress_bar,food_numeric,label_monety,root):
    """
    zwierzak musi miec zroznicowana diete, wiec po pierwszym posileniu zapoznawczym
    nie mozna mu dac do jedzenia tego co jadl w poprzednim posilku i dwa posilki temu
    (np: przy zjedzeniu: woda, woda, chlep nie mozna mu dac znow ani wody ani chlepka bo jedzenie jest za malo zroznicowane
    trzeba dac mu albo rybe albo mystery treat, wtedy:
    woda, woda, chlep, ryba mozna znow dac albo wode albo mystery treat
    """

    if foodType == "woda":
        if len(postac.zjedzonePokarmy) >=2:
            if postac.zjedzonePokarmy[-1] != "woda" and postac.zjedzonePokarmy[-2] != "woda":
                postac.najedzenie += 20
                postac.zjedzonePokarmy.append("woda")
                print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
            else:
                print(f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{postac.zjedzonePokarmy[-2]}, {postac.zjedzonePokarmy[-1]}")
        else:
            postac.najedzenie += 20
            postac.zjedzonePokarmy.append("woda")
            print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
    elif foodType == "chlep":
        if postac.monety >=10:
            if len(postac.zjedzonePokarmy) >=2:
                if postac.zjedzonePokarmy[-1] != "chlep" and postac.zjedzonePokarmy[-2] != "chlep":
                    postac.monety -= 10
                    postac.najedzenie += 40
                    postac.zjedzonePokarmy.append("chlep")
                    print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
                else:
                    print(f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{postac.zjedzonePokarmy[-2]}, {postac.zjedzonePokarmy[-1]}")
            else:
                postac.monety -= 10
                postac.najedzenie += 40
                postac.zjedzonePokarmy.append("chlep")
                print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
    elif foodType == "ryba":
        if postac.monety >=20:
            if len(postac.zjedzonePokarmy) >=2:
                if postac.zjedzonePokarmy[-1] != "ryba" and postac.zjedzonePokarmy[-2] != "ryba":
                    postac.monety -= 20
                    postac.najedzenie += 60
                    postac.punkty += 5
                    postac.zjedzonePokarmy.append("ryba")
                    print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
                else:
                    print(f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{postac.zjedzonePokarmy[-2]}, {postac.zjedzonePokarmy[-1]}")
            else:
                postac.monety -= 20
                postac.najedzenie += 60
                postac.punkty += 5
                postac.zjedzonePokarmy.append("ryba")
                print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
    else:
        if postac.monety >= 50:
            if len(postac.zjedzonePokarmy) >=2:
                if postac.zjedzonePokarmy[-1] != "mystery treat" and postac.zjedzonePokarmy[-2] != "mystery treat":
                    postac.monety -= 50
                    postac.zjedzonePokarmy.append("mystery treat")
                    print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
                    random_event(root, postac)
                else:
                    print(f"zwierzak musi jesc bardziej zroznicowanie, sprobuj pokarmow innych niz:\n{postac.zjedzonePokarmy[-2]}, {postac.zjedzonePokarmy[-1]}")
            else:
                postac.monety -= 50
                postac.zjedzonePokarmy.append("mystery treat")
                print(f"zwierzak zjadl: {postac.zjedzonePokarmy[-1]}")
                random_event(root, postac)


    refreshFood(postac,food_progress_bar,food_numeric)

    label_monety.config(text=f"Monety: {postac.monety}")
    label_monety.grid(row=3, column=0,columnspan=2)