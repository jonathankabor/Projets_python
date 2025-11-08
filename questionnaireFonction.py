"""
LES FONCTIONS : PROJET QUESTIONNAIRE
Question : Quelle est la capitale de la France ?
(a) Marseille  
(b) Nice
(c) Paris
(d) Nantes

Votre réponse :
Bonne réponse / Mauvaise réponse

...
Question : Quelle est la capitale de l'Italie 
...
  
"""


def afficher_la_bonne_reponse1():
    print("Quelle est la capitale de la France ?")
    print("(a) Marseille")
    print("(b) Nice")
    print("(c) Paris")
    print("(d) Nantes")
    
    reponse = input("Quel est votre choix parmis les réponses possibles ?")
    choix = "c"
    if reponse == choix:
        print("Bravo : Bonne réponse")
    else:
        print("Mausaive réponse")
        
def afficher_la_bonne_reponse2():
    print("Quelle est la capitale de l'italie ?")
    print("(a) Milan")
    print("(b) Rome")
    print("(c) Venise")
    print("(d) Naples")
    
    reponse = input("Quel est votre choix parmis les réponses possibles ?")
    choix = "b"
    if reponse == choix:
        print("Bravo : Bonne réponse")
    else:
        print("Mausaive réponse")
    
    
afficher_la_bonne_reponse1()
afficher_la_bonne_reponse2()