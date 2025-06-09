def updateFood(root,postac,food_progress_bar,food_numeric):
    postac.najedzenie = postac.najedzenie - 1
    food_progress_bar['value'] = postac.najedzenie
    food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")
    root.after(3000, lambda: updateFood(root,postac,food_progress_bar,food_numeric))    #lambda bo updateFood potrzebuje root a nie jest w mainGameLoop

def refreshFood(postac,food_progress_bar,food_numeric):
    food_progress_bar['value'] = postac.najedzenie
    food_numeric.configure(text=f"{postac.najedzenie} / {postac.maxNajedzenie}")

def feed(foodType,postac,food_progress_bar,food_numeric,label_monety):
    #todo max 2 razy ten sam pokarm pod rzad
    if foodType == "woda":
        postac.najedzenie += 20
    if foodType == "chlep":
        if postac.monety >= 10:
            postac.monety -= 10
            postac.najedzenie += 40
    if foodType == "ryba":
        if postac.monety >= 20:
            postac.monety -= 20
            postac.najedzenie += 60
            postac.punkty += 5
    if foodType == "mystery treat":  # todo
        if postac.monety >= 50:
            postac.monety -= 50
            pass

    refreshFood(postac,food_progress_bar,food_numeric)

    label_monety.config(text=f"Monety: {postac.monety}")
    label_monety.grid(row=3, column=0,columnspan=2)