import random
import time
import os


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
        


# Génération de la séquence initiale
sequence = ""
for i in range(4):
    chiffre = random.randint(0,9)
    sequence += str(chiffre)

clear_screen() 
print("Bienvenue dans le jeu du Simon") 

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    seq_utilisateur : input("Rentrez la séquence: ")
    if seq_utilisateur == sequence:
        score +=1

    chiffre = random.randint(0,9)
    sequence += str(chiffre)
