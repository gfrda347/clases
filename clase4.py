#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectángulo:
    def __init__(self, punto1, punto2):
        self.esquina_sup_izq = punto1
        self.esquina_inf_der = punto2

    def calcular_lados(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return base, altura

    def calcular_perímetro(self):
        base, altura = self.calcular_lados()
        return 2 * (base + altura)

    def calcular_area(self):
        base, altura = self.calcular_lados()
        return base * altura

    def es_cuadrado(self):
        base, altura = self.calcular_lados()
        return base == altura

punto1 = Punto(1, 3)
punto2 = Punto(6, 1)
rectangulo = Rectángulo(punto1, punto2)

print("Esquina superior izquierda:", rectangulo.esquina_sup_izq)
print("Esquina inferior derecha:", rectangulo.esquina_inf_der)

perimetro = rectangulo.calcular_perímetro()
print("Perímetro del rectángulo:", perimetro)

area = rectangulo.calcular_area()
print("Área del rectángulo:", area)

es_cuadrado = rectangulo.es_cuadrado()
print("¿El rectángulo es un cuadrado?", es_cuadrado)
