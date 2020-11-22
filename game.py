#game.py
import os
from colorama import Fore, Back, Style
from termcolor import colored, cprint
import time

enemy_ship = colored("O", 'red', attrs=['reverse', 'blink', 'bold'])
player_ship = colored( "∆", 'cyan', attrs=['reverse', 'blink', 'bold'])
#player_ship_shielded_full = "((∆))"
#player_ship_shielded_half = "(∆)"
bullet = colored( ".", 'green', attrs=['bold'])

def game():
    name = input("ENTER YOUR NAME:\t")

    user_score = 0

    game_map = [ [0, 0, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],   
    [ 0, 0, 0, 0, 0, 0, 0, 0 ] ]  

    player_ship_pos = game_map[7][3] = player_ship
    enemy_ship_pos0 = game_map[0][1] = enemy_ship
    enemy_ship_pos1 = game_map[0][3] = enemy_ship
    enemy_ship_pos2 = game_map[0][5] = enemy_ship
    
    bullet_pos = game_map[6][3] = bullet



    for i in range(len(game_map)) :  
        for j in range(len(game_map[i])) :  
            print(Fore.BLACK, Back.BLACK, game_map[i][j], end=" ") 
        print()  

    print(Fore.GREEN, Back.BLACK, "Welcome to galaga! Use Y/N to shoot and WASD to move when prompted!")
    shoot_yn = input("SHOOT? (Y/N):\t")
    if(shoot_yn == 'n' or shoot_yn == 'N'):
        pass
    elif(shoot_yn == 'y' or shoot_yn == 'Y'):
        game_map[6][3] = 0
        bullet_pos = game_map[5][3] = bullet
        time.sleep(0.2)
        bullet_pos = game_map[4][3] = bullet
        time.sleep(0.2)
        bullet_pos = game_map[3][3] = bullet
        time.sleep(0.2)        
        bullet_pos = game_map[2][3] = bullet
        time.sleep(0.2)        
        bullet_pos = game_map[1][3] = bullet
        time.sleep(0.2)        
        bullet_pos = game_map[0][3] = bullet
        if(bullet_pos == game_map[0][3]):
            print(Fore.GREEN, Back.BLACK, "Yay! You scored a point! Good job!")
            user_score = user_score + 1
            lb_file = 'leaderboard.txt'
            lb_data =("\t"+name+": "+ str(user_score)+"\n")
            lb = open(lb_file, 'a')
            lb.write(lb_data)
            lb.close


    dir_input = input("MOVE (WASD):\t")
    if(dir_input == 'a' or dir_input == 'A'):
        os.system('clear')
        game_map[7][3] = 0
        player_ship_pos = game_map[7][2] = player_ship
        for i in range(len(game_map)) :  
            for j in range(len(game_map[i])) :  
                print(Fore.BLACK, Back.BLACK, game_map[i][j], end=" ") 
            print()
        print(Fore.GREEN, Back.BLACK, "Good job! now you know how to play!")
        shoot_yn = input("SHOOT? (Y/N):\t")
        if(shoot_yn == 'n' or shoot_yn == 'N'):
            pass
        elif(shoot_yn == 'y' or shoot_yn == 'Y'):
            pass
  

    elif(dir_input == 'd' or dir_input == 'D'):
        os.system('clear')
        game_map[7][3] = 0
        player_ship_pos = game_map[7][4] = player_ship
        for i in range(len(game_map)) :  
            for j in range(len(game_map[i])) :  
                print(Fore.BLACK, Back.BLACK, game_map[i][j], end=" ") 
            print()  
        print(Fore.GREEN, Back.BLACK, "Good job! now you know how to play!")
        shoot_yn = input("SHOOT? (Y/N):\t")
        if(shoot_yn == 'n' or shoot_yn == 'N'):
            pass
        elif(shoot_yn == 'y' or shoot_yn == 'Y'):
            pass

    elif(dir_input == 'w' or dir_input == 'W'):
        os.system('clear')
        game_map[7][3] = 0
        player_ship_pos = game_map[6][3] = player_ship
        for i in range(len(game_map)) :  
            for j in range(len(game_map[i])) :  
                print(Fore.BLACK, Back.BLACK, game_map[i][j], end=" ") 
            print()  
        print(Fore.GREEN, Back.BLACK, "Good job! now you know how to play!")
        shoot_yn = input("SHOOT? (Y/N):\t")
        if(shoot_yn == 'n' or shoot_yn == 'N'):
            pass
        elif(shoot_yn == 'y' or shoot_yn == 'Y'):
            pass

    elif(dir_input == 's' or dir_input == 'S'):
        os.system('clear')
        game_map[7][3] = 0
        player_ship_pos = game_map[7][3] = player_ship
        print(Fore.GREEN, Back.BLACK, "You can not move here!")
        shoot_yn = input("SHOOT? (Y/N):\t")
        if(shoot_yn == 'n' or shoot_yn == 'N'):
            pass
        elif(shoot_yn == 'y' or shoot_yn == 'Y'):
            pass



