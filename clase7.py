#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def __str__(self):
        propietarios_str = ", ".join(self.propietarios)
        return f"Número de cuenta: {self.numero_cuenta}, Propietarios: {propietarios_str}, Balance: {self.balance:.2f}"

cuenta1 = CuentaBancaria("123456789", ["John Doe", "Jane Smith"], 5000)
cuenta2 = CuentaBancaria("987654321", ["Alice Johnson"], 10000.50)

print(cuenta1)
print(cuenta2)

