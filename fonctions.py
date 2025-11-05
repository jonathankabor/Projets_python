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

"""
# Les paramètres d'une fonction

def afficher_infos_personne(nom, age):
    print("La personne est", nom + ", son age est", age, "ans")
    print("Le nom comporte", len(nom),  "caractères")
    
print("Début du programme")

afficher_infos_personne("Emilie", "20")

print("Fin du programme")

"""

"""
# Les paramètres optionnels

def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas donné de nom")
    else:
        if age == 0:
            print("La personne est", nom)
        else:
            print("La personne est", nom + ", son age est", age, "ans")
            print("Le nom comporte", len(nom),  "caractères")
        
print("Début du programme")

afficher_infos_personne("Toto", 20)

print("Fin du programme")

"""

"""
# return (pas obligatoire)
# --> sortir de la fonction
# --> renvoyer une valeur (pas obligatoire)

def est_majeur(age):
    if age <= 0:
        return False
    # Vrai ou Faux (True / False)
    # si l'age >= 18 => True sinon False
    if age >= 18:
        return True
    return False

def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas donné de nom")
        return
    if age == 0:
        print("La personne est", nom)
    else:
        print("La personne est", nom + ", son age est", age, "ans")
        print("Le nom comporte", len(nom),  "caractères")
        if est_majeur(age):
            print("il est majeur")
        else:
            print("il est mineur")
        
print("Début du programme")

# afficher_infos_personne("Toto", 20)
age = 0

if age == 0:
    exit(0) # exit pour forcer la sortie
    
print("La personne a", age, "ans")
majeur_ou_non = est_majeur(age)
if majeur_ou_non:
    print("il est majeur")
else:
    print("il est mineur")

print("Fin du programme")

"""

"""
recuperer_et_afficher_infos_personne
    -> recuperer_infos_personne()
    -> afficher_infos_personne(nom, age)

"""
# implémenter recuperer_et_afficher_infos_personne
# parametre : numero_personne
# rien retourner
# input / print

def recuperer_et_afficher_infos_personne(numero_personne):
    nom = input("Nom de la personne " + str(numero_personne) + ": ")
    age = input("Age de la personne " + str(numero_personne) + ": ")
    print("La personne " + str(numero_personne), "est", nom, "son age est", age, "ans")
    print("le nom comporte", len(nom), "caractères")


nb_personnes = 3

for i in range(nb_personnes): # 0 1 2
    recuperer_et_afficher_infos_personne(i+1)
