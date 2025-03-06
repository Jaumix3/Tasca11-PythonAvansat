# Funció per controlar la divisió per zero
def divisio_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No es pot dividir per zero"
print(divisio_segura(10, 0))