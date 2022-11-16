# Ejercicio 8-1. MENSAJE:
# Escriba una funcion llamada mostrar_mensaje() que imprima una oracion 
# diciendo a todos lo que esta aprendiendo en este capitulo. Llame a 
# la funcion y asegurese de que el mensaje se muestra correctamente.

"""def mostrar_mensaje():
    """"imprime una oracion con lo aprendido""""""
    print("\nEn este capitulo vamos a estar aprendiendo todo "
          "sobre las funciones")

mostrar_mensaje()"""

# Ejercicio 8-2. LIBRO FAVORITO:
# Escriba una funcion llamada libro_favorito() que acepte un parametro 
# titulo. La funcion deberia imprimir un mensaje como "Uno de mis libros
# favoritos es Alicia en el Pais de las Maravillas". Llame a la funcion, 
# asegurandose de incluir el titulo de un libro como argumento en la 
# llamada a la funcion
"""
def libro_favorito(parameter):
    """"Imprime tu libro favorito""""
    print(f"\nUno de mis libros favoritos es: {parameter.title()}")

libro_favorito("20.000 leguas de viaje submarino")
"""
# Ejercicio 8.3 CAMISETA: Escriba una funcion llamada hacer_camiseta() 
# que acepte una talla y un texto para un mensaje que habria que imprimir
# en la camiseta. 
# La funcion deberia imprimir una frase resumiendo la talla de la camiseta
# y el mensaje impreso.
# Llame a la funcion una vez con argumentos posicionales para hacer
# una camiseta.
# LLame a la funcion por segunda vez usando argumentos de palabra clave.

# Ejercicio 8.4 CAMISETAS GRANDES: Modifique la funcion hacer_camiseta() 
# para que las camisetas sean grandes por defecto con el mensaje que diga 
# "Me encanta python". 
# Haga una camiseta grande y una mediana con el mensaje predeterminado 
# y una de cualquier talla con un mensaje diferente.
"""
talle = input("Ingrese su talle a continuacion (s/m/l/xl/xxl): ")
mensaje = input("Ingrese el mensaje que desea imprimir en su camiseta: ")

def hacer_camiseta(talle='xl', mensaje='Me encanta Python'):
    """"Muestra talle y lo que va impreso en la camiseta"""""
    print(f'\nSu camiseta talle {talle.upper()} esta lista y se imprimira' 
          f' el siguiente mensaje en ella:\n "{mensaje.capitalize()}"')

hacer_camiseta(talle, mensaje)
hacer_camiseta()
hacer_camiseta(talle='m')
hacer_camiseta(talle='xl', mensaje='D10s')
"""

# Ejercicio 8.5 CIUDADES: Escriba una funcion llamada describir_ciudad() 
# que acepte el nombre de una ciudad y su pais. La funcion deberia imprimir
# una oracion simple como "Reikiavik esta en Islandia". De al parametro 
# del pais un valor predeterminado. Llame a la funcion para tres ciudades
# diferentes, con al menos una que no esté en el pais predeterminado

"""def describir_ciudad(ciudad, pais='Japon'):
    """"Muestra donde esta la ciudad""""
    print(f"\nLa ciudad de {ciudad.title()} se encuentra en {pais.title()}")
    
describir_ciudad('osaka')
describir_ciudad('tokio')
describir_ciudad('rosario de lerma', pais='Argentina')
"""

# Ejercicio 8.6 NOMBRES DE CIUDAD: Escriba una funcion llamada ciudad_pais()
# que admita el nombre de una ciudad y su pais. La funcion deberia devolver
# una cadena con formato, similar a esta: "Santiago, Chile". Llame a su funcion 
# con al menos tres pares de ciudades e imprima los resultados devueltos


"""def ciudad_pais(ciudad, pais):
    """"Genera el detalle de una ubicacion""""
    formato_ubicacion = f"{ciudad}, {pais}"
    return formato_ubicacion.title()

cant = True
while cant:
    a = input("Desea ingresar una nueva ubicacion? si/no: ")
    if a == "no":
        cant = False
        print("----Programa finalizado----")
    else:
        ciudad = input("Ingrese la ciudad: ")
        pais = input("A que pais pertence dicha ciudad?: ")
        ubicacion = ciudad_pais(ciudad, pais)
        print(ubicacion)"""
        
# Ejercicio 8.7 ALBUM: Escriba una funcion llamada hacer_album() que 
# cree un diccionario para describir un album musical. La funcion 
# deberia aceptar un nombre de artista y un titulo de album y deberia 
# devolver un diccionario con estas dos informaciones. Use la funcion 
# para hacer tres diccionarios que representen distintas informaciones. 
# Use la funcion para hacer tres diccionarios que representen distintos 
# albumes. Imprima cada valor devuelto para comprobar que los diccionarios 
# estan almacenando bien la informacion.

# Use None para añadir un parametro opcional a hacer_album() que permita 
# guardar el numero de canciones que contiene un album. Si la linea de 
# llamada incluye un valor para el numero de canciones añadalo al diccionario
# del album. Haga al menos una nueva llamada a la funcion que incluya este 
# dato.


# Ejercicio 8.8 Albumes de Usuario: Empiece con el programa del ejercicio 8.7. 
# Escriba un bucle while que permita a los usuarios introducir el artista y 
# el titulo de un album. Una vez que disponga de esa informacion, llame a 
# hacer_album() con la entrada de usuario e imprima el diccionario que se 
# ha creado. Asegurese de incluir un valor para salir en el bucle while
"""
def hacer_album(artist_name, album_title, tracks=None):
    """"Crea un diccionario para describir un album musical""""
    discos = {'Artista':artist_name.title(), 'Album':album_title.title()}
    if tracks:
        discos['Tracks'] = tracks
    return discos

flag = True

while flag:
    ingreso = input('Desea agregar un disco a su biblioteca? si/no: ')
    if ingreso == 'si':
        artist_name = input('Ingrese el nombre del artista o banda: ')
        album_title = input('Ingrese el nombre del album: ')
        ft = input('Conoce la cantidad de canciones que posee el disco? si/no: ')
        if ft == 'si':
            tracks = int(input('Ingrese la cantidad de canciones que hay en el disco: '))
        else:
            tracks = None
        disco = hacer_album(artist_name.title(),album_title.title(),tracks)
        biblioteca_de_discos = disco
        print(f"\n{biblioteca_de_discos}\n")
    else:
        flag = False
        print('---Fin del programa---')            
"""
# Ejercicio 8.9 MENSAJES: Haga una lista con una serie de mensajes de 
# texto cortos. Paselo a una funcion llamada mostrar_mensajes() que 
# imprima cada mensaje.
    
mensajes_cortos = ['hola capo', 'buen dia', 'buenas noches', 'hasta mañana']

def mostrar_mensajes(mensajes_cortos):
    """Muestra mensajes de texto cortos"""
    for mensaje in mensajes_cortos:
        print(mensaje.capitalize())

print("\n\tEjercicio 8.9 MENSAJES: \n")
mostrar_mensajes(mensajes_cortos)

# Ejercicio 8.10 ENVIAR MENSAJES: Empiece con una copia del programa 
# del ejercicio 8.9. Escriba una funcion llamada enviar_mensajes() que
# imprima cada mensaje de texto y lo mueva a una nueva lista denominada 
# mensajes_enviados a medida que imprime. Despues de llamar a la funcion,
# imprima ambas listas para asegurarse de que los mensajes se han movido 
# correctamente.

mensajes_cortos = ['hola capo', 'buen dia', 'buenas noches', 'hasta mañana']
mensajes_enviados = []
def enviar_mensajes(mensajes_cortos,mensajes_enviados):
    """Imprime cada mensaje y lo mueve a una nueva lista"""
    while mensajes_cortos:
        mensaje = mensajes_cortos.pop()
        mensajes_enviados.append(mensaje)
    
print("\n\tEjercicio 8.10 ENVIAR MENSAJES: \n")
enviar_mensajes(mensajes_cortos,mensajes_enviados)

print(f"Lista de mensajes: {mensajes_cortos}")
print(f"Lista de mensajes enviados: {mensajes_enviados}")
    
    
# Ejercicio 8.11 MENSAJES ARCHIVADOS: Empiece con su trabajo para el 
# ejercicio 8.10. Llame a la funcion enviar_mensajes() con una copia 
# de la lista de mensajes. Después, imprima ambas listas para confirmar 
# que la lista original conserva sus mensajes

print("\t\nEjercicio 8.11\n")

mensajes_cortos = ['hola capo', 'buen dia', 'buenas noches', 'hasta mañana']
mensajes_enviados = []

enviar_mensajes(mensajes_cortos[:],mensajes_enviados)

print(f"Lista de mensajes: {mensajes_cortos}")
print(f"Lista de mensajes enviados: {mensajes_enviados}")

# Ejercicio 8.12 SANGUCHE: Escriba una funcion que acepte una lista
# de elementos que quiere una persona para un sandwich. La función
# deberia tener un parámetro que recoja todos los argumentos que le
# dé la llamada e imprimir un resumen del sandwich que está pidiendo.
# Llame a la función tres veces, usando un número distinto de argumentos.
print("\n\t-----Ejercicio 8.12-----")
def hacer_sanguche(*ingredientes):
    """Imprime resumen de sanguche que prepara"""
    print("\nSale sanguche con:")
    for ingrediente in ingredientes:
        print(f"-{ingrediente.title()}")
        
hacer_sanguche('jamon', 'queso', 'mayonesa')
hacer_sanguche('milanesa')
hacer_sanguche('lomito', 'mostaza', 'lechuga', 'tomate', 'huevo')

# Ejercicio 8.13 PERFIL DE USUARIO: Empiece con una copia de user_profile.py
# Haga un perfil suyo llamando a build_profile(), usando su nombre y apellido
# y otros tres pares clave-valor que le describan
print("\n\t-----Ejercicio 8.13-----")
def build_profile(nombre, apellido, **kwargs):
    """Crea un diccionario con todos sus datos de usuario"""
    kwargs['Nombre'] = nombre.title()
    kwargs['Apellido'] = apellido.title()
    return kwargs

perfil_1 = build_profile('joaquin', 'de souza', 
                         age=32, 
                         ocupacion='operador',
                         lenguaje='Python')

print(perfil_1)

# Ejercicio  8.14 COCHE: Escriba una función que guarde información
# sobre un coche en un diccionario. Deberiía recibir siempre un fabricante
# y un nombre de modelo y aceptar después un número arbitrario de argumentos
# de palabra clave. Llame a la función con la informaci´n requerida
# y otros dos pares nombre-valor, como un color o una prestación opcional.
# Su función debería funcionar parauna llamada como esta:
#       car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Imprima el diccionario devuelto y asegúrese de que se ha almacenado bien
#toda la informacion


def info_auto(marca, modelo, **kwargs):
    kwargs['marca'] = marca
    kwargs['modelo'] = modelo
    return kwargs
auto = info_auto('fiat', 'punto', motor=1.4, puertas=5, gnc=False,
                 deudas=True, chasis='impecable')
print("\n\t-----Ejercicio 8.14-----")
print(auto)

auto = info_auto('subaru', 'outback', color='blue', tow_package=True)
print("\n\t-----Ejercicio 8.14-----")
print(auto)

# Ejercicio 8.15 Ponga todas las funciones del ejemplo printting_models.py
#en un archivo aparte llamado printing_functions.py Escriba una sentencia
#import en la parte superior de printing_models.py y modifique el
# archivo para usar las funciones importadas

# Ejercicio 8.16 IMPORTACIONES: Use un programa que haya escrito que contenga 
# una funcion y guarde esa funcion en un archivo aparte. Importe la funcion
# al archivo de programa principal y llamela con cada una de estas tecnicas.

    """
    import nombre_modulo
    form nombre_modulo import nombre funcion
    from nombre_modulo import nombre_funcion as nf
    import nombre_modulo as nm
    form nombre_modulo import *
    """
    
    