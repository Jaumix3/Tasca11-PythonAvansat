def paraules_que_comencen(per_paraules, lletra):
    return list(filter(lambda paraula: paraula.startswith(lletra), per_paraules))

llista = ["maria", "manta", "peu", "mà"]
lletra = "p"
resultat = paraules_que_comencen(llista, lletra)
print(resultat)