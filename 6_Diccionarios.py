from re import S
from tkinter import Place


print("####################################")
print("##### EJERCICIO 6.1    PERSONA #####")
print("####################################\n")

print('Usar un diccionario para guardar informacion de una'
    'persona que conozca\n')

persona = {
    'nombre' : 'maria lourdes',
    'apellido' : 'colombo',
    'edad' : 30,
    'cumpleaños' : '25 de septiembre',
    'mascota' : 'gato',
}

print(persona)

print("\n####################################")
print("##### EJERCICIO 6.2   NUMEROS  #####")
print("####################################\n")

print('Use un diccionario para almacenar los numeros favoritos de '
    'diferentes personas, piense al menos 5 personas\n')

num_fav = {
    'chita' : 7,
    'menem' : 13,
    'di' : 6,
    'sad' : 12,
    'ted' : 0,
    'borja' : 'd'
}

print(f"El numero favorito de Chita es {num_fav['chita']}")
print(f"El numero favorito de Ted es {num_fav['ted']}")
print(f"El numero favorito de Menem es {num_fav['menem']}")
print(f"El numero favorito de Sad es {num_fav['sad']}")
print(f"El numero favorito de Borja es {num_fav['borja']}")
print(f"El numero favorito de Di es {num_fav['di']}")

print("\n####################################")
print("##### EJERCICIO 6.3  GLOSARIO  #####")
print("####################################\n")

glosario = {
    'python' : 'Es un lenguaje de programacion de tipado rapido y '
            'lectura sencilla',
    'if' : 'se utiliza para evaluar una expresion condicional y asi'
            'determinar el flujo del programa en funcion de esa evaluacion',
    'diccionario' : 'Se utilizan para almacenar dos conjuntos de elementos,'
            'es decir dos datos entrelazados (clave y valor)',
    'listas' : 'Las listas son una estructura de datos formadas por una '
            'secuencia de objetos',
    'tuplas' : 'las tuplas son una estructura de datos, al igual que las '
            'listas, pero que no pueden ser modificadas',
    'cadenas' : 'una cadena es una seria de caracteres. cualquier cosa que'
            'haya que leer entre comillas se considera una cadena en Python',
    'variables' : 'las variables son "etiquetas" que permiten hacer referencia'
            'a los datos (que se guardan en unas "cajas" llamadas objetos).',
    'comentarios' : 'sirven para explicar a las personas que puedan leer nuestro'
            'codigo en el futuro que es lo que hace el programa y explicar algunas '
            'partes del codigo'
}

print(f"Con ustedes lo que es Python: \n\t{glosario['python'].capitalize()}")
print(f"Con ustedes lo que son las Listas: \n\t{glosario['listas'].capitalize()}")
print(f"Con ustedes lo que son las Tuplas: \n\t{glosario['tuplas'].capitalize()}")
print(f"Con ustedes lo que es la sentencia IF: \n\t{glosario['if'].capitalize()}")
print(f"Con ustedes lo que es un diccionario: \n\t{glosario['diccionario'].capitalize()}")

print("\n####################################")
print("##### EJERCICIO 6.3 GLOSARIO.2 #####")
print("####################################\n")

# Limpiar el codigo del ejercicio 6.3 sustituyendo las llamadas print por un 
# bucle que pase por las claves y valores del diccionario

for glos, defi in glosario.items():
    print(f"La definicion de {glos.title()}: \n\t{defi.capitalize()}")
    

print("\n####################################")
print("#####   EJERCICIO 6.4   RIOS   #####")
print("####################################\n")

# Haga un diccionario con tres rios importantes y al pais por el que discurre cada uno. 
# Un par clave-valor podria ser 'nilo':'egipto'
# - Use un bucle para imprimir una frase sobre cada rio
# - Use un bucle para imprimir el nombre de cada rio incluido en el diccionario
# - Use un bucle para imprimir el nombre de cada pais incluido en el diccionario

rios = {
    'rio de la plata' : 'buenos aires',
    'rio cuarto' : 'cordoba',
    'pilcomayo' : 'salta',
}

for rio, prov in rios.items():
    print(f"El {rio.capitalize()} pasa por la provincia de {prov.title()}")


print(f"\nLos rios incluidos en el listado son:")
for rio in rios.keys():
    print(rio.title())
    
print(f"\nLas provincias por donde pasan estos rios son: ")
for prov in rios.values():
    print(prov.title())
    
print("\n####################################")
print("#####  EJERCICIO 6.6  Sondeos  #####")
print("####################################\n")

# Use el codigo de favorite_languages.py
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'java',
    'phil' : 'python',
}
#   - Haga una lista de personas que deberian hacer la encuesta sobre lenguajes 
# preferidos. Incluya algunos nombres que esten ya en el diccionario y otros que 
# no lo esten
#   - Pase en bucle por la lista de personas que deberian hacer la encuesta. 
# Si ya la han hecho, deles las gracias por responder. Si todavia no lo han completado, 
# imprima un mensaje invitandolas a hacerlo

personas_nuevas = ('lourdes', 'chimi','sarah', 'tom', 'lula', 'phil')

for persona in personas_nuevas:
    if persona in favorite_languages.keys():
        print(f"Che {persona.title()}, vos ya hiciste la encuesta... dejalo para otro !")
    else:
        print(f"Hola {persona.title()}, te invito a realizar la siguiente encuesta. Te prendes? :)")
        
print("\n####################################")
print("#####  EJERCICIO 6.7 PERSONAS  #####")
print("####################################\n")

# # Empiece con el programa que ha escrito en el ejercicio 6.1
# Haga 2 diccionarios nuevos que representen distintas personas 
# y guarde los 3 diccionarios en una lista llamada personas.
# Pase en bucle la lista y al hacerlo imprima todo lo que sabe de esas personas

persona1 = {
    'nombre' : 'maria lourdes',
    'apellido' : 'colombo',
    'edad' : 30,
    'cumpleaños' : '25 de septiembre',
    'mascota' : 'gato',
}

persona2 = {
    'nombre' : 'anita',
    'apellido' : 'benitez',
    'edad' : 30,
    'cumpleaños' : '16 de octubre',
    'mascota' : 'perro',
}

persona3 = {
    'nombre' : 'juan bautista',
    'apellido' : 'ricci',
    'edad' : 21,
    'cumpleaños' : '2 de noviembre',
    'mascota' : 'perra',
}

personas = (persona1, persona2, persona3)
n = 1

for persona in personas:  
    print(f"\nEstos son los datos de la Persona {n}:")
    n += 1
    for dato, valor in persona.items():
        datolo = f"{dato}: {valor}"
        print(datolo.title())

print("\n####################################")
print("#####  EJERCICIO 6.7 MASCOTAS  #####")
print("####################################\n")

# Haga varios diccionarios, cada uno representando una mascota diferente.
# En cada diccionario incluya el tipo de animal y el nombre del dueño
# Guarde estos diccionarios en una lista llamada mascotas
# A continuacion pase en bucle por la lista e imprima todo lo que sabe sobre 
# las mascotas

mascota1 = {
    'tipo de animal' : 'gato',
    'raza' : 'negro',
    'nombre' : 'chimi',
    'edad' : 3,
    'dueño' : 'joaquin',
}

mascota2 = {
    'tipo de animal' : 'gato',
    'raza' : 'siames',
    'nombre' : 'moni',
    'edad' : 7,
    'dueño' : 'lourdes',
}

mascota3 = {
    'tipo de animal' : 'perro',
    'raza' : 'labrador',
    'nombre' : 'mora',
    'edad' : 4,
    'dueño' : 'sofia',
}

mascota4 = {
    'tipo de animal' : 'gato',
    'raza' : 'gris',
    'nombre' : 'tom',
    'edad' : 5,
    'dueño' : 'pedro',
}

mascota5 = {
    'tipo de animal' : 'perro',
    'raza' : 'ovejero aleman',
    'nombre' : 'milo',
    'edad' : 7,
    'dueño' : 'joaquin',
}

mascotas = (mascota1, mascota2, mascota3, mascota4, mascota5)
n = 1

for mascota in mascotas:
    print(f"\nEstos son los datos de la mascota N° {n}:")
    n += 1
    for dato, valor in mascota.items():
        datolo = f"{dato}: {valor}"
        print(datolo.title())
        
print("###########################################")
print("##### EJERCICIO 6.9 LUGARES FAVORITOS #####")
print("###########################################\n")

# Haga un diccionario que se llame lugares_faovritos, piense en 3 nombres
# para usar como claves en el diccionario y guarde entre uno y tres lugares
# favoritos para cada persona.
# Para haceer este ejercicio un poco mas interesante, pregunte a algunos 
# amigos por sus sitios preferidos
# Pase en bucle e imprima el nombre y el lugar favorito de cada persona

favorite_places = {
    'sofia' : ['usa'],
    'lourdes' : ['egipto', 'bariloche', 'maldivas'],
    'joaquin' : ['machu pichu', 'japon'],
    'pedro' : ['brasil', 'japon', 'usa'],
}

for name, country in favorite_places.items(): 
    if len(country) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in country:
            print(f"\t\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is:")
        for place in country:
            print(f"\t\t{place.title()}")
            
print("\n##############################################")
print("#####  EJERCICIO 6.10 NUMEROS FAVORITOS  #####")
print("##############################################\n")

# Modifique el programa del ejercicio 6.2 para que cada persona pueda 
# tener mas de un numero favorito.
# Imprima nombre de cada persona junto a sus numeros favoritos

num_fav = {
    'chita' : [7, 20, 26],
    'menem' : [13, 15, 27, 60],
    'di' : [6],
    'sad' : [12, 9, 18],
    'ted' : [0, 1],
    'borja' : [666],
}

for name, numbers in num_fav.items():
    if len(numbers) > 1:
        print(f"\nLos numeros favoritos de {name.title()} son:")
        for number in numbers:
            print(number)
    else:
        print(f"\nEl numero favorito de {name.title()} es:")
        print(number)
        
print("\n#####################################")
print("#####  EJERCICIO 6.11 CIUDADES  #####")
print("#####################################\n")

# Haga un diccionario llamado ciudades. Use los nombres de 3 ciudades como 
# claves en su diccionario

# Cree un diccionario de informacion sobre esas ciudades e incluya el pais 
# en el que se encuentra y su poblacion aproximada y alguna curiosidad 
# sobre la ciudad.

# Las claves para cada ciudad serian pais, poblacion y curiosidad. Imprima 
# el nombre de cada ciudad y toda la informacion que tenga guardada sobre ella.

cities = {
    'boston' : {
        'country' : 'USA',
        'population' : '689.326 habs.',
        'curiosity' : "The Public Library of Boston was the first in the United"
        "States of America of being public, in 1948, and in this one, You could" 
        "enter free of charge"
    },
    'osaka' : {
        'country': 'japan',
        'population' : '2.691.000 habs.',
        'curiosity' : "Osaka has also been known as the 'nation’s kitchen' and" 
        "has served as a center for the rice trade during the Edo period. These" 
        "days, it refers to its reputation as a gourmand’s paradise and "
        "okonomiyaki is Osaka’s most famous dish."
    },
    'cali' : {
        'country' : 'colombia',
        'population' : '2.200.000 habs.',
        'curiosity' : "Cali is distinguished in Colombia as the 'Rumba's capital'" 
        "and, in the world as 'Salsa's capital', that's because the street party "
        "and dance are caracteristics of the city."
    }
}

for city, val in cities.items():
    print(f"\nCity of {city.title()}:")
    for key, va in val.items():
        datolo = f"{key.title()}: {va.capitalize()}"
        print(f"\t{datolo}")
        
print("\n########################################")
print("#####  EJERCICIO 6.12 EXTENSIONES  #####")
print("########################################\n")

# Ahora estamos trabajando con ejemplos lo bastante complejos como para poder 
# extenderse de distintas maneras. 
# Elija uno de los programas de ejemplo de este capitulo y amplielo añadiendo 
# claves y valores nuevos, cambiando el contexto del programa o mejorando el 
# formato de la salida