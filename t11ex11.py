def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as fitxer:
            return fitxer.readlines()
    except FileNotFoundError:
        return "Error: El fitxer no existeix"
    except Exception as e:
        return f"S'ha produït un error: {e}"