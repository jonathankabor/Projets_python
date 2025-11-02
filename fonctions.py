# Les fonctions

""" 
nom = "Jo le Magicien"
print("Je m'appelle " + nom) # concaténé la chaine # <-- 1 seul paramètre
print()
print("Je m'appelle", nom, "J'ai", 22, "ans") # <-- 2 paramètres

input("Votre nom :") # <-- Retourne une valeur (La fonction input bloque le programme tant qu'on a pas donné 
# une réponse)
print("Votre nom est:", nom)

nom1 = input("Nom de la personne 1: ")
age1 = input("Age de la personne 1: ")
print("La personne 1 est", nom1, "son age est", age1, "ans")
print("le nom comporte", len(nom1), "lettres")

nom2 = input("Nom de la personne 2: ")
age2 = input("Age de la personne 2: ")
print("La personne 1 est", nom2, "son age est", age2, "ans")
print("le nom comporte", len(nom2), "lettres")

"""

"""
# définition de la fonction
def afficher_infos_personne_toto_20():
    print("La personne est toto, son age est 20 ans")
    print("Le nom comporte 4 caractères")
    
def afficher_infos_personne_titi_25():
    print("La personne est titi, son age est 30 ans")
    print("Le nom comporte 4 caractères")

print("Début du programme")

afficher_infos_personne_toto_20()
afficher_infos_personne_titi_25()

print("Fin du programme")

"""
# Les paramètres d'une fonction