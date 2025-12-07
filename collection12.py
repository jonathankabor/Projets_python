# LES COLLECTIONS : LISTES / TUPLES
# Any et All 
# Any : Quelconque / n'importe quel
# All : Tous

#          0        1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

"""

#a = [True, False, False, True]
#a = [False, False, False, False]
a = [True, True, True, True]


print(any(a))
print(all(a))

"""

"""
found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break
    
if found:
    print("Trouvé")
else:
    print("Non trouvé")

"""
        
nom_avec_un_z_existe = all([True if "z" in nom.lower() else False for nom in noms])
if nom_avec_un_z_existe:
    print("Trouvé")
else:
    print("Non trouvé")