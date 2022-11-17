import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    """Test sobre empleado.py"""
    
    def setUp(self):
        """Crea una persona empleada para probar los aumentos"""
        self.nombre = "Joaquin"
        self.apellido = "De Souza"
        self.salario_anual = 25000
    
    
    def test_dar_aumento_predeterminado(self):
        """Prueba que el aumento de 5000 predeterminado se aplique"""
        Empleado.dar_aumento(self, "")
        self.assertEqual(self.salario_anual, 30000)

    def test_dar_aumento_personalizado(self):
        """Prueba que el aumento que se requiere dar
        se aplique"""
        
        Empleado.dar_aumento(self, 1000)
        self.assertEqual(self.salario_anual, 26000)

if __name__ == '__main__':
    unittest.main()