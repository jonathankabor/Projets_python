# TÉLÉCHARGER UNE IMAGE AVEC REQUESTS
#
# https://codeavecjonathan.com/res/papillon.jpg

import sys
sys.path.append(r"C:\Users\Hp\Projets_python\myenv\Lib\site-packages")

import requests

reponse = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
if reponse.status_code == 200:
    f = open("papillon.jpg", "wb")
    f.write(reponse.content)
    f.close()
    print("Ecriture terminée")
else:
    print("ERREUR ", reponse.status_code)
