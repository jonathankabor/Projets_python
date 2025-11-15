def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input("Votre réponse (entre" + str(min) + "et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min, max)


def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION") 
    print(" " + question[0])
    for i in range(len(choix)):
        print(" ", i+1, "-", choix[i])
        
    print() 
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))
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