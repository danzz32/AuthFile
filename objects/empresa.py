from models import db

class Empresa(db.Model):
    __tablename__ = 'empresas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)  # Assumindo CNPJ como string com 14 caracteres
    representante = db.Column(db.String(100), nullable=False)
    email_comercial = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    documentos = db.relationship('Documento', back_populates='empresa', cascade='all, delete-orphan')

    def __init__(self, nome, cnpj, representante, email_comercial, senha):
        self.nome = nome
        self.cnpj = cnpj
        self.representante = representante
        self.email_comercial = email_comercial
        self.senha = senha
