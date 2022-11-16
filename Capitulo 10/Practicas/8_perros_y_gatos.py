# Haga dos archivos, gatos.txt y perros.txt. Guarde al menos tres nombres de 
# gato en el primero y tres nombres de perro en el segundo. 
"""

with open('Practicas/gatos.txt', "w") as g:
    while True:
        nombre_gato = input("Ingrese el nombre del gato, o envie 'q' para finalizar: ")
        if nombre_gato == 'q':
            break
        g.writelines(f"{nombre_gato.title()}")
        
with open('Practicas/perros.txt', "w") as p:
    while True:
        nombre_perro = input("Ingrese el nombre del perro, o envie 'q' para finalizar: ")
        if nombre_perro == 'q':
            break
        p.writelines(f"{nombre_perro.title()}")

"""

# Escriba un programa que intente leer estos archivos para imprimir su 
# contenido en la pantalla. 
# Ponga el código en un bloque try-except para 
# capturar el error FileNotFound e imprima un mensaje si falta un archivo. 
# Mueva uno de los archivos a una ubicacion distinta en su sistema y asegurese
# de que el código del bloque except se ejecuta correctamente.

filenames = ['Practicas/gatos.txt', 'perros.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            lines = f.readlines()
            print(f"\nThe names in {filename} are: ")
    except FileNotFoundError:
        print(f"\nEl archivo {filename} no se encontro en la ubicacion seleccionada...")
    else:
        for line in lines:
            print(line.strip())