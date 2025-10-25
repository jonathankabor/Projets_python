import random
import time
import os


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
def seq_aleatoire_chiffre():
    a = random.randint(0, 9) 
    b = random.randint(0, 9) 
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    seq = input(f"Retenez la séquence : {a}{b}{c}{d}") 
    seq_str = str(seq)  
    return seq_str  

seq_aleatoire_chiffre()

 