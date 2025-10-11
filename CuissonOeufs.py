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

while True:
    if choix == '1':
        cuisson1 = "3"
        print(f"Vous avez choisit une cuisson de {cuisson1} minutes pour vos Oeufs à la coque")
        break
    elif choix == '2':
        cuisson2 = "6"
        print(f"Vous avez choisit une cuisson de {cuisson2} minutes pour vos Oeufs mollets")
        break
    elif choix == '9':
        cuisson3 = "540"
        print(f"Vous avez choisit une cuisson de {cuisson3} minutes pour vos Oeufs durs")
        break
    else:
        print("Choix invalide veuillez rentrer '1', '2' ou '3' .")