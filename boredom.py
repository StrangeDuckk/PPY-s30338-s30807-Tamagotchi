import mainGameLoop
import tkinter as tk
def updateBoredom(root,postac,boredom_progress_bar,boredom_numeric):
    if not mainGameLoop.frozen:
        postac.nuda = postac.nuda + 1
        boredom_progress_bar['value'] = postac.nuda
        boredom_numeric.configure(text=f"{postac.nuda} / {postac.maxNuda}")
    root.after(3000, lambda: updateBoredom(root,postac,boredom_progress_bar,boredom_numeric))

def refreshBoredom(postac,boredom_progress_bar,boredom_numeric):
    boredom_progress_bar['value'] = postac.nuda
    boredom_numeric.configure(text=f"{postac.nuda} / {postac.maxNuda}")

def play(activityType,postac,boredom_progress_bar,boredom_numeric,buttons,root):
    if mainGameLoop.activity_happening:
        return  #ignorowanie nacisniecia

    if activityType == "spacer":
        duration = 10000
        postac.nuda -= 10
    if activityType == "kasztany":
        duration = 20000
        postac.nuda -= 20
    if activityType == "konie":
        duration = 40000
        postac.nuda -= 40

    refreshBoredom(postac,boredom_progress_bar,boredom_numeric)

    for button in buttons:  #wyszarzenie przyciskow
        button.configure(state=tk.DISABLED)

    mainGameLoop.activity_happening = True

    def end_activity():
        for button in buttons:
            button.configure(state=tk.NORMAL)
        mainGameLoop.activity_happening = False

    root.after(duration,end_activity)
