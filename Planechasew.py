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
    print("psycho is " + str(psycho))
    while(True):
        if "PSYCHO" in str(planes[roll][0]):
            if not psycho[0]:
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

#roll function rolls a six sided die and echos the result
#to the result label
def roll(planes, used, psycho, name, desc, chaos, result):
    roll = random.randint(1, 6)
    if(not psycho[0]):
        if(roll is 1):
            result.configure(text="CHAOS")
        elif(roll is 6):
            result.configure(text="PLANECHASE")
            play(planes, used, psycho, name, desc, chaos)
        else:
           result.configure(text="BLANK")
    else:
        if(roll is 1 or roll is 2):
            result.configure(text="CHAOS")
        elif(roll is 6 or roll is 5):
            result.configure(text="PLANECHASE")
            play(planes, used, psycho, name, desc, chaos)
        else:
           result.configure(text="BLANK")

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
    psycho[0]=True

#MAIN#
#declare variables
planes = []
used = []
here=[]
psycho = [] #must be a list to make it mutable (access using psycho[0])
psycho.append(False)

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
name = tkinter.Label(window, text = "click roll to begin", fg="black",font=("Calibri", 20), wraplength = 300)
desc = tkinter.Label(window, text = "", fg="blue",font=("Calibri", 18), wraplength = 600)
chaos = tkinter.Label(window, text = "", fg="red",font=("Calibri", 18), wraplength = 600)
option = tkinter.Button(window, text="GO PSYCHO", fg="red", bg="black", font=("Calibri", 16), command= lambda: goPsycho(psycho))
planardie = tkinter.Button(window, text="Roll", fg="blue",font=("Calibri", 16), command= lambda: roll(planes, used, psycho, name, desc, chaos, result))
go = tkinter.Button(window, text="Planechase", fg="blue",font=("Calibri", 16), command= lambda: play(planes, used, psycho, name, desc, chaos))
planardie.grid(row = 2, column = 2)
result = tkinter.Label(window, text="")

#images
mtg = tkinter.PhotoImage(file="magic.gif")
displayedmtg = mtg.subsample(4,4)
magic = tkinter.Label(image = displayedmtg)

#pack the pieces out
name.pack()
desc.pack()
chaos.pack()
magic.pack()
go.pack(side="right")
planardie.pack(side = "bottom", fill="x")
result.pack(side="bottom")
option.pack(side="left")

#launch
window.mainloop()

