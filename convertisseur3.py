
"""

Collections
- liste de conversions possibles
- pouces --> cm (...)
- cm --> m
- km --> miles
        

"""

# Conversion de unit1 vers unit2
# return True : l'utilisateur ne veut plus convertir
# la fonction demander_et_afficher_conversion : convertit les unités unit1 vers unit2

#unité de départ, unité d'arrivée, facteur de conversion
CONVERSIONS = (
    ("pouces", "cm", 2.54),
    ("m", "cm", 100),
    ("km", "miles", 0.621371),
    
)

def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float, reverse: bool = False):
    if reverse:
        unit1, unit2 = unit2, unit1
        facteur = 1 / facteur
        
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter): ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer une valeur numérique \n utiliser le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(unit1, unit2, facteur)
        
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion: {valeur_float} {unit1} = {valeur_convertie} {unit2} ")
    return False

def demander_valeur_numerique_utilisateur(valeur_min, valeur_max):
    v = input(f"Donnez une valeur entre {valeur_min} et {valeur_max} : ")
    try:
        v_int = int(v)
    except:
        print("ERREUR: Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)
    
    if not valeur_min <= v_int <= valeur_max:
        print(f"ERREUR: Votre valeur doit être entre {valeur_min} et {valeur_max}")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)
    
    return v_int

#while True:
# menu : choix de la conversion
print("Ce programme vous permet d'effectuer des conversions d'unités")
i = 1
for c in CONVERSIONS:
    unit1 = c[0]
    unit2 = c[1]
    print(f"{i} - {unit1} vers {unit2}")
    i+=1
    print(f"{i} - {unit2} vers {unit1}")
    i+=1
    #print("1 - Pouces vers cm")
    #print("2 - cm vers Pouces")
valeur_choix_maximale = i-1
        
choix_int = demander_valeur_numerique_utilisateur(1, valeur_choix_maximale)

    #if 1 <= choix_int <= valeur_choix_maximale:
    #break
    
    #print(f"ERREUR : Vous devez choisir une valeur entre 1 et {valeur_choix_maximale}\n")
    #choix = input(f"Votre choix (entre 1 et {valeur_choix_maximale}): ")

    #try:
        #choix_int = int(choix)
    #except:
        #print("ERREUR: Vous devez entrer une valeur numérique")
        #continue #pour revenir au début du menu


   
    

   
while True:
    # Demander les valeurs à convertir à l'utilisateur
    #if choix == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54, reverse=False if choix == "1" else True):
            break
        
    #if choix == "2":
        #if demander_et_afficher_conversion("pouces", "cm", 2.54, reverse=True):
        #if demander_et_afficher_conversion("cm", "pouces", 0.394):
            #break