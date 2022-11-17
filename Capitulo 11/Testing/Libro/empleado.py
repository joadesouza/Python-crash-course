class Empleado:
    """
    guarda datos de un empleado"""
    def __init__(self, nombre, apellido, salario_anual):
        """Guarda nombre apellido y salario"""
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.salario_anual = salario_anual
        
    def dar_aumento(self, monto_aumento):
        """Otorga un aumento de 5000 al salario anual o un monto
        presonalizado """
        if monto_aumento:
            self.salario_anual += monto_aumento
            print(f"Su sueldo anual obtuvo un ingreso de {monto_aumento}, su nuevo salario anual es de {self.salario_anual}")
            
        else:
            self.salario_anual += 5000
            print(f"Su sueldo anual obtuvo un ingreso de 5000, su nuevo salario anual es de {self.salario_anual}")
               
      
# nombre = input("Ingrese el nombre del empleado: ")
# apellido = input("Ingrese el apellido del empleado: ")
# salario_anual = input("Ingrese el salario anual del empleado")