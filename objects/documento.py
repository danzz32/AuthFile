from models import db

class Documento(db.Model):
    __tablename__ = 'documentos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    caminho_edital = db.Column(db.String(255))
    caminho_precos = db.Column(db.String(255))
    caminho_licitacao = db.Column(db.String(255))
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=False)
    
    empresa = db.relationship('Empresa', back_populates='documentos')
    itens = db.relationship('Item', back_populates='documento', cascade='all, delete-orphan')
    
    def __init__(self, nome, caminho_edital, caminho_precos, caminho_licitacao, empresa_id):
        self.nome = nome
        self.caminho_edital = caminho_edital
        self.caminho_precos = caminho_precos
        self.caminho_licitacao = caminho_licitacao
        self.empresa_id = empresa_id
