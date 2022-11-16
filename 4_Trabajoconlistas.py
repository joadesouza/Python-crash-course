
"""
magicians = ["David Copperfield", "Mago Sin Dientes", "Black"]
for magician in magicians:
    print(f"{magician.title()}, ese fue un trucazo maistro!!")
    print(f"No puedo esperar a ver el proximo truco, {magician.title()}\n")
print(f"Gracias a todos, fue un show zarpado")
"""

#EJERCICIO 4-1 Pizzas!

"""pizzas = ["muzza", "napo", "calabresa", "fugazzetta"]
for pizza in pizzas:
    print(f"Como me encanta la {pizza} culiaaao")
print(f"amor eterno a la pizza!")"""

#EJERCICIO 4-2 Animales
"""animales = ["perro", "gato", "hamster", "conejo"]
for animal in animales:
    print(f"Un buen compañero en casa puede ser un {animal}\n")
print(f"Cualquiera de estos animales puede ser un gran compañero en el hogar\n")
print(f"Todos ellos tienen en comun ser muy dociles")
"""

# RANGE()
"""
for value in range(1,6):
    print(value) #Imprime del 1 al 5 excluyendo el 6
print()
for value in range(6):
    print(value) #imprime del 0 al 5 excluyendo al 6

"""

# LIST()

"""numbers = list(range(1, 6))
print(numbers) #imprime la lista numbers [1,2,3...5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)
"""
"""
squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)

print(squares)
# Arranca con lista vacia, recorre el rango desde 1 al 10 y a cada valor lo multiplica exponencialmente ** en 2
# para asi guardar el resultado en la variable square, luego agregarlo a la lista con append

squares = []
for value in range (1, 11):
    squares.append(value ** 2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

print()
print()

squares = [value**2 for value in range(1, 11)]
print(squares)

"""

#EJERCICIO 4-3 Contar hasta 20

"""for value in range(1, 21):
    print(value)
"""
#EJERCICIO 4-4 Millon

print(f"Aca metemos una lista de millon papuuuu")
"""millon = list(range(1, 1000001))

for value in millon:
    print(value)
    print( "-----")
    """
#EJERCICIO 4-5 Sumar millon
"""print(min(millon))
print(max(millon))
print(sum(millon))
"""
#EJERCICIO 4-6 Impares

print(f"\n Aca metemos numeros impares putin \n")
"""for value in range(1, 21, 2):
    print(f"{value}\n")
"""
#EJERCICIO 4-7 tresessss
"""print(f"Estos son los numeros divisibles por 3 hasta el 30: ")
treses = [value * 3 for value in range(1, 11)]
print(treses)
print()"""

#EJERCICIO 4- 8/9 CUBITO
"""print(f"Estos son los primeros 10 cubos en lista: ")
cubito = [value ** 3 for value in range(1, 11)]
print(cubito)

print(f"Y estos son los mismos pero uno por uno, je")
for value in range(1, 11):
    cubi = value **3
    print(cubi)
"""

#EJERCICIO 4-10 TROZOS

my_foods = ['pizza', 'asado', 'milanesas', 'hamburguesas', 'panchito', 'matambre', 'lomito']
friend_foods = my_foods[:]
my_foods.append('bondiolita')
friend_foods.append('tarta lituana')

print(f'mis comidas favoritas son: \n{my_foods}\n')
print(f'las comidas favoritas de mi amigo son: \n{friend_foods}\n')

print(f'\nEstos son los tres primeros elementos de la lista:\n{my_foods[:3]}\n')
print(f'Estos tres elementos estan en el medio de la lista:\n{my_foods[3:5]}\n')
print(f'Estos son los tres ultimos elementos de la lista: \n{my_foods[-3:]}\n')

#EJERCICIO 4- 11 PIIZZASSS
"""
pizzafav = ['muzza', 'napo', 'doble muzza', 'pepperoni', 'fugazzeta']
for pizza in pizzafav:
    print(f'Me encanta la pizza de {pizza}')
print('\nDiosss como me encanta la pizzaaaa')

pizzamigo = pizzafav[:]
pizzafav.append('caprese')
pizzamigo.append('rucula')

print(f'\nMis Pizzas favoritas son:')
for pizza in pizzafav:
    print(pizza)

print(f'\nLas zapis de mi amigo son:')
for pizza in pizzamigo:
    print(pizza)
"""

#EJERCICIO 4 - 12 BUCLES EVERYWHERE
"""
my_foods = ['pizza', 'asado', 'milanesas', 'hamburguesas', 'panchito', 'matambre', 'lomito']
pizzafav = ['muzza', 'napo', 'doble muzza', 'pepperoni', 'fugazzeta']

print('Mis comidas favoritas son: \n')
for food in my_foods:
    print(food)

print('\nMis pizzas favoritas son:\n')
for pizza in pizzafav:
    print(pizza)
"""

#EJERCICIO 4 -13 Bufé

bufe_food = ('milanga', 'asado', 'peje', 'albondigas con pure', 'tallarines')
print('El restaurante ofrece este menu a sus comenzales: ')
for food in bufe_food:
    print(food)

print('\nEl nuevo menu del restaurante locoo:')
bufe_food = ('milanga', 'tarta lituana', 'peje', 'salchichas con pure', 'tallarines')
for food in bufe_food:
    print(food)