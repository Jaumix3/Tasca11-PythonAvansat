def concatena_amb_connector(l1, l2, connector):
    return ["{}{}{}".format(a, connector, b) for a, b in zip(l1, l2)]

# Programa Principal
l1 = ["Pere", "Jordi"]
l2 = ["Gomila", "Melià"]
connector = ' '
resultat = concatena_amb_connector(l1, l2, connector)
print(resultat)  
