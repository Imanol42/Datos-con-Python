class CuentaBanco:
    def __init__(self,nombre,apellido,edad,correo,pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.pais = pais

class MovimientosBancarios:
    def __init__(self,cliente,saldo):
        self.cliente = cliente
        self.saldo = saldo
    
    def egreso(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return print(f"egreso exitoso! tu nuevo saldo es de: {self.saldo}")
        else:
            print(f"no puedes retirar esa cantidad. tu saldo actual es de: {self.saldo}")
    
    def ingreso(self,cantidad):
        self.saldo += cantidad
        return print(f"ingreso exitoso! tu nuevo saldo es de: {self.saldo}")

    def total(self):
        return print(f"tu saldo actual es de: {self.saldo}")

persona1 = CuentaBanco("Imanol","Gonzalez",24,"gimanol699@gmail.com","Argentina")

cuenta1 = MovimientosBancarios(persona1,int(input("ingresar saldo actual: ")))

cuenta1.egreso(int(input("ingrese cantidad a retirar: ")))

print(persona1.nombre,persona1.apellido," edad: ",persona1.edad," saldo en cuenta: ",cuenta1.saldo)