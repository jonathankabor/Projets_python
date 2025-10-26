import random
import time
import os


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
        
chiffre = random.randint(0,9)

print("Bienvenue dans le jeu du Simon")

