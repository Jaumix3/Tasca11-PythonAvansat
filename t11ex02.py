from functools import reduce

def Passar_a_Numero(l):
    return reduce(lambda x, y: x * 10 + y, l)

# Programa Principal
l = [3, 4, 1, 5]
resultat = Passar_a_Numero(l)
print(resultat)
