# Cuisson des oeufs, correction
DUREE_PROGRESSION = 10

import time
import winsound

# titre : "Oeufs ç la coque"
# durée : 3*60

cHOIX_CUISSON = (
   ("Oeufs à la coque", 3*60), 
   ("Oeufs mollets", 6*60),
   ("Oeufs durs", 9*60)    
)

print("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")

while True:
    choix = input("Votre choix : ")
    if choix =='1' or choix =='2' or choix =='3':
            break
    print("ERREUR: Vous devez choisir 1, 2 ou 3\n")
    
duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60
    
while duree > 0:
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
        duree -=1
        if duree <= 0:
            break
        
        
    if duree <= 0:
            break

    min = duree//60 # division entière (pas de virgules)
    sec = duree-min*60
    print()
    print(f"Temps restant : {min:02d}:{sec:02d}", end="", flush=True)

print()   
print("cuisson terminée")
frequency = 2500
duration = 1000

winsound.Beep(frequency, duration)
