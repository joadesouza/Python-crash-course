"""Una clase con las caras de un dado"""
from random import randint

class Dados:
    """simula un dado de 6 caras"""
    def __init__(self, caras=6):
        self.caras = caras
        
    def tirar_dados(self):
        resultado = randint(1,self.caras)
        print(f"El dado de {self.caras} caras cayó en {resultado}")
    
    def tirar_dado10(self):
        self.caras = 10
        resultado = randint(1,self.caras)
        print(f"El dado de {self.caras} caras cayó en {resultado}")
        
    def tirar_dado20(self):
        self.caras = 20
        resultado = randint(1,self.caras)
        print(f"El dado de {self.caras} caras cayó en {resultado}")