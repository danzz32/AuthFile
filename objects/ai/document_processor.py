# import torch
# from transformers import BertTokenizer, BertForSequenceClassification
#
#
# class DocumentProcessor:
#     def __init__(self, model_path, tokenizer_path):
#         # Carregar o modelo e o tokenizer BERT
#         self.tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
#         self.model = BertForSequenceClassification.from_pretrained(model_path)
#
#     def analyze(self, text):
#         # Tokenizar o texto
#         inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
#         # Fazer a previsão
#         with torch.no_grad():
#             outputs = self.model(**inputs)
#         # Supondo que a saída do modelo seja logits para uma classificação
#         predictions = torch.argmax(outputs.logits, dim=-1)
#         return predictions.numpy()
