# programation Python

def demander_nom():
    reponse_nom = ""
    while  not reponse_nom =="Jonathan":
        reponse_nom = input ("Quel est ton nom ? ") # une variable avec un chaine de caractère
    
    return reponse_nom
    
    
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est ton age ? ")
        try:
            age_int = int(age_str) 
        except:    
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
            
    return age_int
        
def afficher_informations_personne(nom, age, taille=0):
    print()
    print("je m'appelle " + nom + ", j'ai " + str(age) + " ans")
    #print(f"je m'appelle {nom}, j'ai {age} ans")
    print("Cette année j'aurai " + str(age + 1) + " ans")
    #print("Cette année j'aurai %s ans" % (age + 1))
    #print("je m'appelle %s, j'ai %s ans" % (nom, age))
    print("Votre taille : " + str(taille) + " m")
   
    
    # == egal
    # < inférieur
    # <= inférieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean)
    # if else condition
    # elif contraction de else et if
    
    # age == 17 ans -> Vous êtes presque majeur
    # age == 18 ans -> Tout juste majeur : Félicitation
    # age > 60 : Vous êtes sénior
    # age < 10 : Vous êtes enfant
    # Adolescent si age >= 12 et age < 18
    # Bebe si age == 1 ou age == 2
    # age >= 12 and age < 18
    
    
    if age == 17:
        print("Vous êtes presque majeur") 
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")   
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")


# afficher la taille
#taille = 1.85 #float
#print(type(taille))
# if not taille ==0:
#    print("Votre taille : " + str(taille) + " M")
       

# nom = "Jo le Magicien"
# age = 37
# str -> int

# while (age n'est pas correct)

#afficher la suite

# demander le nom
#nom1 = demander_nom()
#nom2 = demander_nom()

# demander l'age
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

#print("Fin de la boucle")
#else:

#Afficher les résultats
#afficher_informations_personne(nom1, age1)
#afficher_informations_personne(nom2, age2)

    
# print(type(nom))
# print(type(age))
# 1.5 -> float
# vrai ou faux boolean (true/false)
# str(30) -> "30"


# int -> str


# print("et je suis l'homme le plus fort du monde")
# print("Merci, passez une bonne journée")

# boucle while : "tant que"...




#n = 0 # cree la variable
#print(n)
#n=10  # reaffecte la variable
#print(n)
#n=n+1 # incremente
#print(n)

#print("Debut de la boucle")
#while n < 10:
#    print("valeur de n: " + str(n))
#    n = n + 1
#print("Fin de la boucle")


#mot_de_passe = ""

#while not mot_de_passe == "TOTO":
    
#    mot_de_passe = input ("Quel est le mot de passe ? ")

#print ("Mot de passe correct, vous avez accès au compte")

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" +  str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom, age,1.85)
    
    
print("""
Vous
    mettez
        ce que vous voulez, life is good                
""")
print("Jojo", 37, "ans",  "taille:", 1.85)