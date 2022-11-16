flag = True
with open('/practicas/lista_invitados.txt', 'w') as file_object:
    while flag:
        invitado = input("ingrese el nombre del invitado o escriba exit para salir: ")
        if invitado == "exit":
            flag = False
            break
        else:
            file_object.write(f"{invitado.title()}\n")
