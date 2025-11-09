# PYTHON FONCTIONS : NOTIONS AVANCEES
#
# DIFFERENCE ENTRE BREAK ET RETURN
# BREAK PEUT SUTILISER PARTOUT DANS LES BOUCLES ET DANS LE PROGRAMME
# RETURN LUI IL EST SPECIFIQUE AUX FONCTIONS

def a():
    print("Début de la fonction")
    for i in range(0, 100):
        if i > 20:
            break
        print(i)
    print("Fin de la fonction")
        
a()