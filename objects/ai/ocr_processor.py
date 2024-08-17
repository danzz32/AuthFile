# import fitz
# import pytesseract
# from PIL import Image
# from docx import Document
#
#
# class OcrProcessor:
#     def __init__(self, language='por'):
#         self.language = language
#
#     def process(self, file_path):
#         if file_path.endswith('.pdf'):
#             return self._extract_text_from_pdf(file_path)
#         elif file_path.endswith('.docx'):
#             return self._extract_text_from_word(file_path)
#         elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#             return self._extract_text_from_image(file_path)
#         else:
#             raise ValueError('Tipo arquivo não suportado!')
#
#     def _extract_text_from_pdf(self, file_path):
#         text = ''
#         pdf_document = fitz.open(file_path)
#         for page_num in range(len(pdf_document)):
#             page = pdf_document.load_page(page_num)
#             text += page.get_text()
#         return text
#
#     def _extract_text_from_word(self, file_path):
#         text = ''
#         doc = Document(file_path)
#         for para in doc.paragraphs:
#             text += para.text + '\n'
#         return text
#
#     def _extract_text_from_image(self, file_path):
#         img = Image.open(file_path)
#         return pytesseract.image_to_string(img, lang=self.language)
