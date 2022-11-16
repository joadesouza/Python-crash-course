"""Una clase sobre los privilegios de los usuarios administradores"""

class Privilegios:
    """Clase de los diferentes privilegios del administrador... supongo"""
    def __init__(self, privilegios):
        self.privilegios = []

    def show_privileges(self):
        """Muestra todos los privilegios del administrador"""
        print("\nLos privilegios que tiene el admin son los siguientes: ")
        for privi in self.privilegios:
            print(f"\t- {privi.capitalize()}")
        print()
    
    def add_privileges(self):
        """Agrega nuevos privilegios de admin"""
        question = input("Desea agregar un privilegio al admin? si/no: ")
        while question == "si":    
            self.privilegios.append(input("Ingrese un nuevo privilegio para agregar: "))
            question = input("Desea agregar otro privilegio al admin? si/no: ")

        print("La lista de privilegios fue actualizada")
        for privi in self.privilegios:
            print(privi)