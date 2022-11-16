    
# Incluya el código del ejercicio 10-6 en un bucle while para que el usuario 
# pueda seguir introduciendo n'umeros aunque se equivoquen y metan texto en 
# vez de un número

print("Vamos a hacer una suma de dos numeros.")
print("Ingrese 'q' para finalizar el programa. ")

while True:
    numero_uno = input("\nIngrese el primer numero: ")
    if numero_uno == 'q':
        print("---PROGRAMA FINALIZADO---")
        break
    numero_dos = input("Ingrese el segundo numero: ")
    if numero_dos == 'q':
        print("---PROGRAMA FINALIZADO---")
        break
    
    try:
        resultado = int(numero_uno) + int(numero_dos)
    except ValueError:
        print("\nSolo pueden sumarse numeros")
    else:
        print(f"\nEl resultado de {numero_uno} + {numero_dos} es: {resultado}")