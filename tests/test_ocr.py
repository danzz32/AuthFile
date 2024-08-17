# import os
#
# import pytest
# from PIL import Image, ImageDraw
#
# from objects.ai import OcrProcessor
#
# # Caminhos para arquivos de teste
# TEST_PDF_PATH = 'authfile/tests/test_document.pdf'
# TEST_DOCX_PATH = 'authfile/tests/test_document.docx'
# TEST_IMAGE_PATH = 'authfile/tests/test_image.png'
#
#
# @pytest.fixture
# def ocr_processor():
#     return OcrProcessor(language='por')
#
#
# def setup_module(module):
#     # Criar arquivos de teste antes dos testes
#     # Criar PDF de teste
#     from fpdf import FPDF
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Texto de teste para PDF.", ln=True)
#     pdf.output(TEST_PDF_PATH)
#
#     # Criar DOCX de teste
#     from docx import Document
#     doc = Document()
#     doc.add_paragraph("Texto de teste para DOCX.")
#     doc.save(TEST_DOCX_PATH)
#
#     # Criar imagem de teste
#     img = Image.new('RGB', (100, 100), color='white')
#     d = ImageDraw.Draw(img)
#     d.text((10, 10), "Texto de teste para imagem", fill=(0, 0, 0))
#     img.save(TEST_IMAGE_PATH)
#
#
# def teardown_module(module):
#     # Remover arquivos de teste após os testes
#     for file_path in [TEST_PDF_PATH, TEST_DOCX_PATH, TEST_IMAGE_PATH]:
#         if os.path.exists(file_path):
#             os.remove(file_path)
#
#
# def test_ocr_process_pdf(ocr_processor):
#     text = ocr_processor.process(TEST_PDF_PATH)
#     assert "Texto de teste para PDF." in text, "Texto extraído do PDF está incorreto"
#
#
# def test_ocr_process_docx(ocr_processor):
#     text = ocr_processor.process(TEST_DOCX_PATH)
#     assert "Texto de teste para DOCX." in text, "Texto extraído do DOCX está incorreto"
#
#
# def test_ocr_process_image(ocr_processor):
#     text = ocr_processor.process(TEST_IMAGE_PATH)
#     assert "Texto de teste para imagem" in text, "Texto extraído da imagem está incorreto"
