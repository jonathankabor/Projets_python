###
# LES PREMIERS PAS EN POO (PROGRAMMATION ORIENTEE OBJET)
###
# - Différence programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entiyé --> class)
#    Données :nom, age
#    Actions : (méthodes)
#       - SePresenter
#       - DemanderNom (input)


def afficher_informations_personne(nom, age):
    print(f"La personne s'appelle {nom}, son age est {age} ans")
    
def demander_nom_personne():
    nom = input("Quel est votre nom ?")
    return nom

nom1 = "Jean"
age1 = 30

nom2 ="Paul"
age2 = 25

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)

nom3 = demander_nom_personne()
age3 = 18
afficher_informations_personne(nom3, age3)

