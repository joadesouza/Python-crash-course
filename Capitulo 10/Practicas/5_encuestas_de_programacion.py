# Escriba un bucle while que pregunte a la gente por que les gusta programar.
# Cada vez que alguien introduzca una razon añadala a un archivo que almacene 
# todas las respuestas.
flag = True
with open('practicas/respuesta_encuesta.txt', 'w') as file_object:
    while flag:
        print("Si no desea responder esta encuesta escriba 'finalizar'")
        respuesta = input("Hola, porque te gusta programar?: ")
        if respuesta.lower() == 'finalizar':
            flag = False
            print("Disculpe las molestias y muchas gracias por su tiempo")
            print("\n--- PROGRAMA FINALIZADO ---\n")
        else:
            file_object.write(f"{respuesta.capitalize()}\n")