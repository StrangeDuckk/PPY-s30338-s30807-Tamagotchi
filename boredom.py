def updateBoredom(root,postac,boredom_progress_bar,boredom_numeric):
    postac.nuda = postac.nuda + 1
    boredom_progress_bar['value'] = postac.nuda
    boredom_numeric.configure(text=f"{postac.nuda} / {postac.maxNuda}")
    root.after(3000, lambda: updateBoredom(root,postac,boredom_progress_bar,boredom_numeric))

def refreshBoredom(postac,boredom_progress_bar,boredom_numeric):
    boredom_progress_bar['value'] = postac.nuda
    boredom_numeric.configure(text=f"{postac.nuda} / {postac.maxNuda}")

def play(activityType,postac,boredom_progress_bar,boredom_numeric):
    if activityType == "spacer":
        postac.nuda -= 10
    if activityType == "kasztany":
        postac.nuda -= 20
    if activityType == "konie":
        postac.nuda -= 40

    refreshBoredom(postac,boredom_progress_bar,boredom_numeric)