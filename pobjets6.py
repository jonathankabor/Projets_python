# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nombre_de_personnes = 3

# noms = []

liste_personnes = []

for i in range(nombre_de_personnes):
    nom = input("nom de la personne 1 : " + str(i+1) + " : ")
    liste_personnes.append(Personne(nom))


# noms.append(input("nom de la personne 2 : "))
# noms.append(input("nom de la personne 3 : "))

# l = []

# for nom in noms:
#    l.append(Personne(nom))

for personne in liste_personnes:
    personne.SePresenter()