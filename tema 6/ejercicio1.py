from abc import ABC, abstractmethod
from tokenize import PseudoExtras

class Vehiculo:
    color = "no especificado"
    ruedas = 2
    puertas = 2

class Coche(Vehiculo):

    velocidad = 444
    cilindrada = 555
    
    
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color
        self.ruedas = 4
        self.puertas = 5

c1 = Coche("rojo")
print("color", c1.color)
print("puertas", c1.puertas)
print("ruedas",c1.ruedas)
print("cilindrada",c1.cilindrada)
print("velocidad",c1.velocidad)


    
