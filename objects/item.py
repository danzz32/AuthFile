from models import db

class Item(db.Model):
    __tablename__ = 'itens'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)  # Número do item, pode ser alfanumérico
    descricao = db.Column(db.String(255), nullable=False)  # Descrição do item
    unidade = db.Column(db.String(50), nullable=False)  # Unidade de medida do item
    quantidade = db.Column(db.Float, nullable=False)  # Quantidade do item
    preco_unitario = db.Column(db.Float, nullable=False)  # Preço unitário do item
    preco_total = db.Column(db.Float, nullable=False)  # Preço total do item
    documento_id = db.Column(db.Integer, db.ForeignKey('documentos.id'), nullable=False)
    
    documento = db.relationship('Documento', back_populates='itens')
    
    def __init__(self, numero, descricao, unidade, quantidade, preco_unitario, preco_total):
        self.numero = numero
        self.descricao = descricao
        self.unidade = unidade
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.preco_total = preco_total
