with open('Practicas/aprender_python.txt') as file_object:
    contenido = file_object.read()

print(contenido.rstrip()) 
print()

filename = 'Practicas/aprender_python.txt'
n=1

with open(filename) as file_object:
    lines = file_object.readlines()
    
while n < 3:
    print()
    for line in lines:
        print(line.rstrip())
    n += 1
    
