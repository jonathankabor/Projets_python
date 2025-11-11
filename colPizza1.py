# collection pizza
# afficher les pizza par ligne

# --------------- LISTE DES PIZZAS (4) -----------------------

def afficher_pizza(collection):
    nb_pizzas = len(collection)
    print(f"---- LISTE DES PIZZAS ({(nb_pizzas)})----")
    for i in collection:
        print(i)
        
            
    
pizzas = ("4 fromages", "végétarienne", "hawai", "calzone")
afficher_pizza(pizzas)
