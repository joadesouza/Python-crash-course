"""Una clase Admin que guarda los datos de los usuarios administradores"""
from Usuario import Usuario

class Admin(Usuario):
    """Esta clase heredara los atributos de la clase usuario del ejercicio 9.5"""
    def __init__(self, nombre, apellido, username, ubicacion):
        "inicializa los atributos de la clase Usuario"
        super().__init__(nombre, apellido, username, ubicacion)
        self.privilegios = ["puede añadir comentario", "puede borrar comentario", 
                            "puede vetar usuarios", "puede culiar travestis"]