import random
import time
import os

points = 0
nombre_de_chiffres_a_memoriser = 4

def effacer_ecran():
# Fonction pour effacer l'écran de la console (compatible Windows/Linux/MacOS)
    os.system('cls' 
        if os.name == 'nt' 
        else 'clear')


def jeu_de_memoire():

    
    print("Bienvenue dans le Jeu de Mémoire de Chiffres!")
    print("Préparez-vous à mémoriser une séquence de chiffres.\n")

while True:
    effacer_ecran() # Efface l'écran avant chaque nouvelle séquence

    print(f"--- Niveau {points +1} ---")
    print(f"Vous devez mémoriser {nombre_de_chiffres_a_memoriser} chiffres.")
    time.sleep(1) # Petite pause avant d'afficher les chiffres

# 1. Générer les chiffres aléatoires
    chiffres_a_memoriser = [str(random.randint(0, 9)) 
for i in range(nombre_de_chiffres_a_memoriser)]
    sequence_chiffres = "".join(chiffres_a_memoriser)

# 2. Afficher pour la mémorisation (3 secondes)
    print("\nMEMORISEZ CECI MAINTENANT:")
    print("***************************")
    print(f"{sequence_chiffres}")
    print("***************************")

# Le cœur de la mémorisation
    time.sleep(3)

# 3. Effacer et demander la réponse
    effacer_ecran()
    print("TEMPS ÉCOULÉ!")
    print("---------------------------------")

# Le `strip()` est pour retirer les espaces accidentels.
# Le `try-except` permet de gérer si l'utilisateur n'entre rien ou autre chose.
    reponse_utilisateur = input(f"Veuillez entrer la séquence de {nombre_de_chiffres_a_memoriser} chiffres que vous avez vue : ").strip()

# 4. Vérifier la réponse
    if reponse_utilisateur == sequence_chiffres:
        points += 1
        nombre_de_chiffres_a_memoriser += 1 # Incrémentation pour le prochain niveau
        print("\nFÉLICITATIONS! Réponse correcte. 🎉")
        print(f"Score actuel : {points} point(s).")
        print("Passons au niveau suivant avec un chiffre supplémentaire.")
        input("Appuyez sur ENTRÉE pour continuer...") # Attendre l'utilisateur
    else:
        print("\nDOMMAGE! Réponse incorrecte. 😢")
        print(f"La séquence correcte était : {sequence_chiffres}")
        print(f"Votre réponse était : {reponse_utilisateur}")
        print(f"Votre score final est de {points} point(s).")
        break # Arrête la boucle et le programme





    
    