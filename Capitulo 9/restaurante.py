

"""Una clase para usar con cualquier tipo de restaurante o local de comida"""

class Restaurante:
    """Creacion de un restaurante"""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre del resto y tipo de cocina"""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        """describe el restaurante"""
        print(f"Este restaurante se llama {self.nombre_restaurante.title()}")
        print(
            f"{self.nombre_restaurante.title()} realiza platos del tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Imprime mensaje avisando que esta abierto el restaurante"""
        print(
            f"Atencion! {self.nombre_restaurante.title()} ya abrio sus puertas!")

    def establecer_numero_servido(self, actualizacion_servido):
        """Actualiza la cantidad de clientes atendidos"""
        if actualizacion_servido >= 0:
            print("Actualizando numero de clientes atendidos...\n")
            self.numero_servido += actualizacion_servido
            print(
                f"La cantidad de clientes atendidos es de: {self.numero_servido}\n")
        else:
            print(
                f"La cantidad de clientes atendidos sigue siendo {self.numero_servido}\n")

    def incrementar_numero_servido(self, incremento_clientes):
        """Incrementa el numero de clientes atendidos"""
        if incremento_clientes >= 0:
            self.numero_servido += incremento_clientes
            print(f"El numero de clientes atendidos es: {self.numero_servido}")
        else:
            print(
                f"El numero de clientes atendidos sigue siendo: {self.numero_servido}")


