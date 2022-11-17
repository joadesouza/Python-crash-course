def get_formatted_name(first, last, middle=''):
    """
    Devuelve un nombre con formato
    :param first: nombre en formato String
    :param middle:  segundo nombre en formato String
    :param last:  apellido en formato String
    :return: nombre completo
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()