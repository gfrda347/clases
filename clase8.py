#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def __str__(self):
        propietarios_str = ", ".join(self.propietarios)
        return f"Número de cuenta: {self.numero_cuenta}, Propietarios: {propietarios_str}, Balance: {self.balance:.2f}"

    def depositar(self, monto):
        """
        Realiza un depósito en la cuenta bancaria.
        """
        self.balance += monto

cuenta1 = CuentaBancaria("123456789", ["John Doe", "Jane Smith"], 5000)

print(cuenta1)  

cuenta1.depositar(1500)

print(cuenta1) 
