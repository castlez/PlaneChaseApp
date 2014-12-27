import random
import colorama
import os
from colorama import Fore, Back, Style
import tkinter

#Custom planechase game!
#Programming: Jonny Castle and Ian Stout
#Plane concepts and program design: Jonny Castle, Ian Stout and Bryan Steele

#FUNCTIONS$
def play():
    plane.configure(text = "clicked me!")

#MAIN#
colorama.init()
window = tkinter.Tk()
window.title("Planechase")
window.geometry("900x600")
#window.wm_iconbitmap(r'C:\Users\Jonny\Documents\Programs\Planechase_gen\PlaneChaseApp\mtg.ico')<----issues
roller = tkinter.Button(window, text="Roll", command = play)
plane = tkinter.Label(window, text = "click roll to begin")
plane.pack()
roller.pack()




