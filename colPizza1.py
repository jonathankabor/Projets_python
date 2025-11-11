# collection pizza
# afficher les pizza par ligne
# "AUCUNE PIZZA"

# --------------- LISTE DES PIZZAS (4) -----------------------

def afficher_pizza(collection):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return
        
    print(f"---- LISTE DES PIZZAS ({(nb_pizzas)})----")
    for i in collection:
        print(i)
    print()
    print("Première pizza: " + collection[0])
    print("Dernière pizza: " + collection[-1])
        
            
    
pizzas = ("4 fromages", "végétarienne", "hawai", "calzone")
vide = ()
afficher_pizza(vide)
