# Visite Project Gutenberg y elija unos cuantos textos en inglés que le 
# gustaría analizar. 
# Descargue los archivos de esas obras o copie el texto del navegador en 
# un archivo de su ordenador. 
# Puede usar el método count() para descubrir cuantas veces aparece una 
# palabra o grase en una cadena. 
# Por ejemplo, el siguiente codigo cuenta el numero veces que aparece 
# 'row' en una cadena:
"""
line= "Row, row, rock, row your boat"
count = line.count('row')
print(count)
count = line.lower().count('row')
print(count)
"""

# Escriba un programa que lea los archivos que ha sacado de PG y determine
# cuantas veces aparece la palabra 'the' en cada texto. 
# Será una aproximacion, ya que tambien contará palabras como 'then' y 'there'. 
# Pruebe a contar 'the ' con un espacio en la cadena y observe como baja el recuento

filenames = ['archivos/frankenstein.txt', 'archivos/pride_and_prejudice.txt', 'archivos/the picture of dorian gray.txt']
for filename in filenames:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        count = content.lower().count('the')
        perfect_count= content.lower().count('the ')

        print(f"El archivo {filename} contiene aproximadamente {count} veces la palabra 'the' ")
        print(f"El archivo {filename} contiene exactamente {perfect_count} veces la palabra 'the' \n")
        