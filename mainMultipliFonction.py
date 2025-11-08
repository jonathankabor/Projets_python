"""
EXERCICE FONCTIONS
Tables de multiplication

1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
... 
10 * 4 = 40

afficher_table_multiplication(n)
min / max
erreur : si min > max => erreur   
"""



def afficher_table_multiplication(n):
    min = 1
    max = 10
    for i in range(min, max+1):
        print(i, "x", n, "=", i*n)
        
afficher_table_multiplication(4)