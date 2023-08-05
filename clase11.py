#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
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

    def aplicar_cuota_manejo(self):
        cuota_manejo = 0.02 * self.balance
        self.balance -= cuota_manejo

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print("Propietarios:")
        for propietario in self.propietarios:
            print(f"  - {propietario}")
        print(f"Balance: {self.balance:.2f}")

cuenta1 = CuentaBancaria("123456789", ["Santiago", "Sara"], 5000)
cuenta1.mostrar_detalles()
