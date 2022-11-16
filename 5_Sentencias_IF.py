print('##########################################')
print('## EJERCICIO 5.1  PRUEBAS CONDICIONALES ##')
print('##########################################')
print('\n- Escriba una serie de pruebas condicionales. Imprima una frase')
print('describiendo cada prueba y su prediccion para el resultado')
print('- Examine los resultados y asegurese de comprender por que cada linea se evalua como True o False')
print('- Cree al menos diez pruebas y haga que cinco, como minimo, se evaluen como True y otras cinco como False\n')

caballeros = ['pegaso', 'andromeda', 'cisne', 'dragon']
caballero = 'fenix'
print('estara el caballero de fenix dentro del equipo a esta altura?, yo creo que aun no...')
print(caballero in caballeros)

car = 'subaru' 
print("\nis car == 'subaru'? I predict True")
print(car == 'subaru')

animal = 'simio'
print('Es el animal que está dentro del equipo un primate?')
print(animal == 'simio')

profecia = True
print('\nComo es el estado de la profecia de Atena?')
print(profecia)

print('\nEs el caballero dorado de Acuario el unico que no aparecio todavia?')
print('camus' not in caballeros)

golpes = 58
print('\nGolpeo mas de 70 veces?')
print(golpes >= 70)

print('\nGolpeo menos de 70 veces?')
print(golpes < 70)


edad = 31
print(f'\nSu edad es de {edad}')
print('La edad del caballero ideal esta entre 25 y 31')
print(edad <= 31 and edad >=25)

print('Puede entrar si tiene entre 17 y 25 o entre 32 y 37')
print((edad >= 17 and edad <= 25) or (edad >=32 and edad <= 37))

print('\n#############################################')
print('## EJERCICIO 5.2 MAS PRUEBAS CONDICIONALES ##')
print('#############################################\n')

print('* Pruebas de igualdad y desigualdad con cadenas.')
print('* Pruebas con el metodo lower()')
print('* Pruebas numericas que impliquen igualdad y desigualdad,') 
print('mayor que y menor que, mayor o igual que y menor o igual que')
print('* Pruebas con las palabras clave and y or')
print('* Prueba para comprobar si un elemento esta en una lista')
print('* Prueba para comprobrar si un elemento no esta en una lista')

auto = 'audi'
print('\nEl auto que vimos era un Toyota?')
print(auto == 'toyota')
print('\nEl auto que vimos era un Audi?')
print(auto == 'audi')

fenix = 'Ikki'
print('\nEs el nombre del caballero de fenix, Ikki?')
print(fenix.lower() == 'ikki')

print('\nEs el nombre del caballero de fenix, Seiya?')
print(fenix.lower() == 'seiya')

bananas = 5
manzanas = 8
peras = 2
uvas = 10
sandias = 2

print('Hay tantas peras como sandias?')
print(peras == sandias)
print('Son distintas las cantidades de manzanas y de peras?')
print(manzanas != bananas)
print('hay mas bananas que manzanas?')
print(bananas > manzanas)
print('las sandias son mas que las uvas?')
print(sandias >= uvas)
print('Solo puedes llevar las frutas si las bananas son mas que las sandias y las uvas menos que las manzanas')
print(bananas >= sandias and uvas <= manzanas)
print('Solo pueden pagar las frutas si llevas mas de 8 uvas o 3 sandias')
print(uvas >= 8 or sandias >= 3)

juguetes_chimi = ['laucha roja', 'laucha gris', 'laucha peluda gris', 'laucha peluda marron', 'laucha de hilo', 'laucha gigante']
print('esta la ardilla con los juguetes de chimi?')
print('ardilla' in juguetes_chimi)
print('\nEl erizo vibrante tampoco esta junto a los demas juguetes de chimito')
print('erizo' not in juguetes_chimi)


print('\n#############################################')
print('###### EJERCICIO 5.3 COLORES DE ALIENS ######')
print('#############################################\n')

colour_alien = 'green'

if colour_alien == 'green':
    print('YES!! You have 5 points')

colour_alien = 'yellow'

if colour_alien == 'green':
    print('YES!! You have earned 5 points')

print('\n#############################################')
print('#### EJERCICIO 5.4 COLORES DE ALIENS #2 #####')
print('#############################################\n')

colour_alien = 'red'

if colour_alien =='green':
    print("OK! You've earned 5 points")
else:
    print("YES!! You've earned 10 points!")
    
colour_alien = 'green'

if colour_alien =='green':
    print("OK! You've earned 5 points")
else:
    print("YES!! You've earned 10 points!")
    

print('\n#############################################')
print('#### EJERCICIO 5.5 COLORES DE ALIENS #3 #####')
print('#############################################\n')

colour_alien = 'red'

if colour_alien == 'green':
    print("OK! You've earned 5 points")
elif colour_alien == 'yellow':
    print("Yikes! You've earned 10 points!")
else:
    print("YESS!! You've earned 15 points!")
    
print('\n#######################################')
print('#### EJERCICIO 5.6 ETAPAS VITALES #####')
print('#######################################\n')

edad = 32

if edad < 2:
    print(f'Edad: {edad} años, es un bebé')
elif edad < 4:
    print(f'Edad: {edad} años, es un infante')
elif edad >= 4 and edad < 13:
    print(f'Edad: {edad} años, es un niño')
elif edad >= 13 and edad < 20:
    print(f'Edad: {edad} años, es un adolescente')
elif edad >= 20 and edad < 65:
    print(f'Edad: {edad} años, es un adulto')
elif edad >= 65:
        print(f'Edad: {edad} años, es un anciano')

print('\n#######################################')
print('#### EJERCICIO 5.7 FRUTA FAVORITA #####')
print('#######################################\n')

frutavoritas = ['banana', 'kiwi', 'mandarina', 'pera', 'manzana verde']

if 'manzana' in frutavoritas:
    print('Ah como te gustan las manzanas eh')
if 'banana' in frutavoritas:
    print('Ah como te gustan las bananas eh')
if 'sandia' in frutavoritas:
    print('Ah como te gustan las sandias eh')
if 'pera' in frutavoritas:
    print('Ah como te gustan las peras eh')
if 'manzana verde' in frutavoritas:
    print('Ah como te gustan las manzanas verdes eh')
if 'naranja' in frutavoritas:
    print('Ah como te gustan las naranjas eh')
    
    
print('\n#######################################')
print('#### EJERCICIO 5.8 y 5.9 HOLA ADMIN #####')
print('#######################################\n')

usuarios = ['admin', 'jorge', 'seba', 'migue', 'menem']

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print(f'Hola Admin, quiere ver el estado del sistema?')
        else:
            print(f'Hola {usuario}, bienvenido nuevamente!')
else:
    print('parece que no hay ningun usuario conectado')
    
    
print('\n#######################################')
print('#### EJERCICIO 5.10 COMPROBAR USERS #####')
print('#######################################\n')

current_users = ['menem', 'ted', 'di', 'sad', 'borja', 'chita', 'mitocondria']
new_users = ['mitocondria', 'chita', 'rino', 'pantera', 'tortuga', 'dogc']

for new_user in new_users:
    if new_user in current_users:
        print(f'Vas a tener que ponerte otro nombre capo, {new_user} ya esta en uso')
    else:
        print(f'dale nomas con ese nombre {new_user}')
        
        
print('\n###########################################')
print('#### EJERCICIO 5.11 NUMEROS ORDINALES #####')
print('###########################################\n')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero ==1:
        print(f'{numero}st')
    elif numero ==2:
        print(f'{numero}nd')
    elif numero ==3:
        print(f'{numero}rd')
    elif numero >3:
        print(f'{numero}th')        