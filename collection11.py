# LES COLLECTIONS : LISTES / TUPLES
# Les compréhensions de listes


#          0        1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

"""

longeur_noms = []
for nom in noms:
    longeur_noms.append(len())
    
"""

# longeur_noms = [len(nom) for nom in noms if len(nom) < 10]
# noms_avec_e = [nom for nom in noms if "e" in nom]

# longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]

a = [i for i in range(10) if (i//2)*2 == i] # pair
# a = [i for i in range(10) if (i//2)*2 != i] impair
b = [(i, True if (i//2)*2 == i else False) for i in range(10)]

print(b)