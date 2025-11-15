def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION") 
    print(" " + question[0])
    for i in range(len(choix)):
        print(" ", i+1, "-", choix[i])
    
    reponse_str = input("Votre réponse (entre 1 et " + str(len(choix)) + ") :")
    reponse_int = int(reponse_str)
    
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score +=1
    else:
        print("Mausaive réponse")
    print()


score = 0


'''
    questionnaire[]
    question
        titre = "Quelle est la capitale de la France"
        reponses = ("Marseille", "Nice", "Paris", "Nantes")
        lettre_bonne_reponse = "Paris"
        
        
'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

'''
titre = question[0]
choix = question[1]
'''

poser_question(question1)
poser_question(question2)

# poser_question("Quelle est la capitale de la france ?", "Marseille", "Nice", "Paris", "Nantes", "c")
# poser_question("Quelle est la capitale de l'italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)