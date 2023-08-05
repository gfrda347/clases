#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_al_centro = ((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2) ** 0.5
        return distancia_al_centro <= self.radio



centro = Punto(2, 3)
radio = 5
circulo = Circulo(centro, radio)

print("Centro del círculo:", circulo.centro)
print("Radio del círculo:", circulo.radio)

area = circulo.calcular_area()
print("Área del círculo:", area)

perimetro = circulo.calcular_perimetro()
print("Perímetro del círculo:", perimetro)

punto1 = Punto(6, 4)
punto2 = Punto(8, 2)
print("¿El punto (6, 4) pertenece al círculo?", circulo.punto_pertenece(punto1))  
print("¿El punto (8, 2) pertenece al círculo?", circulo.punto_pertenece(punto2)) 