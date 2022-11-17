# Escriba una funcion que acepte dos parametros: un nombre de ciudad y un nombre
# de pais.
# ->< La funcion deberia devolver una cadena sencilla con la forma Ciudad, Pais, como
# Santiago, Chile.
# ->< Guarde la funcion en un modulo llamado ciudad_funciones.py
# ->< Cree un archivo test_ciudades.py que pruebe la funcion que acaba de escribir
# (recuerde que tiene que importar unittest y la funcion que quiere probrar).
# ->< Escriba un metodo llamado test_ciudad_pais() para verificar que llamar a la
# funcion con valores como 'santiago' y 'chile' produce la cadena correcta.
# ->< Ejecute test_ciudades.py y asegurese de que test_ciudad_pais() pasa.

def ciudad_funciones(ciudad,  pais, habitantes=''):
    """Devuelve la ubicacion en formato: 
    
    ciudad, pais - habitantes
    Salta, Argentina - 150000 habitantes
    
    Args:
        ciudad (string): nombre de la ciudad
        pais (string): nombre del pais
        habitantes (int): cantidad de habitantes
    Returns:
        ubicacion: formateado como "ciudad, pais - habitantes"
    """
    if habitantes:
        ubicacion = f"{ciudad}, {pais} - {habitantes} habitantes"
        return ubicacion.title()
    else:
        ubicacion = f"{ciudad}, {pais}"
        return ubicacion.title()