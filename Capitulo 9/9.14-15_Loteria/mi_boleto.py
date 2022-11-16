mi_boleto = [7,9,3,'c']
intentos = 0
import Loteria

nuevo_boleto_ganador = Loteria.numeros_ganadores

while mi_boleto in nuevo_boleto_ganador:
    intentos += 1
    print(f"Intento numero: {intentos}")