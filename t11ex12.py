# Afegir noms dels professors
professors = ["Professor A", "Professor B"]
with open(fitxer_path, 'a') as fitxer:
    fitxer.write("\n" + "\n".join(professors))

# Llegir el fitxer i posar el contingut en una llista
with open(fitxer_path, 'r') as fitxer:
    noms = fitxer.readlines()
noms = [nom.strip() for nom in noms]
print(noms)