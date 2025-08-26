"""
    while (age n'est pas correct)
        demande l'age
        
        afficher la suite    
"""


def afficher_informations_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans")
    # print(f"Vous vous appelez {nom}, Vous avez {age} ans")
    # print("Vous vous appelez %s, vous avez %s ans" %(nom, age))
    print("L'an prochain vous aurez " + str(age+1) + " ans")
    # print("L'an prochain vous aurez %s ans" %(age + 1))
    
    # == egal
    # < inférieur
    # <= inférieur ou égale
    # > supérieur
    # >= supérieur ou égale
    # True / False (Boolean)
    #
    
    # age == 17 -> Vous êtes presque majeur
    # age == 18 -> Tout juste majeur : Félicitation
    # elif -> else if
    # age > 60 : Vous êtes sénior
    # age < 10 : Vous êtes enfant
    # adolescent si age >= 12 et age < 18
    # Bebe si age == 1 ou age == 2
    
    
    if age ==1 or age ==2:
        print("Vous êtes un Bébé")
    elif age < 10:
        print("Vous êtes enfant")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")    


# afficher la taille
    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")

def demander_nom():
    reponse_nom =""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ?")
    return reponse_nom


def demander_age(nom_personne): 
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ?") 
        try:
            age_int = int(age_str)
        except ValueError:   
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


   
# Demander le nom
# nom1 = demander_nom()
# nom2 = demander_nom()

# Demander l'âge
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

# Afficher les résultats
#afficher_informations_personne(nom1, age1)
#afficher_informations_personne(nom2, age2)


    
      
#print("Fin de la boucle")
# nom = "Jo le Magicien"
# age = 37


    
    

#else:
      

# print(type(nom))
# print(type(age))

# str(37) -> "37"
# str -> int
# age : "37" / int(age) : 37 / age_prochain : 38 / str(age_prochain) : "38" 


#Boucle while : "tant que" ...add()

# n = 0

# while n < 10:
#    print("Valeur de n: " + str(n))
#    n = n + 1
#    print("Fin de la boucle")


# mot_de_passe = ""
# while not mot_de_passe == "GIGA":
#    mot_de_passe = input("Quel est le mot de passe ? ")
    
#print("Mot de passe correct, vous avez acces au compte")


# la Boucle for
NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
   nom = "personne" + str(i+1)
   age = demander_age(nom)
   afficher_informations_personne(nom, age, 1.85)

print("""
  Test
        affichage
            sur plusieurs ligne    
""")
print("Jo le Magicien", 37, "taille:",1.85 )


