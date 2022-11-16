from fileinput import filename
import json


import json

def get_stored_username():
    """Obtiene un nombre de usuario almacenado si esta disponible"""
    filename = 'users.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_user():
    """Genera un nuevo nombre de usuario"""
    filename = 'users.json'    
    username = input("Como es su nombre de usuario? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Excelente, lo recordaremos cuando regrese {username}")
    
def greet_user():
    """Saluda al usuario por su nombre"""    
    username = get_stored_username()
    if username:
        print(f"Bienvenido de vuelta {username}!!")
    else:
        filename = 'users.json'
        username = get_new_user()
