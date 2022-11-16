def count_words(filename):
    """
    Vamos a leer un archivo de texto si es que ha sido generado
    o se encuentra en nuestro directorio

    Args:
        filename (txt): Archivo de texto
    """
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")    

filenames = ['Libro/alice.txt', 'Libro/harry_potter.txt', 'Libro/simbionte.txt']
for filename in filenames:
    count_words(filename)