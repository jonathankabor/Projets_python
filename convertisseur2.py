def conversion():

    # 1. Demander à l'utilisateur le sens de la conversion
        while True:
            choix = input("Souhaitez-vous convertir de 'pouces vers cm' (entrez '1') ou de 'cm vers pouces' (entrez '2') ? ")
            if choix == '1':
                unite1 = "pouces"
                unite2 = "cm"
                taux = 2.54
                break
            elif choix == '2':
                unite1 = "cm"
                unite2 = "pouces"
                taux = 0.394
                break
            else:
                print("Choix invalide. Veuillez entrer '1' ou '2'.")

        print(f"\nVous avez choisi de convertir de {unite1} vers {unite2}.")

    # 2. Boucle pour convertir au moins 4 valeurs
        for i in range(1, 5): # Boucle pour 4 essais
            while True:
                try:
                    valeur = float(input(f"Conversion {i} : Entrez la valeur en {unite1} à convertir : "))
                    valeur_convertie = valeur * taux
                    print(f"La valeur convertie est : {valeur_convertie:.2f} {unite2}")
                    break
                except ValueError:
                    print("Valeur invalide. Veuillez entrer un nombre.")

    # 3. Proposer de quitter ou de recommencer
        while True:
            retenter = input("\nConversion terminée. Voulez-vous recommencer avec un nouveau type de conversion ? (oui/non) ")
            if retenter.lower() == 'non':
                print("Fin du programme. À bientôt !")
                return False # Sortie du programme
            elif retenter.lower() == 'oui':
                print("\n")
                break # Revenir au début de la grande boucle
        conversion()

# Exécuter le programme
conversion()