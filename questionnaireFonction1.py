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
4 questions
"""
"""
print("Quelle est la capitale de la France ?")
print("(a) Marseille")
print("(b) Nice")
print("(c) Paris")
print("(d) Nantes")
    
reponse = input("Votre réponse :")
if reponse == "c":
    print("Bonne réponse")
else:
    print("Mausaive réponse")
        
print()
print("Quelle est la capitale de l'italie ?")
print("(a) Rome")
print("(b) Venise")
print("(c) Pise")
print("(d) Florence")
    
reponse = input("Votre réponse :")
if reponse == "a":
    print("Bonne réponse")
else:
    print("Mausaive réponse")
"""

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    print(question)  
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    reponse = input("Votre réponse :")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
    else:
        print("Mausaive réponse")
    
poser_question("Question : Quelle est la capitale de la france ?", "(a) Marseille", "(b) Nice", "(c) Paris", "(d) Nantes", "c")