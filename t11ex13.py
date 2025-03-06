from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat
    
    @abstractmethod
    def xerrar(self):
        pass
    
    @abstractmethod
    def mourem(self):
        pass
    
    def quisoc(self):
        return f"Soc un {self.especie} de {self.edat} anys."

class Cavall(Animal):
    def xerrar(self): return "Hiiii"
    def mourem(self): return "Galopa"

class Dofi(Animal):
    def xerrar(self): return "Clac clac"
    def mourem(self): return "Neda"

class Abella(Animal):
    def xerrar(self): return "Bzzz"
    def mourem(self): return "Vola"
    def picar(self): return "Pica amb el fibló"

class Huma(Animal):
    def __init__(self, nom, edat):
        super().__init__("Huma", edat)
        self.nom = nom
    def xerrar(self): return "Hola!"
    def mourem(self): return "Camina"

class Fiet(Huma):
    def __init__(self, nom, edat, pares):
        super().__init__(nom, edat)
        self.pares = pares
    def nompares(self): return ", ".join(self.pares)

class Centaure(Cavall, Huma):
    def __init__(self, nom, edat):
        Huma.__init__(self, nom, edat)
        Cavall.__init__(self, "Centaure", edat)

class Xou:
    def xerrar(self): return "Soc un Xou"
    def mourem(self): return "Mourem diferent"
    def quisoc(self): return "Soc un Xou únic"

# Creació d'una llista d'animals i crida als mètodes
animals = [Cavall("Cavall", 5), Dofi("Dofi", 3), Abella("Abella", 1), Huma("Joan", 30), Centaure("Chiron", 100), Xou()]
for animal in animals:
    print(animal.quisoc())
    print(animal.xerrar())
    print(animal.mourem())