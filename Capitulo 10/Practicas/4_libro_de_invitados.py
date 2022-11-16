# Escriba un bucle while que pida a los usuarios su nombre. Cuando lo 
# introduzcan, imprima un saludo en la pantalla y añada una linea registrando 
# su visita en un archivo llamado libro_invitados.txt
# Asegurese de que cada entrada apareec en una nueva linea del archivo.

flag = True

with open('practicas/libro_invitados.txt', 'w') as file_object:
    while flag:
        invitado = input("Ingrese su nombre y apellido para firmar el"
                         " libro de invitados o escriba exit para finalizar: ")
        if invitado.lower() == 'exit':
            print("\n --- PROGRAMA FINALIZADO ---\n")
            flag = False
        else:
            print(f"Hola {invitado.title()}!! Ahora te anoto ;)")
            file_object.write(f"{invitado.title()}\n")
    