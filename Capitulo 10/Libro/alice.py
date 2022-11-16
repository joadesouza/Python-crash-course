import word_count

filename = 'Libro/alice.txt'
filenames = ['Libro/alice.txt', 'Libro/harry_potter.txt', 'Libro/simbionte.txt']
for filename in filenames:
    word_count.count_words(filename)


"""
try:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
else:
    # Cuenta el numero aproximado de palabras en la fila.
    words = contents.split()
    num_words = len(words)
    print(f"The file{filename} has about {num_words} words.")
    
"""