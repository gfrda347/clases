class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distancia(self, otro_punto):
        """
        Calcula la distancia entre este punto y otro_punto utilizando la fórmula
        de distancia euclidiana en el plano cartesiano.
        """
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5
