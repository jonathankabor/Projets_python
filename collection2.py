# LISTES - EXERCICE : DEMANDER NOMS DE PERSONNES


# nom et l'age input

"""
for i in range(3):
    nom = input("Nom de la personne : ")
    print("Le nom est :", nom)
    
"""

# demander des noms de personnes
# boucle infinie, sort quand le nom est vide == "" => break
# seulement à la fin afficher tous les noms

noms = []

nom = input("Nom de la personne : ")

while True:
    nom = input("Nom de la personne : ")
    if nom == "":
        break
    noms.append(nom) # rajouter le nom saisie dans la liste
    
print()
print("Nom des personnes")
noms.sort() # trier les noms par ordre alphabetique A-Z a-z
for nom in noms:
    print("  " + nom)