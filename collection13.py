# LES COLLECTIONS : LISTES / TUPLES
# any / isdigit 


#          0        1        2            3         4       5
#noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


def chaine_contient_chiffre(chaine):
    """for c in chaine:
        if c.isdigit():
            return True
    return False"""
    return any([c.isdigit() for c in chaine])


nom = input("Quel est ton nom ? ")
if nom == "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)
    

