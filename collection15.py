# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"


# extraire l'extension du fichier

def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return nom_fichier_split[-1]
    return None

# faire la correspondance avec les définition

def obtenir_definition_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
        return None
    
    

fichiers = ["notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpg", "planning",
            "data.dat"]

definition_extensions = (("exe", "Executable"),
                         ("doc", "Document Word"),
                         ("txt", "Document Texte"),
                         ("jpg", "Image JPEG")
    
)

definition_extensions_dict = {"exe": "Executable",
                         "doc": "Document Word",
                         "txt": "Document Texte",
                         "jpg": "Image JPEG"}


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        #definition = obtenir_definition_extension(ext, definition_extensions)
        definition = definition_extensions_dict.get(ext.lower())
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")

"""
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)

"""

# lower / upper
# in / index / for
# split
# -1


