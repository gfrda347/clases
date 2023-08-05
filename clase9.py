#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def __str__(self):
        propietarios_str = ", ".join(self.propietarios)
        return f"Número de cuenta: {self.numero_cuenta}, Propietarios: {propietarios_str}, Balance: {self.balance:.2f}"

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("No hay suficiente saldo en la cuenta.")


# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Santiago", "Sara"], 5000)

print(cuenta1) 
cuenta1.retirar(3000)

print(cuenta1)  

cuenta1.retirar(3000)

