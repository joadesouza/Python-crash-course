# from ciudad_funciones import ciudad_funciones

print("ingrese q para terminar en cualquier momento")
while True:
    ciudad = input("Ingrese la ciudad: ")
    if ciudad == 'q':
        print("\n---PROGRAMA FINALIZADO---\n")
        break
    else:
        pais = input("Ingrese el pais: ")
        if ciudad == 'q':
            print("\n---PROGRAMA FINALIZADO---\n")
            break
        else:
            habitantes = input('Ingrese cantidad de habitantes: ')
            if habitantes == 'q' :
                print("\n---PROGRAMA FINALIZADO---\n")
                break
            else:
                ubicacion = f"{ciudad}, {pais} - {habitantes} Habitantes."
                print(ubicacion.title())