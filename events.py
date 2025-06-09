import tkinter as tk
from tkinter import messagebox
import mainGameLoop

def random_event(root):
    message = messagebox.showinfo('Random Event', 'Random Event has occurred. You are probably dead :3')
    mainGameLoop.frozen = False