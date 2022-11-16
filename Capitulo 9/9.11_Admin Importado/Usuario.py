"""La clase que guarda los usuarios y sus datos"""

class Usuario:
    """Creara usuario con nombre y apellido"""
    def __init__(self, nombre, apellido, username, ubicacion):
        """Inicializa los atributos de nombre y apellido"""
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.ubicacion = ubicacion
    
    def describir_usuario(self):
        """Describe al usuario por nombre y apellido"""
        nombre_completo = f"{self.nombre} {self.apellido}"
        print(f"El nombre real del usuario {self.username} es {nombre_completo.title()} y se registro desde {self.ubicacion}")
    
    def saludar_usuario(self):
        """Saluda al usuario"""
        print(f"Hola {self.nombre.title()}!! :D")