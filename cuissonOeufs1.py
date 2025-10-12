


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

print("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
choix = input("Votre choix : ")

duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60
    
while True:
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
    print("")

    duree = 100
    min = duree//60 # division entière (pas de virgules)
    sec = duree-min*60