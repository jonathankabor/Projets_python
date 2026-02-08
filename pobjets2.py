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
    def __init__(self, nom): 
        self.nom = nom   # crée une variable d'instance : nom
        print("Constructeur personne " + nom)   
        
    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)
        
#   def AutreFonction(self):
#       print("Nom: " + self.nom)



# ----- UTILISATION -----
personne1 = Personne("Jean")  # Je cree une personne
personne2 = Personne("Paul")  # Je cree une personne

# Personne.SePresenter(personne1)
personne1.SePresenter()
# personne1.AutreFonction()
personne2.SePresenter() # méthode d'instance

# personne.AutreFonction()  # méthode de classe



