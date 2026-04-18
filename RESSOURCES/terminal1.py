# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat
subprocess.run("dir", shell=True)  # dir sur PC