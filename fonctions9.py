# PYTHON FONCTIONS : NOTIONS AVANCEES
#
# CALLBACK
#

"""
def ma_fonction():
    print("toto")
    return 1

a = 5

b = ma_fonction

print("a", a, "b", ma_fonction())

"""
"""

def afficher_table_multiplication(n):
    for i in range(1, 10+1):
        print(i, "x", n, "=", i*n)

def afficher_table_addition(n):
    for i in range(1, 10+1):
        print(i, "+", n, "=", i+n)
        
"""

"""
        
def mult_callback(a, b):
    return a*b

def add_callback(a, b):
    return a+b

def power_callback(a, b):
    return pow(a, b)

"""
      
def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1, 10+1):   
        print(i, operateur_str, n, "=", operation_cbk(i, n))   
        
# FONCTIONS LAMBDA

afficher_table(2, "x", lambda a, b, : a*b)
print()
afficher_table(2, "+", lambda a, b, : a+b)
print()
afficher_table(2, "^", lambda a, b, : pow(a, b))

