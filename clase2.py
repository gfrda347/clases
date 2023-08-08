#Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

punto1 = Punto(3, 5)
punto2 = Punto(-2, 7)

print("Coordenadas del punto 1:", punto1) 
print("Coordenadas del punto 2:", punto2)  