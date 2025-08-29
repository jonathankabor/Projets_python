import random

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique ? (entre {nb_min} et {nb_max})")
        try:        
            nombre_int = int(nombre_str)
        except:
            print("ERREUR, Vous devez renseigner un nombre. Réessayez")
        # Pour gérer l'intervalle entre ne nb_min et le nb_max il faut rajouter une condition else
        # Sinon il sera facile de sortir de l'intervalle
        # il est important de déclarer à nouveau que nombre_int = 0 à la fin de la condition pour le
        # forcer à ne pas sortir de la fonction et de reboucler pour demander à nouveau le nombre magique
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez")
                nombre_int = 0            
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4


# Boucle while
"""
# faiblesse de la boucle while dans les cas d'erreur le nombre de vies ne diminue pas
nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies >  0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -=1
    else:
        print("Le nombre magique est plus grand")
        vies -=1

if vies == 0:
    print(f"Vous avez perdu ! Le nompbre magique était: {NOMBRE_MAGIQUE}")"""
    

# boucle for
# il faut rajouté un boolean ici dans la condition ou on gagne pour éviter d'afficher
# malgré la victoire vous avez perdu, le nombre magique était

gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")

#if vies == 0:
if not gagne:
    print(f"Vous avez perdu ! Le nompbre magique était: {NOMBRE_MAGIQUE}")