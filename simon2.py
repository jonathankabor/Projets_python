"""
- Longueur séquence initiale : 4
- Durée de mémorisation : 3s
- A chaque tour : 1 chiffre
- Un nombre de vies

Facile
    longueur_initiale : 3
    duree_memorisation : 4
    increment_sequence : 1
    nombre_vies : 2

Normal
    longueur_initiale : 4
    duree_memorisation : 3
    increment_sequence : 1
    nombre_vies : 1

Difficile
    longueur_initiale : 5
    duree_memorisation : 2
    increment_sequence : 2
    nombre_vies : 0

"""


import random
import time
import os

NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_initiale": 3,
        "duree_memorisation_sec": 4,
        "increment_sequence": 1,
        "nombre_essais": 2,
    },
    {
        "titre": "Normal",
        "longueur_initiale": 4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais": 1,
    },
    {
        "titre": "Difficile",
        "longueur_initiale": 5,
        "duree_memorisation_sec": 2,
        "increment_sequence": 2,
        "nombre_essais": 0,
    },
)

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

    seq_utilisateur = input("Rentrez la séquence: ")
    if seq_utilisateur == sequence:
        score +=1
    else:
        break

    chiffre = random.randint(0,9)
    sequence += str(chiffre)
    clear_screen()
    
print("Mauvaise réponse")
print(f"La réponse était {sequence}")
print(f"Votre score final est : {score}")
