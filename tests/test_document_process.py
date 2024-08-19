import unittest
import numpy as np
from objects.ai import DocumentProcessor

# Substitua pelos caminhos corretos do seu modelo e tokenizer
MODEL_PATH = 'path/to/your/bert/model'
TOKENIZER_PATH = 'path/to/your/bert/tokenizer'


class TestDocumentProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.document_processor = DocumentProcessor(model_path=MODEL_PATH, tokenizer_path=TOKENIZER_PATH)

    def test_document_processing(self):
        # Texto de exemplo para análise
        sample_text = """
        Nome: João da Silva
        CPF: 123.456.789-00
        Endereço: Rua Exemplo, 123
        """

        # Campos a serem buscados
        fields_to_find = ['Nome', 'CPF', 'Endereço']

        # Simule a análise do texto
        results = self.document_processor.analyze(sample_text, fields_to_find)

        # Valide os resultados esperados
        self.assertIsInstance(results, dict, "Os resultados devem ser um dicionário")
        self.assertEqual(len(results), len(fields_to_find),
                         "O número de campos encontrados deve corresponder ao número de campos buscados")

        for field in fields_to_find:
            self.assertIn(field, results, f"Campo '{field}' não encontrado no resultado")
            self.assertIn('start', results[field], f"Localização do campo '{field}' está incorreta")
            self.assertIn('end', results[field], f"Localização do campo '{field}' está incorreta")
            self.assertLess(results[field]['start'], results[field]['end'],
                            f"A localização do campo '{field}' está incorreta")

        # Caso queira validar o conteúdo dos campos encontrados (opcional)
        self.assertEqual(sample_text[results['Nome']['start']:results['Nome']['end']], 'Nome',
                         "Conteúdo do campo 'Nome' está incorreto")
        self.assertEqual(sample_text[results['CPF']['start']:results['CPF']['end']], 'CPF',
                         "Conteúdo do campo 'CPF' está incorreto")
        self.assertEqual(sample_text[results['Endereço']['start']:results['Endereço']['end']], 'Endereço',
                         "Conteúdo do campo 'Endereço' está incorreto")


if __name__ == '__main__':
    unittest.main()
