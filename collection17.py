


pizzas_nom = ("4 fromages", "Calzone", "Hawai")
pizzas_prix = (10.5, 11, 8)

noms_et_prix = list(zip(pizzas_nom, pizzas_prix))

for (nom, prix) in noms_et_prix:
    print(f"{nom} - {prix}€")
    
unzipped = list(zip(*noms_et_prix))
pn, pp = list(zip(*noms_et_prix))