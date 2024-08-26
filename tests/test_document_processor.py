import unittest
from objects.document_processor import DocumentProcessor
import os

class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        # Configurações iniciais para os testes
        self.processor = DocumentProcessor()
        self.test_pdf = 'tests/test_document.pdf'
        
        # Cria um PDF de teste
        with open(self.test_pdf, 'w') as f:
            f.write("%PDF-1.4\n%����\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n2 0 obj\n<<\n/Type /Pages\n/Count 1\n/Kids [3 0 R]\n>>\nendobj\n3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/Resources <<\n/ProcSet [/PDF /Text]\n/Font <<\n/F1 5 0 R\n>>\n>>\n>>\nendobj\n4 0 obj\n<<\n/Length 44\n>>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(Teste de PDF) Tj\nET\nendstream\nendobj\n5 0 obj\n<<\n/Type /Font\n/Subtype /Type1\n/BaseFont /Helvetica\n>>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000073 00000 n \n0000000121 00000 n \n0000000202 00000 n \n0000000283 00000 n \ntrailer\n<<\n/Size 6\n/Root 1 0 R\n>>\nstartxref\n344\n%%EOF")
    
    def tearDown(self):
        # Limpa após os testes
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)

    def test_read_pdf(self):
        # Testa a extração de texto do PDF
        text = self.processor.read_pdf(self.test_pdf)
        self.assertIn("Teste de PDF", text)
    
    def test_process_document(self):
        # Testa o processamento do documento
        processed_data = self.processor.process_document(self.test_pdf)
        
        # Verifica se o retorno não está vazio
        self.assertTrue(processed_data.size(0) > 0)
        print(f"Processed Data: {processed_data}")

if __name__ == '__main__':
    unittest.main()
