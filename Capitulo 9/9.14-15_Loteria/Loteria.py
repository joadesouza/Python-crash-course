loteria = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
n=0
numeros_ganadores = []


from random import choice

while n < 4:
    resultado_loteria = choice(loteria)
    if resultado_loteria in numeros_ganadores:
        continue
    else:
        numeros_ganadores.append(resultado_loteria)
        n += 1

print(f"Los numeros ganadores son: {numeros_ganadores}")

mi_boleto = (7,9,3,'c')
intentos = 1
n = 0
ng = 0
boleto_ganador = False
# Prueba para verificar que controle bien los numeros ganadores
# numeros_ganadores = ['c',9,7,3]

while boleto_ganador == False:
    for numero in numeros_ganadores:
        if numero in mi_boleto:
            ng += 1
        else:
            continue
    
    if ng == 4:
        print(f"Felicidades!!! Ganaste la loteria despues de {intentos} intentos")
        boleto_ganador = True
    else:
        numeros_ganadores = []
        while n < 4:
            resultado_loteria = choice(loteria)
            if resultado_loteria in numeros_ganadores:
                continue
            else:
                numeros_ganadores.append(resultado_loteria)
                n += 1
        intentos += 1
        print(f"Intento numero: {intentos}")
        print(f"Los numeros ganadores son: {numeros_ganadores}\n")
    n = 0
    numeros_ganadores = ()