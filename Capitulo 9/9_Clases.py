# Ejercicio 9.1 RESTAURANTE: Haga una clase llamada Restaurante. El metodo
# __init__() para Restaurante deberia albergar dos atributos_ nombre_restaurante
# y tipo_cocina. Cree un método llamado describir_restaurante() que imprima
# estos dos datos, y un metodo llamado abrir_restaurante que imprima el mensaje
# indicando que el restaurante está abierto.
# Haga una instancia llamada restaurante a partir de su clase. Imprima las dos
# atributos por separado y luego llame a ambos métodos



class Restaurante:
    """Creacion de un restaurante"""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre del resto y tipo de cocina"""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        """describe el restaurante"""
        print(f"Este restaurante se llama {self.nombre_restaurante.title()}")
        print(
            f"{self.nombre_restaurante.title()} realiza platos del tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Imprime mensaje avisando que esta abierto el restaurante"""
        print(
            f"Atencion! {self.nombre_restaurante.title()} ya abrio sus puertas!")


"""
restaurant = Restaurante('la mini', 'pizza')
print(f"El nombre del restaurante es {restaurant.nombre_restaurante.capitalize()}")
print(f"{restaurant.nombre_restaurante.capitalize()} tiene como especialidad hacer {restaurant.tipo_cocina}")

restaurant.abrir_restaurante()
restaurant.describir_restaurante()

"""
# Ejercicio 9.2 TRES RESTAURANTES: Empiece con la clase del ejercicio 9.1. Cree tres instancias diferentes a partir de ella y llame a describir_restaurante() para cada instancia

primer_resto = Restaurante('La mini', 'pizza')
segundo_resto = Restaurante('hamburgo', 'hamburguesas')
tercer_resto = Restaurante('El rey del calzone', 'comida italiana')

print(
    f"Este lugar de comida se llama {primer_resto.nombre_restaurante.capitalize()}")
print(f"{primer_resto.nombre_restaurante.capitalize()} tiene como platos principales {primer_resto.tipo_cocina}")
primer_resto.abrir_restaurante()

print("---------------")

print(f"Acá tenemos a {segundo_resto.nombre_restaurante.capitalize()}")
print(f"{segundo_resto.nombre_restaurante.capitalize()} prepara unas {segundo_resto.tipo_cocina}")
segundo_resto.abrir_restaurante()

print("---------------")

tercer_resto.describir_restaurante()
tercer_resto.abrir_restaurante()
print("\n----Fin del Programa----\n")

# Ejercicio 9.3 USUARIOS: Cree una clase llamada Usuario. Cree dos atributos llamados nombre y apellido y otros que suelan quedarse en un perfil de usuario. Haga un metodo llamado describir_usuario() que imprima un resumen de la informacion del usuario. Haga otro método llamado saludar_usuario() que imprima un saludo.
# Cree varias instancias que representen a distintos usuarios y llame a ambos métodos para cada usuario

"""
class Usuario:
    """"Creara usuario con nombre y apellido""""
    def __init__(self, nombre, apellido, username, ubicacion):
        """"Inicializa los atributos de nombre y apellido""""
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.ubicacion = ubicacion
    
    def describir_usuario(self):
        """"Describe al usuario por nombre y apellido""""
        nombre_completo = f"{self.nombre} {self.apellido}"
        print(f"El nombre real del usuario {self.username} es {nombre_completo.title()} y se registro desde {self.ubicacion}")
    
    def saludar_usuario(self):
        """"Saluda al usuario""""
        print(f"Hola {self.nombre.title()}!! :D")

question = input("Desea agregar 1 nuevo usuario? si/no: ")
if question == 'si': 
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    ubicacion = input("Pais: ")
    username = input("Ingrese su nombre de usuario: ")        
    usuario_uno = Usuario(nombre, apellido, username, ubicacion)
    usuario_uno.describir_usuario()
    usuario_uno.saludar_usuario()
    question = input("Desea agregar un segundo nuevo usuario? si/no: ")
    if question == 'si':
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        ubicacion = input("Pais: ")
        username = input("Ingrese su nombre de usuario: ")

        usuario_dos = Usuario(nombre, apellido, username, ubicacion)
        usuario_dos.describir_usuario()
        usuario_dos.saludar_usuario()
    else:
        print("\n---Programa finalizado---\n")
else:
    print("\n---Programa finalizado---\n")
"""
# Ejercicio 9.4 NUMERO SERVIDO: Empiece con el programa del ejercicio 9.1.

# ><-Añada un atributo llamado numero_servido con un valor predeterminado
# de 0.

# ><-Cree una instancia llamada restaurante a partir de esta clase.

# ><-Imprima el numero de clientes a los que ha servido el restaurante,
# cambie ese valor y vuelva a imprimirlo.

# ><-Añada un metodo llamado establecer_numero_servido() que le permita configurar
# el numero de clientes a los que se ha servido. Llamelo con un numero nuevo y
# vuelva a imprimir el valor.

# ><-Añada un metodo llamado incrementar_numero_servido() que le permita
# incrementar el numero de clientes atendidos. Llamelo con cualquier numero
# que pueda representar a cuantos clientes se ha servido en un dia laborable
# normal.


class Restaurante:
    """Creacion de un restaurante"""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre del resto y tipo de cocina"""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        """describe el restaurante"""
        print(f"Este restaurante se llama {self.nombre_restaurante.title()}")
        print(
            f"{self.nombre_restaurante.title()} realiza platos del tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Imprime mensaje avisando que esta abierto el restaurante"""
        print(
            f"Atencion! {self.nombre_restaurante.title()} ya abrio sus puertas!")

    def establecer_numero_servido(self, actualizacion_servido):
        """Actualiza la cantidad de clientes atendidos"""
        if actualizacion_servido >= 0:
            print("Actualizando numero de clientes atendidos...\n")
            self.numero_servido += actualizacion_servido
            print(
                f"La cantidad de clientes atendidos es de: {self.numero_servido}\n")
        else:
            print(
                f"La cantidad de clientes atendidos sigue siendo {self.numero_servido}\n")

    def incrementar_numero_servido(self, incremento_clientes):
        """Incrementa el numero de clientes atendidos"""
        if incremento_clientes >= 0:
            self.numero_servido += incremento_clientes
            print(f"El numero de clientes atendidos es: {self.numero_servido}")
        else:
            print(
                f"El numero de clientes atendidos sigue siendo: {self.numero_servido}")


restaurante = Restaurante('pedro', 'pizza')
restaurante.describir_restaurante()

print(f"La cantidad de clientes atendidos es: {restaurante.numero_servido}\n")
restaurante.numero_servido = 5
print(f"La cantidad de clientes atendidos es: {restaurante.numero_servido}\n")

restaurante.establecer_numero_servido(20)
restaurante.establecer_numero_servido(-5)

# Ejercicio 9.5 INTENTOS DE INICIO DE SESION:
# ><- Añada un atributo intentos_inicio a la clase usuario del ejercicio 9.3.

# ><- Escriba un metodo llamado incrementar_intentos_inicio() que aumente el
# valor de intentos_inicio en 1.

# ><- Escriba otro metodo llamado restablecer_intentos_inicio() que restablezca
# el valor de intentos_inicio().

# ><- Vuelva a imprimir intentos_inicio para asegurarse de que se ha restablecido a 0
print("\n\tEJERCICIO 9.5\n")


class Usuario:
    """Creara usuario con nombre y apellido"""

    def __init__(self, nombre, apellido, username, ubicacion):
        """Inicializa los atributos de nombre y apellido"""
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.ubicacion = ubicacion
        self.intentos_inicio = 0

    def describir_usuario(self):
        """Describe al usuario por nombre y apellido"""
        nombre_completo = f"{self.nombre} {self.apellido}"
        print(
            f"El nombre real del usuario {self.username} es {nombre_completo.title()} y se registro desde {self.ubicacion}")

    def saludar_usuario(self):
        """Saluda al usuario"""
        print(f"Hola {self.nombre.title()}!! :D")

    def incrementar_intentos_inicio(self, incremento_intentos):
        """Incrementa y muestra los intentos de inicio de sesion"""
        if incremento_intentos >= 0:
            self.intentos_inicio += incremento_intentos
            print(f"Intentos de inicio: {self.intentos_inicio}")

    def restablecer_intentos_inicio(self):
        """Restablece los intentos de inicio a 0"""
        print("Restableciendo los intentos de inicio...")
        self.intentos_inicio = 0


if input("Desea hacer la prueba de este ejercicio? si/no: ") == "si":
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    ubicacion = input("Pais: ")
    username = input("Ingrese su nombre de usuario: ")
    usuario_uno = Usuario(nombre, apellido, username, ubicacion)
    usuario_uno.describir_usuario()
    usuario_uno.saludar_usuario()

    usuario_uno.incrementar_intentos_inicio(1)
    usuario_uno.restablecer_intentos_inicio()

    print(f"Intentos restablecidos a {usuario_uno.intentos_inicio}")

else:
    print("\n\t-----EJERCICIO FINALIZADO-----\n")


# EJERCICIO 9.6 Carrito de Helados:
# Un carrito de helados es, en cierto modo, parecido a un restaurante.
# ><- Escriba una clase llamada CarritoDeHelados que herede de la clase Restaurante
# del ejercicio 9.1 o del 9.4. Servirá cualquiera de las dos versiones, asi que
# coja la que mas le guste.
# ><- Añada un atributo llamado sabores que almacene una
# lista de sabores de helado.
# ><- Cree una instancia de CarritoDeHelados y llame a ese método.
print("\n\tEJERCICIO 9.6\n")


class CarritoDeHelados(Restaurante):
    """Es un carrito de helados con todo lo que tiene el restaurante"""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de la clase Restaurante"""
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ['maracuya', 'dulce de leche',
                        'chocolate', 'tramontana']

    def agregar_sabores(self):
        """Agrega sabores a la lista de sabores"""
        while input("\nDesea añadir un sabor nuevo a la lista? si/no: ") == "si":
            nuevo_sabor = input("\nIngrese el sabor que desea agregar: ")
            if nuevo_sabor in self.sabores:
                print("\nEse sabor ya se encuentra en nuestras filas"
                      "... Por favor, intentelo de nuevo :D")
            else:
                self.sabores.append(nuevo_sabor)
        print(f"\n La lista de sabores fue actualizada con éxito!\n Estos "
              f" son todos los sabores que tenemos: \n {self.sabores}")


if input("Desea realizar el ejercicio 9.6? si/no: ") == "si":
    caballito = CarritoDeHelados('il cavalino', 'helados')

    caballito.describir_restaurante()
    caballito.abrir_restaurante()
    caballito.incrementar_numero_servido(15)
    print(caballito.sabores)
    caballito.agregar_sabores()
else:
    print("\n\t-----EJERCICIO FINALIZADO-----\n")    

# EJERCICIO 9.7 ADMIN:
# Un administrador es un tipo especial de usuario. 

# ><- Escriba una clase llamada Admin que herede de la clase Usuario del 
# ejercicio 9.3 o del 9.5. 

# - Añada un atributo privilegios que acoja una lista de cadenas como 
# "puede añadir comentario", "puede borrar comentario", "puede vetar 
# usuarios", etc. 

# - Escriba un método llamado show_privileges() que enumere el conjunto de 
# privilegios del administrador. 

# - Cree una instancia de Admin y llame al método.

class Admin(Usuario):
    """Esta clase heredara los atributos de la clase usuario del ejercicio 9.5"""
    def __init__(self, nombre, apellido, username, ubicacion):
        "inicializa los atributos de la clase Usuario"
        super().__init__(nombre, apellido, username, ubicacion)
        self.privilegios = ["puede añadir comentario", "puede borrar comentario", 
                            "puede vetar usuarios", "puede culiar travestis"]
        
        
class Privilegios:
    """Clase de los diferentes privilegios del administrador... supongo"""
    def __init__(self, privilegios):
        self.privilegios = []

    def show_privileges(self):
        """Muestra todos los privilegios del administrador"""
        print("\nLos privilegios que tiene el admin son los siguientes: ")
        for privi in self.privilegios:
            print(f"\t- {privi.capitalize()}")
        print()
    
    def add_privileges(self):
        """Agrega nuevos privilegios de admin"""
        question = input("Desea agregar un privilegio al admin? si/no: ")
        while question == "si":    
            self.privilegios.append(input("Ingrese un nuevo privilegio para agregar: "))
            question = input("Desea agregar otro privilegio al admin? si/no: ")

        print("La lista de privilegios fue actualizada")
        for privi in self.privilegios:
            print(privi)
                
    
print("\n\tEJERCICIO 9.7\n")

if input("Desea hacer la prueba de este ejercicio? si/no: ") == "si":
    while input("\nDesea agregar un nuevo admin? si/no: ") == "si":
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        ubicacion = input("Pais: ")
        username = input("Ingrese su nombre de usuario: ")
        
        priv_admin_two = Privilegios(None)
        admin_two = Admin(nombre, apellido, username, ubicacion)
        
        priv_admin_two.add_privileges()
        priv_admin_two.show_privileges()
        
        # admin_one = Admin(nombre, apellido, username, ubicacion)
        # admin_one.describir_usuario()
        # admin_one.saludar_usuario()
        # print()
        # admin_one.incrementar_intentos_inicio(1)
        # admin_one.restablecer_intentos_inicio()
        # print()
        # admin_one.privilegios()
        # print(f"Intentos restablecidos a {admin_one.intentos_inicio}")

    else:
        print("\n\t-----EJERCICIO FINALIZADO-----\n")
else:
    print("\n\t-----EJERCICIO FINALIZADO-----\n")
    
# EJERCICIO 9.8 PRIVILEGIOS:

# ><- Escriba una clase Privilegios aparte. Esta clase deberia tener un atributo, 
# privilegios, que almacene una lista de cadenas como la descrita en el 
# ejercicio anterior. 

# ><- Mueva el método show_privileges() a esta clase. 

# ><- Haga una instancia de Privilegios como atributo de la clase Admin. 

# ><- Cree una nueva instancia de Admin y use su método para mostrar los privilegios.

print("\n\t-----EJERCICIO FINALIZADO 9.8-----\n")


# EJERCICIO 9.9 MEJORA DE BATTERY: 
# >< Use la ultima version de electric_car.py. 

# ><- Añada un metodo a la clase Battery llamado upgrade_battery(). Este metodo deberia 
# comprobar el tamaño de la bateria y establecer la capacidad en 100 si no está ya así. 

# - Haga un coche electrico con un tamaño de bateria predeterminado, llame a get_range() 
# una vez y vuelva a llamarlo para mejorar la bateria. Deberia ver un incremento en la 
# autonomia del coche

print("\n\tEJERCICIO 9.9\n")

if input("Desea hacer la prueba de este ejercicio? si/no: ") == "si":
    import sys
    sys.path.insert(1, 'J:\Python\works\Imported')

    from electric_car import *

    
    my_car = ElectricCar("Fiat", "punto", 2015)
    my_battery = Battery(25)
    print()
    
    print(my_car.get_descriptive_name())
    
    my_battery.describe_battery()
    my_battery.get_range()
    my_battery.upgrade_battery()
    my_battery.get_range()
    
    print("\n\t-----EJERCICIO FINALIZADO 9.8-----\n")
    
    
else:
    print("\n\t-----EJERCICIO FINALIZADO 9.8-----\n")
    
 