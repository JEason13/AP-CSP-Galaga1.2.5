#main.py

import numpy 
import os 
import random 
import time 
from colorama import Fore, Back, Style

from assets import ship_logo
from assets import galaga_logo
from assets import main_menu_text

from game import game

lb = open('leaderboard.txt', 'r')
lb_contents = lb.read()


os.system('clear') #clear the screen
os.system("\x1b[40m") #set background color to black

def splash():
    print(Fore.RED + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.CYAN + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.RED + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.CYAN + galaga_logo)
    time.sleep(1)
    os.system('clear')

    print(Fore.RED + ship_logo)

def how_to_play():
    print(Fore.GREEN + "\n\n\tThis game is a clone of the 1981 game Galaga. \n\tIn this game you will have to pilot a spaceship and attempt to avoid dangers such as enemy alien ships and their gunfire. \n\tUse your gun to shoot the enemy ships and earn points. But be caeful, you only have three lives!\n\n\n\n")

def quit_game():
    print(Fore.GREEN + "\n\n\n\tThanks for playing! See you again soon!\n\n")

def main_menu(): 
    print(Fore.RED + main_menu_text)
    time.sleep(1)
    print(Fore.YELLOW + "\t• START GAME  (1)\n")
    print(Fore.YELLOW + "\t• LEADERBOARD (2)\n")
    print(Fore.YELLOW + "\t• HOW TO PLAY (3)\n")
    print(Fore.YELLOW + "\t• QUIT        (4)\n")
    main_menu_input = str(input("\tENTER THE NUMBER OF YOUR CHOICE:\t"))
    if(main_menu_input == '4'):
        quit_game()
    elif(main_menu_input == '3'):
        how_to_play()
        time.sleep(15)
        os.system('clear')
        main_menu()
    elif(main_menu_input == '2'):
        print(Fore.GREEN + "\n\t" + lb_contents)
        lb.close
        time.sleep(15)
        os.system('clear')
        main_menu()
    elif(main_menu_input == '1'):
        os.system('clear')
        print(Fore.GREEN + "")
        game()
        print(Fore.GREEN + "")



splash()
main_menu()