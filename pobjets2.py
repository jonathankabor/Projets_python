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
#  [Personne "Jean"]    [Personne "Paul"]

# ----- DEFINITION -----
# nom : str
# age : int
# 1 - Si age == 0
#  =>Bonjour, je m'appelle Toto
#  =>On affiche pas mineur
#  => Demander le nom à l'utilisateur
#  => DemanderNom(...) -> input("") -> nom

class Personne:
    def __init__(self, nom: str, age: int): 
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)   
        
    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        if self.age == 0:
            print("Bonjour, je m'appelle " + self.nom)
        else:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
        
#   def AutreFonction(self):
#       print("Nom: " + self.nom)
#   EstMajeur -> True / False

    def EstMajeur(self):
        return self.age >= 18  



# ----- UTILISATION -----
personne1 = Personne("Jean", 30)  # Je cree une personne
personne2 = Personne("Paul", 15)  # Je cree une personne
personne3 = Personne()

# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter() # méthode d'instance
personne3.SePresenter()

# print("estMajeur2 : ", personne2.EstMajeur())

# personne1.AutreFonction()

# personne.AutreFonction()  # méthode de classe




