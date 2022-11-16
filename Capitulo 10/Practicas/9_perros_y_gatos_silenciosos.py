filenames = ['Practicas/gatos.txt', 'perros.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            lines = f.readlines()
            print(f"\nThe names in {filename} are: ")
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.strip())