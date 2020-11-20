#main.py

import numpy 
import os 
import random 
import time 
from colorama import Fore, Back, Style
from assets import ship_logo
from assets import galaga_logo

os.system('clear') #clear the screen
os.system("\x1b[40m") #set background color to black

def splash():
    print(Fore.RED + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.BLUE + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.RED + galaga_logo)
    time.sleep(1)
    os.system('clear')
    print(Fore.BLUE + galaga_logo)
    time.sleep(1)
    os.system('clear')

    print(Fore.RED + ship_logo)


splash()