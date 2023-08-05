#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
class Carta:
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return f"{self.valor} de {self.pinta}"

carta1 = Carta("10", Carta.CORAZON)
carta2 = Carta("A", Carta.TREBOL)

print(carta1) 
print(carta2)  
