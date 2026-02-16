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
    def __init__(self, nom: str = "", age: int = 0): 
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)   
        
    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"
            
        print(info_personne)
            
        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
        
#   def AutreFonction(self):
#       print("Nom: " + self.nom)
#   EstMajeur -> True / False

    def EstMajeur(self):
        return self.age >= 18  
    
    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")



# ----- UTILISATION -----
# personne1 = Personne("Jean", 30)  # Je cree une personne
# personne2 = Personne("Paul", 15)  # Je cree une personne


liste_personnes = [Personne("Jean", 30), Personne("Paul", 15), Personne()]
# liste_personnes[1].SePresenter()
print("Affichage liste 1")
for personne in liste_personnes:
    personne.SePresenter()

# personne3 = Personne()
personne4 = Personne(age=20)
liste_personnes.append(personne4)

print("Affichage liste 2")
for personne in liste_personnes:
    personne.SePresenter()
    
# Personne.SePresenter(personne1)
# personne1.SePresenter()
# personne2.SePresenter() # méthode d'instance
# personne3.SePresenter()
# personne4.SePresenter()

# print("estMajeur2 : ", personne2.EstMajeur())

# personne1.AutreFonction()

# personne.AutreFonction()  # méthode de classe




