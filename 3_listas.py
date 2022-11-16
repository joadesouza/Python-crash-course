# EJERCICIO 3-1 Nombres
 
amigos = ["sad", "di", "ted", "menem", "borja"]
"""
print(amigos[0])
print(amigos[1])
print(amigos[2])
print(amigos[3])
print(amigos[4]) 
"""

#Ejercicio 3-2 Saludos
"""
print(f"Hola perri {amigos[0]}, llegaste!")
print(f"Mira quien aparecio, {amigos[1]}")
print(f"Abran las cervezas, llego {amigos[2]}")
print(f"ssshhh, que ya esta aca {amigos[3]}")
print(f"cerrando la boca {amigos[4]}") 
"""

#EJERCICIO 3-3 Su propia lista
"""
transporte = ["auto", "moto","bici"]
print(f"Ya me canse de andar en {transporte[0]}, no veo la hora de poder comprarme una {transporte[2]} para ir al laburo o en su defecto una {transporte[1]}")
"""

#EJERCICIO 3-4 Lista de Invitados
"""invitados = ["pino", "nico", "seba"]
print(f"hola {invitados[0].title()}, te invito a cenar")
print(f"Hola manito {invitados[1].title()}, vamos a comer con {invitados[0].title()}")
print(f"heyyy {invitados[2].title()}, estamos yendo a cenar con {invitados[0].title()} y {invitados[1].title()}... te prendes?")
print()"""
#EJERCICIO 3-5 Cambios
"""print()
print(f"Al final {invitados[1].title()} no puede venir, vamos a llamar a Facu")
invitados[1] = "facu"
print()
print(f"hola {invitados[0].title()}, te invito a cenar")
print(f"Hola manito {invitados[1].title()}, vamos a comer con {invitados[0].title()}")
print(f"heyyy {invitados[2].title()}, estamos yendo a cenar con {invitados[0].title()} y {invitados[1].title()}... te prendes?")"""

#EJERCICIO 3-6 Se suman mas
"""
print("Vamos a meter mas en la mesa")
print()
invitados.insert(0, "menem")
invitados.insert(2, "sad")
invitados.append("di")

print(invitados)
"""
#EJERCICIO 3-7 Reduccion
"""
print("\t Lamentablemente solo entran 2 muchachos\n")
borrado = invitados.pop(2)
print(f"Perdon manito, pero {borrado} no va a poder entrar")
borrado = invitados.pop()
print(f"Perdon manito, pero {borrado} no va a poder entrar")
borrado = invitados.pop(1)
print(f"Perdon manito, pero {borrado} no va a poder entrar")
borrado = invitados.pop(0)
print(f"Perdon manito, pero {borrado} no va a poder entrar\n")

print(invitados)
"""

#EJERCICIO 3-8 Ver el Mundo
"""
places = ["machu pichu", "cataratas", "perito moreno", "niza", "new york"]
print("\n Esta es la lista original: ")
print(places)
print("\n Esta es la lista ordenada: ")
print(sorted(places))
print("\n De nuevo la lista original, pa chequear nomas:")
print(places)
print("\n Esta es la lista ordenada con sorted pero en reversa")
print(sorted(places, reverse=True))
print("\n Otra vez la lista original: ")
print(places)
places.reverse()
print("\n Lista cambiada con 'reverse'")
print(places)
print("\n La volvemos a la original otra vez con 'reverse': ")
places.reverse()
print(places)
print("\n Ahora la ordenamos en orden alfabetico con SORT: ")
places.sort()
print(places)
print("\n De nuevo usamos sort y cambiamos para guardarla en orden inverso: ")
places.sort(reverse=True)
print(places)
"""

#EJERCICIO 3-9 Invitados Cena

"""cantidad_invitados = len(invitados)
print(f"La cantidad de invitados es: {cantidad_invitados}")
"""
#EJERCICIO 3-10 Todas las funciones

lista_bandas = ["U2", "Coldplay", "Bon Jovi", "Aerosmith", "Guns n' Roses", "Nirvana", "Linkin Park"]

print(lista_bandas)
print(f"La proxima banda que ire a ver sera la de los {lista_bandas[4]}")
print()
print(f"La banda {lista_bandas[5]} ya no existe mas, en su lugar seguira Foo Figthers")
lista_bandas[5]="Foo Fighters"
print(lista_bandas)
print()

print(f"Agregare a la lista las bandas nacionales como Caballeros de la Quema y Calamaro")
lista_bandas.append("Calamaro")
lista_bandas.append("Caballeros de la Quema") 
print(lista_bandas)
print()

print(f"Lamentablemente nunca podre ver a {lista_bandas[6]} por la muerte de Chester asi que sera eliminada")
del lista_bandas[6]
print()

popped_banda = lista_bandas.pop(0)
print(f"dudo mucho que {popped_banda} toque nuevamente en Argentina, tendre que eliminarla")
print(lista_bandas)
print()

print(f"Vamos a ordenar un poco los nombres de las bandas en orden alfabetico")
lista_bandas.sort()
print(lista_bandas)
print(f"sino podemos ponerla en orden inverso")
lista_bandas.sort(reverse=True)
print(lista_bandas)
print()

print(f"La cantidad de bandas que quiero o fui a ver sera al final de {len(lista_bandas)}")