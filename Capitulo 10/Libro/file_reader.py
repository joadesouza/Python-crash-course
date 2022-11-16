"""De este modo leeremos todo el archivo"""

# with open('libro/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

""" Asi leeremos linea por linea, por si necesitamos buscar algo o editar el texto"""

# filename = 'libro/pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line) #si queremos eliminar ese caracter vacio que sale debemos 
                    # agregar la extension .rstrip() a line para que
                    # quede asi "print(line.rstrip())"
    
"""De este modo trabajaremos cada linea de texto como valores de una lista"""
                    
# filename = 'libro/pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines() #El metodo readlines() recoge cada linea y la asigna a una lista (lines)
#                                     #Que puede seguir funcionando despues que termine el bloque with
    
# for line in lines: #Usamos for para imprimir cada linea de la lista "lines"
#     print(line.strip())
    
    
    