from restaurante import Restaurante as resto 

my_restaurante = resto('la mini', 'pizzas')

my_restaurante.describir_restaurante()
my_restaurante.abrir_restaurante()

print(f"Este restaurante es conocido por su gran variedad de {my_restaurante.tipo_cocina}")