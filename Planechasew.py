import random
import colorama
import os
from colorama import Fore, Back, Style
import tkinter
colorama.init()
window = tkinter.Tk()
window.title("Planechase")
window.geometry("300x300")
window.wm_iconbitmap('mtg.ico')
#Custom planechase game!
#Programming: Jonny Castle and Ian Stout
#Plane concepts and program design: Jonny Castle, Ian Stout and Bryan Steele

#FUNCTIONS#

#print all function (not really used, maybe remove) 
def print_all(list):
    for i in range(len(list)):
        for k in range(len(list[i])):
            print(list[i][k])

#print one plane
def print_one(plane):
    for i in range(len(plane)):
        if (i==0):
            print(Fore.BLACK + Back.WHITE + plane[i] + Style.RESET_ALL)
        if (i==1):
            print(Fore.BLUE + Back.WHITE + plane[i] + Style.RESET_ALL)
        if (i==2):
            print(Fore.RED + Back.WHITE + plane[i] + Style.RESET_ALL)      

#function to play a plane
def play(planes, used, bool):
    if not planes: #if there are no planes
        print(Style.BRIGHT + Fore.RED + Back.WHITE + "YOU HAVE BEEN PLAYING FAR TOO LONG" + Style.RESET_ALL)
        return
    roll = random.randint(0, len(planes)-1)
    while(planes[roll][0].find("PSYCHO")==0 and bool==False):
        roll = random.randint(0, len(planes)-1)
        continue
    print_one(planes[roll])
    used.append(planes[roll])
    here=planes[roll]
    planes.remove(planes[roll])
    return here

#MAIN FUNCTION#
def main():
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

    #game loop
    while(True):
        
        if(psycho):
            print(Fore.RED + Style.BRIGHT)
            option = input("What do? (r to option, p, planechase, q to quit) ")
            print(Style.RESET_ALL)
        else:
            option = input("What do? (r to option, p, planechase, q to quit) ")
            
        if(option == 'r'):  #TODO accept "enter"
            roll = random.randint(1,6)
            if (psycho):
                if(roll==1 or roll==2):
                    os.system('cls')
                    print(Style.BRIGHT + Fore.RED + Back.GREEN + "\nCHAOS\n" + Style.RESET_ALL)
                    print_one(here)
                elif(roll==3 or roll==4):
                    os.system('cls')
                    print(Fore.CYAN + Back.RED + "\nBLANK\n" + Style.RESET_ALL)
                    print_one(here)
                elif(roll==5 or roll==6):
                    os.system('cls')
                    print(Fore.WHITE + Back.BLUE + "\nPLANECHASE\n" + Style.RESET_ALL)
                    here=play(planes, used, psycho)
                    
            if(not psycho):
                if(roll==1):
                    os.system('cls')
                    print(Style.BRIGHT + Fore.RED + Back.GREEN + "\nCHAOS\n" + Style.RESET_ALL)
                    print_one(here)
                elif(roll==2 or roll==3 or roll==4 or roll==5):
                    os.system('cls')
                    print(Fore.CYAN + Back.RED + "\nBLANK\n" + Style.RESET_ALL)
                    print_one(here)
                elif(roll==6):
                    os.system('cls')
                    print(Fore.WHITE + Back.BLUE + "\nPLANECHASE\n" + Style.RESET_ALL)
                    here=play(planes, used, psycho)
                    
            continue
        if(option == 'p'):
            os.system('cls')
            here=play(planes, used, psycho)
            continue
        if(option == 'q'):
            break
        if(option == 'psycho'):
            psycho = True
            print (Fore.RED + Style.BRIGHT + 'PSYCHO MODE' + Style.RESET_ALL)

    #salutations    
    print("thanks for playing")
    return
main()


