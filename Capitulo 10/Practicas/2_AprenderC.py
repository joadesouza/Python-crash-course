
with open('Practicas/aprender_python.txt') as file_object:
    lines = file_object.readlines()
    
for line in lines:    
    line = line.replace("python", "Java")
    print(line.rstrip())
