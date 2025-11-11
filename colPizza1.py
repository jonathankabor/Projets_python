# collection pizza
# afficher les pizza par ligne
# "AUCUNE PIZZA"

# --------------- LISTE DES PIZZAS (4) -----------------------



# def tri_personnalise(e):
#    return len(e)

def afficher_pizza(collection, n_premiers_elements=-1):
#    collection.sort(reverse= True, key=tri_personnalise)
    c = collection
    if not n_premiers_elements == -1:
        c = collection[: n_premiers_elements]
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return
        
    print(f"---- LISTE DES PIZZAS ({(nb_pizzas)})----")
    for i in c:
        print(i)
    print()
    print("Première pizza: " + c[0])
    print("Dernière pizza: " + c[-1])
        

def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    # if pizza_existe(p, collection):
    if p.lower() in collection:
        print("ERREUR : Cette pizza existe déjà")
    else:
        collection.append(p)
          

# def pizza_existe(e, collection):
#    for i in collection:
#        if i == e:
#            return True
#    return False

 
pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
#vide = ()
ajouter_pizza_utilisateur(pizzas)
afficher_pizza(pizzas, 3)

# lower() -> minuscules
# upper() -> majuscules
