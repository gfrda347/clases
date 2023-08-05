
#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.class Punto:
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def calcular_distancia(self, otro_punto):
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5

punto1 = Punto(2, 3)
punto2 = Punto(5, 7)
punto1.mostrar()  

punto1.mover(4, 6)
punto1.mostrar() 

distancia_entre_puntos = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia_entre_puntos)  