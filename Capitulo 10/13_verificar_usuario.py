# El listado definitivo de remember_me.py asume que el usuario ya a 
# introducido su nombre o que el programa se ejecuta por primera vez. 
# Deberiamos modificarlo por si el usuario actual no es la unica persona 
# que usó el programa.
# Antes de imprimir el mensaje de bienvenida en greet_user(), pregunte al
# usuario si es el nombre correcto. 
# Si no, llame a get_new_username() para obtener el nombre de usuario 
# adecuado

from fileinput import filename
from Libro.remember_me import *

print("Responda con si/no..")
question = input(f"Es usted el usuario [{get_stored_username()}] ? ")
if question.lower() == "si":
    greet_user()
else:
    get_new_user()

