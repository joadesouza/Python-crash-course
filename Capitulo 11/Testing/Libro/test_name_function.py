import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Pruebas para 'name_function.py' """

    def test_first_last_name(self):
        """Funcionan nombres como Janis Joplin?? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """
        Funcionan nombres complejos como Woflgang Amadeus Mozart?
        """
        formatted_name = get_formatted_name('Wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()