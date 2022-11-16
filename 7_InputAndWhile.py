"""
print("\n//////////////////////////////")
print("///////EJERCICIO 7.1/////////")
print("/////////////////////////////\n")
"""
# COCHE DE ALQUILER: Escriba un programa que pregunte al usuario que tipo de 
# coche desea alquilar. Imprima un mensaje sobre el coche, como "Veamos si 
# tenemos un Subaru para usted."
"""
mens = "Que tipo de auto esta buscando señor?"
mens += "\nPodria especificarnos la marca por favor?: "

auto = input(mens)
print(f"\nAguarde, veremos si tenemos un {auto.title()} disponible para usted")
"""

"""
print("\n//////////////////////////////")
print("///////EJERCICIO 7.2/////////")
print("/////////////////////////////\n")
"""

# MESA EN UN RESTAURANTE: Escriba un programa que pregunte al usuario cuantos 
# vienen a cenar. Si la respuesta es mas de ocho, imprima un mensaje diciendo 
# al usuario que tendran que esperar mesa. De lo contrario, digale que su mesa 
# esta lista.
"""
comensales = int(input("Buenas noches señor, cuantas personas vienen a cenar?: "))

if comensales > 8:
    print(f"\nLo lamento señor, tendra que aguardar un poco mas")
elif comensales == 0:
    print(f"\nSeñor, me esta cachando? Si vienen {comensales} personas a cenar no puedo darles una mesa")
else:
    print(f"\nAdelante señor, tenemos libre una mesa disponible para {comensales} personas")
"""

print("\n//////////////////////////////")
print("///////EJERCICIO 7.3/////////")
print("/////////////////////////////\n")

# MULTIPLOS DE DIEZ: Pida al usario un numero y luego informele de si ese numero
# es multiplo de 10 o no.
"""
numero = int(input("Ingrese un numero y le dire si es multiplo de 10 o no:  "))

if numero % 10 == 0:
    print(f"\nEl numero {numero} es multiplo de 10")
else:
    print(f"\nEl numero {numero} no es multiplo de 10.")
"""
print("\n//////////////////////////////")
print("///////EJERCICIO 7.4/////////")
print("/////////////////////////////\n")

# INGREDIENTES DE PIZZA: Escriba un bucle que pida al usuario que introduzca 
# una serie de ingredientes de pizza y termine escribiendo el valor 'quit'. 
# Cuando introduzca cada ingrediente, imprima un mensaje diciendo que lo 
# añadirá a su pizza
"""
mens = "\nPor favor, indicanos que ingrediente quieres en tu pizza y presione Enter"
mens += "\n(Escriba 'quit' cuando termine)  "

ingredientes_pizza = ""
active = True

while active:
    ingredientes_pizza = input(mens)
    
    if ingredientes_pizza != 'quit':
        print(f"Excelente, agregaremos {ingredientes_pizza.title()} a la pizza")
    else:
        active = False
        print("Gracias, pronto prepararemos tu pedido...")
"""

print("\n//////////////////////////////")
print("///////EJERCICIO 7.5/////////")
print("/////////////////////////////\n")

# ENTRADAS DE CINE: Un cine cobra las entradas a distinto precio en funcion 
# de la edad del espectador. Los menores de 3 años entran gratis, los niños 
# de entre 3 y 12 años pagan 8 euros y la entrada para mayores es de 12 años
# cuesta 12 euros. Escriba un bucle para preguntar a los usuarios su edad y 
# luego digales el precio de su entrada.
"""
mens = "\nIngrese su edad para saber cuanto tiene que abonar: "

while True:
    edad = int(input(mens))
    if edad <= 3:
        print(f"\nEl precio de la entrada es gratuita, adelante!")
        break
    elif edad <= 12:
        print("\nLa entrada te costara 8 euros")
        break
    else:
        print("\nya esta grande señor, debera abonar 12 euros")
        break
"""
"""print("\n//////////////////////////////")
print("///////EJERCICIO 7.6/////////")
print("/////////////////////////////\n")
"""
# TRES SALIDAS: Escriba distintas versiones del ejercicio 7.4 o 7.5 haciendo
# lo siguiente como minimo una vez:
# Use una prueba condicional en la sentencia while para detener el bucle
# Use una variable active para controlar cuanto tiempo se ejecuta el bucle
# Use una sentencia break para salir del bucle cuando el usuario introduzca 
# el valor 'quit'

"""print("\n//////////////////////////////")
print("///////EJERCICIO 7.8/////////")
print("/////////////////////////////\n")
"""
# Haga una lista que se llame pedidos_bocadillos y rellenela con nombres de 
# varios bocadillos. Luego haga una lista vacia y llamela bocadillos_terminados.
# Pase en bucle por la lista de pedidos e imprima un mensaje para cada pedido 
# "Su pedido de atun ya esta listo".
# A medida que se hagan los bocadillos paselos a la lista de terminados, 
# cuando todos los bocadillos esten hechos imprima un mensaje que los enumere 
# a todos.

print("\n//////////////////////////////")
print("///////EJERCICIO 7.9/////////")
print("/////////////////////////////\n")

# YA NO HAY PASTRAMI: Usando la lista de pedidos_bocadillos del ejercicio 7.8,
# asegurese que el bocadillo "pastrami" este incluido al menos tres veces. 
# Añada código al principio del programa para decir que no queda mas pastrami
# y use un bucle while para eliminar todas las apariciones de pastrami dentro 
# de la lista. 
# Asegurese que no pasa ningun Pastrami a la lista de terminados

print('SU ATENCION POR FAVOR!! No queda mas pastrami para ordenar')
pedidos_bocadillos = [
    'albondigas', 'pastrami','salchichas', 'papitas', 'pastrami', 
    'huevos honguito', 'pastrami'
    ]
bocadillos_terminados = []

while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')
    
while pedidos_bocadillos:
    bocadillo = pedidos_bocadillos.pop()
    
    print(f"Su pedido de bocadillo de {bocadillo.title()} esta listo")
    bocadillos_terminados.append(bocadillo)
    
for bocadillo in bocadillos_terminados:
    print(bocadillo.title())
    

print(f"lista terminados: {bocadillos_terminados}")
print(f"lista pedidos: {pedidos_bocadillos}")


print("\n//////////////////////////////")
print("///////EJERCICIO 7.10/////////")
print("/////////////////////////////\n")

# VACACIONES DE ENSUEÑO: Escriba un programa que pregunte a los usuarios por 
# las vacaciones de sus sueños. 
# Escriba unas instrucciones como "Si pudieras visitar cualquier lugar del 
# mundo, a donde irias??"
# Escriba un bloque que imprima el resultado de la encuesta

print("-----------------------")
print("VACACIONES DE ENSUEÑO!!")
print("-----------------------")

encuesta = {}
flag = True

while flag:
    usuario = input("Hola! Como es tu nombre?\n")
    lugar = input("Si pudieras elegir un pais en el mundo al cual viajar, a donde irias??\n")
    freno = input("Alguien mas quiere responder la encuesta? si/no: ")
    encuesta[usuario] = lugar
    
    if freno == "no":
        flag = False
        
for user, response in encuesta.items():
    print(f"Si {user.title()} pudiera viajar a un pais, seria a {response.title()}")    