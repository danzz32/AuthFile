import unittest
from flask import Flask
from flask.testing import FlaskClient
from controllers.main_controller import main_controller

class TestDocumentProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(main_controller)
        cls.client: FlaskClient = cls.app.test_client()

    def test_analyze_document(self):
        # Texto de exemplo para análise
        sample_text = """
        Nome: João da Silva
        CPF: 123.456.789-00
        Endereço: Rua Exemplo, 123
        """

        # Simule a análise do texto
        response = self.client.post('/analyze', json={'text': sample_text})

        # Verifique a resposta
        self.assertEqual(response.status_code, 200)
        response_data = response.json
        self.assertIn('predictions', response_data)
        self.assertIsInstance(response_data['predictions'], list)

if __name__ == '__main__':
    unittest.main()
