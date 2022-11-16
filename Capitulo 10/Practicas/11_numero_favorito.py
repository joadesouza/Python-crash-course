#   Escriba un programa que pida al usuario su numero favorito.
#   Utilice json.dumb() para guardar ese número en un archivo.
#   Escriba un programa aparte que lea ese valor e imprima el mensaje "Se cual 
# es tu numero favorito... es el ___"


import json

filename = 'numero_fav.json'
num = input("Por favor, ingrese su numero favorito: ")
try:
    with open(filename) as f:
        num_fav = json.load(f)
        print(f"\nTu numero favorito es el {num_fav}")
except FileNotFoundError:
    pass
else:
    with open(filename, 'w') as f:
        json.dump(num, f)
        print("Ya se cual es tu numero favorito, jeje")
    