class Car:
    """Un simple intento de representar un coche"""
    
    def __init__(self, make, model, year):
        """Inicializa atributos para describir un coche"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reader = 0
        
    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con el formato adecuado"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Escribe una oracion que dice cuantos kilometros tiene el auto"""        
        print(f"Este {self.make.title()} ahora tiene {self.odometer_reader} km")

    def actualizacion_odometer(self, mileage):
        """
        Configura el cuentakilometros con el valor dado.
        Rechaza el cambio si se intenta hacer retroceder el cuentakilometros
        """
        if mileage >= self.odometer_reader:
            self.odometer_reader = mileage
            
        else:
            print("Ah ah aaah, no podes bajar el kilometrajo gato!")
            print(f"Este auto sigue teniendo los mismos {self.odometer_reader} kilometros")
    
    def increment_odometer(self, mile):
        """Incrementa el kilometraje del vehiculo"""
        if mile < 0:
            print("Eeeeeh que haces gil, vola de aca... no podes restar")
            print(f"El kilometraje sigue siendo de {self.odometer_reader}")
        else:
            self.odometer_reader += mile
            print(f"Ahora el kilometraje es de {self.odometer_reader}")

class Battery:
    """Un simple intento de modelar una bateria de auto electrico"""
    
    def __init__(self, battery_size=75):
        """Inicializa los atributos de la bateria"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Describe la capacidad de la bateria"""
        print(f"La capacidad de la bateria es de {self.battery_size}Kw") 
        
    def get_range(self):
        """Imprime una frase sobre la autonomia que ofrece esta bateria"""
        if self.battery_size < 75:
            range = 15
        elif self.battery_size = 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"Este auto puede recorrer unos {range} kilometros aproximadamente")
        
    def upgrade_battery(self):
        """Carga la bateria al 100"""
        if self.battery_size != 100:
            print("Cargando bateria...")
            self.battery_size = 100
            print(f"\nBateria cargada al {self.battery_size}")
        else:
            print("La bateria ya esta a su maima capacidad! :)")

class ElectricCar(Car):
    """Representa aspectos de un coche propio de los vehiculos electricos """           
    def __init__(self, make, model, year):
        """inicializa los atributos de la clase base"""
        super().__init__(make, model, year)
        

# mytesla = ElectricCar('tesla', 'model s', 2019)

# print(mytesla.get_descriptive_name())

# mytesla.battery.describe_battery()
# mytesla.battery.get_range()
# # Cargar bateria al 100
# mytesla.battery.charge_battery(100)
# mytesla.battery.get_range()