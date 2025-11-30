# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Nombre total de caractères"


#          0        1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# 1 - for / len

"""
for nom in noms:
    s = 0
    s +=len(nom)
print("Nombre total de caractères:", s)
"""
# 2 - completion de liste + sum

"""
longeur_noms = [len(nom) for nom in noms]
print("Nombre total de caractères:", sum(longeur_noms))
"""

# 3 - Join / len

print("Nombre total de caractères:", len("".join(noms)))
