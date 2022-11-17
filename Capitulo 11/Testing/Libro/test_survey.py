
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey"""
    
    def setUp(self):
        """
        Crea una Encuesta y un conjunto de respuestas para usar en todos los
    metodos de prueba
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses= ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Comprueba si una respuesta simple se guarda bien."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_multiple_response(self):
        """
        Comprueba que se guardan correctamente tres respuestas individuales.
        """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ('English', 'Spanish', 'Mandarin')
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()