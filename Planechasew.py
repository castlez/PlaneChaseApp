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

    if (len(planes) == countPsychos(planes)):
        name.configure(text = "only psychos remain")
        desc.configure(text = "")
        chaos.configure(text = "")
        return
    
    roll = random.randint(0, len(planes)-1)
    while(True):
        if "PSYCHO" in planes[roll][0]:
            if not psycho:
                print("skipped a psycho plane")
                roll = random.randint(0, len(planes)-1)
                continue
            else:
                break
        
        else:
            break
    
    display(planes[roll], name, desc, chaos)
    used.append(planes[roll])
    planes.remove(planes[roll])

#counts the number of psycho planes in the deck
#to be compared to the size of the deck to see if
#psycho planes are all that remain
def countPsychos(planes):
    counter = 0
    for i in range(len(planes)):
        if "PSYCHO" in planes[i][0]:
            counter = counter + 1
    return counter
#sets the psycho boolean to true <------doesnt work
def goPsycho(psycho):
    print("going psycho")
    psycho=True
    return psycho

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

#setup window
colorama.init()
#window
window = tkinter.Tk()
window.configure(background="thistle3")
window.title("Planechase")
window.geometry("600x300")
#window.wm_iconbitmap(r'C:\Users\Jonny\Documents\Programs\Planechase_gen\PlaneChaseApp\mtg.ico')<----issues

#widgets
name = tkinter.Label(window, text = "click roll to begin", fg="black", wraplength = 300)
desc = tkinter.Label(window, text = "", fg="blue", wraplength = 300)
chaos = tkinter.Label(window, text = "", fg="red", wraplength = 300)
option = tkinter.Button(window, text="GO PSYCHO", fg="red", bg="black", command= lambda: goPsycho(psycho))
planardie = tkinter.Button(window, text="Planechase", fg="blue", command= lambda: play(planes, used, psycho, name, desc, chaos)) #<--change this to roll instead
planardie.grid(row = 2, column = 2)

#images
mtg = tkinter.PhotoImage(file="magic.gif")
displayedmtg = mtg.subsample(4,4)
magic = tkinter.Label(image = displayedmtg)
#pack the pieces out
name.pack()
desc.pack()
chaos.pack()
magic.pack()
planardie.pack(side = "bottom", fill="x")
option.pack(side="bottom")

#launch
window.mainloop()

