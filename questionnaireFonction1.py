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
    global score
    print("score:", score)
    print("QUESTION") 
    print(" " + question)
    print(" (a)", r1)
    print(" (b)",r2)
    print(" (c)",r3)
    print(" (d)",r4)
    reponse = input("Votre réponse :")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score +=1
    else:
        print("Mausaive réponse")
    print()


score = 0

poser_question("Quelle est la capitale de la france ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)