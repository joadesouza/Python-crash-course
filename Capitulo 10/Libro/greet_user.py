import json

filename = 'users.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Bienvenido de vuelta {username}")