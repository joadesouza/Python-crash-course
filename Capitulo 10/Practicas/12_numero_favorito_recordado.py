# Combine los dos programas del ejercicio anterior en uno solo. Si el numero 
# ya esta guardado diga al usuario cual es su numero favorito. 
# Si no, solicitelo al usuario y guardelo en un archivo. 
# Ejecute el programados veces para ver si funciona

import json

filename = 'numero_fav.json'
try:
    with open(filename) as f:
        num_fav = json.load(f)
        print(f"Tu numero favorito es el {num_fav}")
except FileNotFoundError:
    with open(filename, 'w') as f:
        num = input("Por favor, ingrese su numero favorito: ")
        json.dump(num, f)
        print(f"Tu numero favorito es el {num}\n")
else:
    print("Ya se cual es tu numero favorito, jeje\n")
