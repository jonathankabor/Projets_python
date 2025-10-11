import time
import beepy


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




def cuisson_oeufs_decompte():
    # Démarrer un compte à rebours pour la cuisson des oeufs et afficher le temps restant toutes les 10 secondes
    # Convertir la durée en seconde
    secondes1 = 3
    secondes2 = 6 
    secondes3 = 9
    # Définir l'intervalle d'affichage   
    #intervalle_affichage = 10 
    if secondes1:  
        print(f"La Cuisson des oeufs a durée {secondes1} minutes...")
    elif secondes2:
        print(f"La Cuisson des oeufs a durée {secondes2} minutes...")
    else:
        print(f"La Cuisson des oeufs a durée {secondes3} minutes...")
        
    #temps_restant1 = secondes1
    #temps_restant2 = secondes2
    #temps_restant3 = secondes3
    
choix = input("Quel est votre choix ? :")
    
    #Boucle compte à rebours
while True:
    if choix == '1':
        for i in range(180):
            time.sleep(1)
            print(".", end="", flush=True)
            if (i+1 ) % 10 == 0:
                calcul = 180 - (i + 1 )
                min = calcul // 60
                sec = calcul - min * 60
                print(f"\nLe Temps restant est de : {min:02d}:{sec:02d}", end="", flush=True)
        break
                    
    elif choix == '2':
        for i in range(360):
            time.sleep(1)
            print(".", end="", flush=True)
            if (i+1 ) % 10 == 0:
                calcul = 360 - (i + 1 )
                min = calcul // 60
                sec = calcul - min * 60
                print(f"\nLe Temps restant est de : {min:02d}:{sec:02d}", end="", flush=True)
        break
                    
    elif choix == '3':
        for i in range(540):
            time.sleep(1)
            print(".", end="", flush=True)
            if (i+1 ) % 10 == 0:
                calcul = 360 - (i + 1 )
                min = calcul // 60
                sec = calcul - min * 60
                print(f"\nLe Temps restant est de : {min:02d}:{sec:02d}", end="", flush=True)
        break
    else:
        choix = input("Choix invalide. Veuillez entrer 1, 2 ou 3 : ")           
       
beepy.beep(sound="ping")    
print("\n C'est prêt ! Vos oeufs sont cuits. Bon appétit")

  
cuisson_oeufs_decompte()

        
