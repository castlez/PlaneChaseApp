import random
import colorama
import os
from colorama import Fore, Back, Style
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
            print(Fore.BLUE + Back.WHITE + plane[i] + Style.RESET_ALL)
        if (i==2):
            print(Fore.RED + Back.WHITE + plane[i] + Style.RESET_ALL)
        
        

#function to play a plane
def play(planes, used, bool):
    if not planes: #if there are no planes
        print(Style.BRIGHT + Fore.RED + Back.WHITE + "YOU HAVE BEEN PLAYING FAR TOO LONG" + Style.RESET_ALL)
        return
    x = random.randint(0, len(planes)-1)
    while(planes[x][0].find("PSYCHO")==0 and bool==False):
        x = random.randint(0, len(planes)-1)
        continue
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
    
    planardie = False
    while(True):
        if (planardie):
            print(Fore.RED + Style.BRIGHT)
            roll = input("What do? (r to roll, p, planechase, q to quit) ")
            print(Style.RESET_ALL)
            if(roll == 'r'):  #TODO accept "enter"
                x = random.randint(1,6)
                if (not planardie):
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
                        here=play(planes, used, planardie)
                if (planardie):
                    if(x==1 or x==2):
                        os.system('cls')
                        print(Style.BRIGHT + Fore.RED + Back.GREEN + "\nCHAOS\n" + Style.RESET_ALL)
                        print_one(here)
                    elif(x==3 or x==4):
                        os.system('cls')
                        print(Fore.CYAN + Back.RED + "\nBLANK\n" + Style.RESET_ALL)
                        print_one(here)
                    elif(x==5 or x==6):
                        os.system('cls')
                        print(Fore.WHITE + Back.BLUE + "\nPLANECHASE\n" + Style.RESET_ALL)
                        here=play(planes, used, planardie)
                
                continue
        if (not planardie):
            roll = input("What do? (r to roll, p, planechase, q to quit) ")
            if(roll == 'r'):  #TODO accept "enter"
                x = random.randint(1,6)
                print(x)
                if (not planardie):
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
                        here=play(planes, used, psycho)
                if (planardie):
                    if(x==1 or x==2):
                        os.system('cls')
                        print(Style.BRIGHT + Fore.RED + Back.GREEN + "\nCHAOS\n" + Style.RESET_ALL)
                        print_one(here)
                    elif(x==3 or x==4):
                        os.system('cls')
                        print(Fore.CYAN + Back.RED + "\nBLANK\n" + Style.RESET_ALL)
                        print_one(here)
                    elif(x==5 or x==6):
                        os.system('cls')
                        print(Fore.WHITE + Back.BLUE + "\nPLANECHASE\n" + Style.RESET_ALL)
                        here=play(planes, used, psycho)
                
                continue
        if(roll == 'p'):
            os.system('cls')
            here=play(planes, used, planardie)
            continue
        if(roll == 'q'):
            break
        if(roll == 'psycho'):
            planardie = True
            print (Fore.RED + Style.BRIGHT + 'PSYCHO MODE' + Style.RESET_ALL)
        
        
    print("thanks for playing")
    return
                
    

main()
