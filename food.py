import mainGameLoop
from events import random_event

def updateFood(root,postac,food_progress_bar,food_numeric):
    if not mainGameLoop.frozen:
        postac.najedzenie = postac.najedzenie - 1
        food_progress_bar['value'] = postac.najedzenie
        food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")
    root.after(3000, lambda: updateFood(root,postac,food_progress_bar,food_numeric))    #lambda bo updateFood potrzebuje root a nie jest w mainGameLoop

def refreshFood(postac,food_progress_bar,food_numeric):
    food_progress_bar['value'] = postac.najedzenie
    food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")

def feed(foodType,postac,food_progress_bar,food_numeric,label_monety,root):
    #todo max 2 razy ten sam pokarm pod rzad
    if foodType == "woda":
        if len(postac.zjedzonePokarmy)>=2 or not postac.zjedzonePokarmy[::-1] == postac.zjedzonePokarmy[::-2] == "woda":
            postac.najedzenie += 20
            postac.zjedzonePokarmy.append("woda")
    if foodType == "chlep":
        if postac.monety >= 10:
            if len(postac.zjedzonePokarmy)>=2 or not postac.zjedzonePokarmy[::-1] == postac.zjedzonePokarmy[::-2] == "chlep":
                postac.monety -= 10
                postac.najedzenie += 40
                postac.zjedzonePokarmy.append("chlep")
    if foodType == "ryba":
        if postac.monety >= 20:
            if len(postac.zjedzonePokarmy)>=2 or not postac.zjedzonePokarmy[::-1] != postac.zjedzonePokarmy[::-2] == "ryba":
                postac.monety -= 20
                postac.najedzenie += 60
                postac.punkty += 5
                postac.zjedzonePokarmy.append("ryba")
    if foodType == "mystery treat":
        if postac.monety >= 50:
            if len(postac.zjedzonePokarmy)>=2 or not postac.zjedzonePokarmy[::-1] != postac.zjedzonePokarmy[::-2] == "mystery treat":
                postac.monety -= 50
                postac.zjedzonePokarmy.append("mystery treat")
                random_event(root,postac)

    refreshFood(postac,food_progress_bar,food_numeric)

    label_monety.config(text=f"Monety: {postac.monety}")
    label_monety.grid(row=3, column=0,columnspan=2)