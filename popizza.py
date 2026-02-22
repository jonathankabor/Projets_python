# Nom, prix, ingrédients, végétarienne


class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
        
    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix} €  " + veg_str)
#       print(self.ingredients)
        print(", ".join(self.ingredients))
        print()
        
        
        
# pizza1 = Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"))
# pizza1.Afficher()

# ingredients = ("brie", "emmental", "compté", "parmesan")
# print(", ".join(ingredients))

pizzas = (
    Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Hawai", 9.5, ("tomate", "ananas", "oignons")),
    Pizza("4 saisons", 11, ("oeuf", "emmental", "tomate", "jambon")),
    Pizza("Végétarienne", 7.8, ("champignons", "tomate", "oignons", "poivrons"), True)      
)      

for i in pizzas:
    i.Afficher()