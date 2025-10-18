# Cuisson des oeufs, correction
DUREE_PROGRESSION = 10

import time
import winsound

# titre : "Oeufs ç la coque"
# durée : 3*60

CHOIX_CUISSON = (
   ("Oeufs à la coque", 3*60), 
   ("Oeufs mollets", 6*60),
   ("Oeufs durs", 9*60),
   ("Steak à point", 4*60 + 30)    
)

def temps_sec_en_str(t):
    min = t//60 # division entière (pas de virgules)
    sec = t-min*60
    min_unit = "minutes"
    sec_unit = "secondes"
    if min == 1:
        min_unit = "minute"
    if sec == 1:
        sec_unit = "seconde"
    r = ""
    if min > 0:
        r += f"{min} {min_unit}" 
    if sec > 0:
        if len(r) > 0:
            r += " "
        r += f" {sec} {sec_unit}"
    return r

print("Choix de la cuisson")
index_choix = 1
for choix_cuisson in CHOIX_CUISSON:
   print(f"{index_choix} - {choix_cuisson[0]} : {temps_sec_en_str(choix_cuisson)}") 



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
