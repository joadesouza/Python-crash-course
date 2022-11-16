print('La entrada es gratuita para menores de 4 años')
print('La entrada cuesta 25 dolares para quienes tengan entre 4 y 18 años')
print('La entrada cuesta 50 dolares para mayores de 18 años\n')

age = 89

if age <= 4:
    print('Pasa nomas capo, tenes menos de 4')
elif age > 4 and age <= 18:
    print('Mira campeon, tenes que pagar 25 pe')
elif age <65:
    print('Lo lamento maestro, ya tas viejo y tenes que pagar 50 duros')
elif age >=65:
    print('Abuelo, page 20 y cerramos')