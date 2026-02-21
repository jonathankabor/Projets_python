# Nom, prix, ingrédients, végétarienne


class Pizza:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        
    def Afficher(self):
        print(f"PIZZA {self.nom} : {self.prix} €  ")
        print(self.ingredients)
        print(", ".join(self.ingredients))
        
        
        
pizza1 = Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"))
pizza1.Afficher()

# ingredients = ("brie", "emmental", "compté", "parmesan")
# print(", ".join(ingredients))

        