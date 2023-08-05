#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self):
        return f"Velocidad máxima: {self.velocidad_maxima} km/h, Kilometraje: {self.kilometraje} km"

vehiculo1 = Vehículo(200, 15000)
vehiculo2 = Vehículo(180, 23000)

print("Vehículo 1:", vehiculo1)  
print("Vehículo 2:", vehiculo2)  
