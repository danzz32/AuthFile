# import pdfplumber

# def extract_table_from_pdf(pdf_path):
#     items = []
    
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             # Supondo que a tabela esteja na primeira página
#             page = pdf.pages[0]
            
#             # Verificar se a página tem uma tabela
#             if not page.extract_table():
#                 raise ValueError("Nenhuma tabela encontrada na primeira página.")
                
#             table = page.extract_table()
            
#             # Verificar se a tabela foi extraída corretamente
#             if not table or len(table) < 2:
#                 raise ValueError("Tabela não contém dados suficientes.")
            
#             # Converta a tabela para uma lista de dicionários
#             headers = table[0]
#             for row in table[1:]:
#                 # Garantir que cada linha tem o mesmo número de colunas que os cabeçalhos
#                 if len(row) != len(headers):
#                     raise ValueError("Número de colunas na linha não corresponde ao número de cabeçalhos.")
                
#                 item = dict(zip(headers, row))
#                 items.append(item)
    
#     except Exception as e:
#         print(f"Erro ao extrair tabela do PDF: {e}")
    
#     return items
