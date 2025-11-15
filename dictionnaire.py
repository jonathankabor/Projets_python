

personne = {'nom': 'Mélanie', "age": 25, 'taille': 1.60}
# print(personne)
# print(personne['nom'])
# print(personne['age'])


personne['nom'] = "Claire"

personne['poste'] = "Développeur"

achat = ("Chocolat", "beurre", "fromage")
personne['achats'] = achat
print(personne)

for i in personne:
    print(f"clef: {i} - valeur: {personne[i]}")