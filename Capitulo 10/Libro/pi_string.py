filename = 'libro/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = '' #En esta variable guardaremos los digitos de pi que leeremos de cada linea
for line in lines: #El bucle permite añadirlos a la variable
    pi_string += line.rstrip() #3.1415926535 8979323846 2643383279

print(pi_string)
print(len(pi_string))

"""Para eliminar el espacio en blanco que habia a la izquierda de cada linea usaremos rstrip()"""

filename = 'libro/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = '' #En esta variable guardaremos los digitos de pi que leeremos de cada linea
for line in lines: #El bucle permite añadirlos a la variable
    pi_string += line.strip() #3.141592653589793238462643383279

print(pi_string)
print(len(pi_string))
print()

"""Trabajar con un archivo grande de 1 millon de numeros y mostrar X cantidad de numeros"""

filename = 'libro/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = '' #En esta variable guardaremos los digitos de pi que leeremos de cada linea
for line in lines: #El bucle permite añadirlos a la variable
    pi_string += line.strip() 

print(f"{pi_string[:52]}...")
print(f"Cantidad de caracteres: {len(pi_string)}")
print()

birthday = input("Ingrese su fecha de cumpleaños en el siguiente formato ddmmaa: ")
if birthday in pi_string:
    print("Tu cumpleaños aparece dentro del primer millon de digitos de Pi!! :D ")
else:
    print("Que lastima, tu cumpleaños no se encuentra en Pi :(")