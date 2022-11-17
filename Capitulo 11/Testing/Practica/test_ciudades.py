import unittest
from ciudad_funciones import ciudad_funciones

class Test_function_ciudad_funciones(unittest.TestCase):
    """Purebas para la funcion ciudad_funciones """
    
    def test_function_format_city_country_case(self):
        """
        Vamos a probar si retorna bien la ubicacion en el 
        formato "Ciudad, Pais" con Salta, Argentina
        """
        formatted_city_country = ciudad_funciones('salta', 'argentina')
        self.assertEqual(formatted_city_country, 'Salta, Argentina')
        
    def test_function_format_city_country_habs_case(self):
        """
        Vamos a probar si retorna al agregarle habitantes a la ciudad
        """
        formatted_city_country_habs = ciudad_funciones('santiago', 'chile', '50000000')
        self.assertEqual(formatted_city_country_habs, 'Santiago, Chile - 50000000 Habitantes')
        
if __name__ == '__main__':
    unittest.main()