# Un problema habitual cuando se pide entrada numérica se da cuando la gente
# proporciona texto en vez de números. Cuando intentamos convertir la entrada
# de un entero, obtenemos un ValueError.

# Escriba un programa que solicite dos números, súmelos e imprima el resultado.
# Capture el ValueError si cualquiera de los valores de entrada no es un número
# e imprima un error inteligible para el usuario. Pruebe el programa introduciendo
# dos números y luego escribiendo texto en vez de un número.

numero_uno = input("\nIngrese el primer numero: ")
numero_dos = input("Ingrese el segundo numero: ")

try:
    resultado = int(numero_uno) + int(numero_dos)
except ValueError:
    print("\nSolo pueden sumarse numeros")
else:
    print(f"\nEl resultado de {numero_uno} + {numero_dos} es: {resultado}")
