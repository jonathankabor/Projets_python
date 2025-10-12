


"""
- Oeufs à la coque : 3 minutes
- Oeufs mollets : 6 minutes
- Oeufs durs : 9 minutes

import time
time.sleep(1)
print(".", end="", flush=True)

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

print(f"{min:02d}")
    
"""
import time
import winsound

print("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
choix = input("Votre choix : ")

duree = 0
if choix == "1":
    duree = 12
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
