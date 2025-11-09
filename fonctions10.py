# PYTHON FONCTIONS : NOTIONS AVANCEES
#
# NOMBRE VARIABLE DE PARAMETRE
#

"""

def a(age, taille, numero_telephone):
    print("toto", age, taille, numero_telephone)
    
a(22, 1.85, "0665779090")

"""

def somme(titre, **nombres):
    print("TITRE:", titre)
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("Somme des notes :", maths=15, geo=11, anglais=18))