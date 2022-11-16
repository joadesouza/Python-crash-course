"""De este modo creamos un archivo de texto"""

filename = 'Libro/programming.txt'

with open(filename, 'w') as file_object: #El primer argumento es el archivo 
                                        # que queremos abrir, el segundo 
                                        # 'w' le indica a python que queremos 
                                        # abrirlo en modo escritura (write). 
                                        # Se puede abrir en modo lectura('r'), 
                                        # escritura ('w'), anexo ('a') o 
                                        # lectoescritura ('r+')
    
    file_object.write ("I love programming.") # Usamos el metodo write() con el 
                                              # objeto del archivo para escribir 
                                              # una cadena en el archivo
    file_object.write("I love creating new games.")
    # Incluir lineas nuevas en nuestras llamadas a write() hace que cada cadena 
    # aparezca en su propia linea, para separarlas debemos hacer uso de \n
    
filename = 'Libro/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("\nTambien amo encontrar significados en grandes conjuntos de datos\n")
    file_object.write("Amo crear aplicaciones que pueden correr en un navegador\n")