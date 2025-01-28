def lenp(frase):
    paraules = frase.split()
    long = list(map(len, paraules))
    return long

#Programa Principal
frase = "En Pere la té petita"
resultat = lenp(frase)
print("Les longituds de cada paraula són: {}".format(resultat))

