import random
import colorama
import os
from colorama import Fore, Back, Style
import textwrap
colorama.init()

#Custom planechase game!


#FUNCTIONS (main at the end)

#print all function
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
            print (Fore.BLUE + Back.WHITE + plane[i] + Style.RESET_ALL)
        if (i==2):
            print(Fore.RED + Back.WHITE + plane[i] + Style.RESET_ALL)
        

#function to play a plane
def play(planes, used):
    if not planes: #if there are no planes
        print(Style.BRIGHT + Fore.RED + Back.WHITE + "YOU HAVE BEEN PLAYING FAR TOO LONG" + Style.RESET_ALL)
        return
    x = random.randint(0, len(planes)-1)
    print_one(planes[x])
    used.append(planes[x])
    here=planes[x]
    planes.remove(planes[x])
    return here
    
#test function plays a single plane and displays the differences
def test(planes, used):
    #shows the whole deck    
    print("the plane deck\n")
    print_all(planes)

    #plays one plane
    print("play a random plane\n")
    play(planes, used)

    #the shows again
    print("the plane deck after play\n")
    print_all(planes)

#MAIN FUNCTION, where the magic happens
def main():
    file = open('planes.txt', 'r')

    data = file.readlines()

    planes = []
    used = []

    for line in data:
        words = line.split("`")
        planes.append(words)

    here=[]
    
    
    while(True):
        roll = input("What do? (r to roll, p, planechase, q to quit) ")
        if(roll == 'r'):  #TODO accept "enter"
            x = random.randint(1,6)
            print(x)
            if(x==1):
                os.system('cls')
                print(Style.BRIGHT + Fore.RED + Back.GREEN + "\nCHAOS\n" + Style.RESET_ALL)
                print_one(here)
            elif(x==2 or x==3 or x==4 or x==5):
                os.system('cls')
                print(Fore.CYAN + Back.RED + "\nBLANK\n" + Style.RESET_ALL)
                print_one(here)
            elif(x==6):
                os.system('cls')
                print(Fore.WHITE + Back.BLUE + "\nPLANECHASE\n" + Style.RESET_ALL)
                here=play(planes, used)
            continue
        if(roll == 'p'):
            os.system('cls')
            here=play(planes, used)
            continue
        if(roll == 'q'):
            break
        
    print("thanks for playing")
    return
                
    

main()
