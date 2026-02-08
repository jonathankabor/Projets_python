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
class Personne:
    def __init__(self, nom: str, age: int): 
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)   
        
    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
#   def AutreFonction(self):
#       print("Nom: " + self.nom)



# ----- UTILISATION -----
personne1 = Personne("Jean", 30)  # Je cree une personne
personne2 = Personne("Paul", 25)  # Je cree une personne

# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter() # méthode d'instance

# personne1.AutreFonction()

# personne.AutreFonction()  # méthode de classe



