


# Conversion de unit1 vers unit2
# return True : l'utilisateur ne veut plus convertir
# la fonction effectuer_conversion : convertit les unités unit1 vers unit2

def effectuer_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter): ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer une valeur numérique \n utiliser le point et non la virgule pour les décimales)")
        return effectuer_conversion(unit1, unit2, facteur)
        
    valeur_convertie = round(valeur_float * 2.54, 2)
    print(f"Résultat de la conversion: {valeur_float} {unit1} = {valeur_convertie} {unit2} ")
    return False

while True:
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers Pouces")
    choix = input("Votre choix (1 ou 2): ")
    if not (choix == "1" or choix == "2"):
        break
    
    print("ERREUR : Vous devez choisir 1 ou 2\n")
    
    
while True:
    if choix == "1":
        if effectuer_conversion("pouces", "cm", 2.54):
            break
        
    if choix == "2":
        if effectuer_conversion("cm", "pouces", 0.394):
            break