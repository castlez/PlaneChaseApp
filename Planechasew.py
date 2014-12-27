import random
import colorama
import os
from colorama import Fore, Back, Style
import tkinter

#Custom planechase game!
#Programming: Jonny Castle and Ian Stout
#Plane concepts and program design: Jonny Castle, Ian Stout and Bryan Steele

#FUNCTIONS$

#displays a single plane
def display(here, plane):
    if(plane[0].find("Phenomenon") ==-1):
        here.configure(text = plane[0] + '\n' + plane[1] + '\n' + plane[2])
    else:
        here.configure(text = plane[0] + '\n' + plane[1])

#play function, takes the planes list, the used list
#and the boolean psycho as args and plays a single plane
def play(planes, used, psycho, here):
    roll = random.randint(0, len(planes)-1)
    while(planes[roll][0].find("PSYCHO")==0 and bool==False):
        roll = random.randint(0, len(planes)-1)
        continue
    display(here, planes[roll])
    

#MAIN#
#declare variables
planes = []
used = []
here=[]
psycho = False

#open the planes file
file = open('planes.txt', 'r')
data = file.readlines()

#populate the planes list
for line in data:
    words = line.split("`")
    planes.append(words)

#setup and execute window
colorama.init()
window = tkinter.Tk()
window.title("Planechase")
window.geometry("900x600")
#window.wm_iconbitmap(r'C:\Users\Jonny\Documents\Programs\Planechase_gen\PlaneChaseApp\mtg.ico')<----issues
plane = tkinter.Label(window, text = "click roll to begin", fg="red", wraplength = 700)
roller = tkinter.Button(window, text="Roll", fg="blue", command= lambda: play(planes, used, psycho, plane))
plane.pack()
roller.pack()

window.mainloop()

