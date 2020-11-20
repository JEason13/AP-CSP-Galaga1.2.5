#main.py

import numpy 
import os 
import random 
import time 
from termcolor import colored
from colorama import Fore, Back, Style

string = "Welcome To Galaga!"
def writeText(string):
    for char in string:
        word = print(colored(char, "yellow"))
        word.replace("\n", "") 
        print(Fore.YELLOW + Back.BLACK)
        time.sleep(0.75)

writeText(string)