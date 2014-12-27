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
def display(plane, name, desc, chaos):
    name.configure(text = plane[0])
    desc.configure(text = plane[1])
    try:
       chaos.configure(text = plane[2])
    except IndexError:
        chaos.configure(text = "")
        
#play function, takes the planes list, the used list
#and the boolean psycho as args and plays a single plane
def play(planes, used, psycho, name, desc, chaos):
    if(len(planes) is 0):
        name.configure(text = "There are no more planes")
        desc.configure(text = "")
        chaos.configure(text = "")
        return
    
    roll = random.randint(0, len(planes)-1)
    
    while(not planes[roll][0] is not "PSYCHO" and psycho == False):
        print("skipped a psycho")
        roll = random.randint(0, len(planes)-1)
        continue
    
    display(planes[roll], name, desc, chaos)
    used.append(planes[roll])
    planes.remove(planes[roll])

#MAIN#
#declare variables
planes = []
used = []
here=[]
psycho = []

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
window.geometry("600x400")
#window.wm_iconbitmap(r'C:\Users\Jonny\Documents\Programs\Planechase_gen\PlaneChaseApp\mtg.ico')<----issues
name = tkinter.Label(window, text = "click roll to begin", fg="black", wraplength = 300)
desc = tkinter.Label(window, text = "", fg="blue", wraplength = 300)
chaos = tkinter.Label(window, text = "", fg="red", wraplength = 300)
roller = tkinter.Button(window, text="Roll", fg="blue", command= lambda: play(planes, used, psycho, name, desc, chaos))
roller.grid(row = 2, column = 2)
name.pack()
desc.pack()
chaos.pack()
roller.pack(side = "bottom")

window.mainloop()

