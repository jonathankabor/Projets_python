import time

"""
   Votre programme proposera 3 options :
   1) Oeufs à la coque : 3 minutes
   2) Oeufs mollets : 6 minutes
   3) oeufs durs : 9 minutes 
    
"""
print("***********************")
print("Choisissez votre Menu")
print("***********************")
print("1) Oeufs à la coque : 3 minutes")
print("2) Oeufs mollets : 6 minutes")
print("3) Oeufs durs : 9 minutes")


choix = input("Quel est votre choix ? :")

def cuisson_oeufs_decompte():
    cui1 = "3 minutes"
    cui2 = "6 minutes"
    cui3 = "9 minutes"
    # Démarrer un compte à rebours pour la cuisson des oeufs et afficher le temps restant toutes les 10 secondes
    # Convertir la durée en seconde
    duree_secondes1 = 3 * 60
    duree_secondes2 = 6 * 60 
    duree_secondes3 = 9 * 60
    # Définir l'intervalle d'affichage   
    intervalle_affichage = 10 
    if duree_secondes1:  
        print(f"Cuisson de oeufs lancée pour {duree_secondes1} secondes...")
    elif duree_secondes2:
        print(f"Cuisson de oeufs lancée pour {duree_secondes2} secondes...")
    else:
        print(f"Cuisson de oeufs lancée pour {duree_secondes3} secondes...")
        
    temps_restant = duree_secondes1
    temps_restant = duree_secondes2
    temps_restant = duree_secondes3
    
    
    
    #Boucle compte à rebours
    while True:
        if (temps_restant % intervalle_affichage == 0) or (temps_restant == duree_secondes1):
            minutes = temps_restant // 60
            secondes = temps_restant % 60
            print(f"Le Temps restant est de {cui1}: ")
            temps_restant -=1
            if temps_restant > 0:
                for secondes in range(1, duree_secondes1):
                    time.sleep(1)
                    print(".", end="", flush=True)
            break
        elif (temps_restant % intervalle_affichage == 0) or (temps_restant == duree_secondes2):
            minutes = temps_restant // 60
            secondes = temps_restant % 60
            print(f"Le Temps restant est de {cui2}: ")
            temps_restant -=1
            if temps_restant > 0:
                for i in range(5):
                    time.sleep(1)
                    print(".", end="", flush=True)
            break
        elif (temps_restant % intervalle_affichage == 0) or (temps_restant == duree_secondes3):
            minutes = temps_restant // 60
            secondes = temps_restant % 60
            print(f"Le Temps restant est de {cui3}: ")
            temps_restant -=1
            if temps_restant > 0:
                for i in range(5):
                    time.sleep(1)
                    print(".", end="", flush=True)
            
       
        
    print("\n C'est prêt ! Vos oeufs sont cuits. Bon appétit")
    
while True:
    if choix == '1':
        cuisson1 = "3"
        print(f"Vous avez choisit une cuisson de {cuisson1} minutes pour vos Oeufs à la coque")
        break       
    elif choix == '2':
        cuisson2 = "6"
        print(f"Vous avez choisit une cuisson de {cuisson2} minutes pour vos Oeufs mollets")
        break
    elif choix == '3':
        cuisson3 = "9"
        print(f"Vous avez choisit une cuisson de {cuisson3} minutes pour vos Oeufs durs")
        break
    else:
        print("Choix invalide veuillez rentrer '1', '2' ou '3' .")
        

        
cuisson_oeufs_decompte()

        
