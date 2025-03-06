
def comptar_coincidencies(llista):
   return sum(1 for i, valor in enumerate(llista) if i == valor)




llista = [0, 2, 3, 3, 4]
resultat = comptar_coincidencies(llista)
print(resultat) 
