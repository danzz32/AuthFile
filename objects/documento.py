from models import db

class Documento(db.Model):
    __tablename__ = 'documentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    edital = db.Column(db.String(200), nullable=False)
    licitacao = db.Column(db.String(100), nullable=False)
    precos_de_referencia = db.Column(db.Text, nullable=True)  # Usando Text para campos potencialmente longos
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=False)

    # Relacionamento com a tabela Empresa
    empresa = db.relationship('Empresa', backref=db.backref('documentos', lazy=True))

    def __init__(self, nome, edital, licitacao, precos_de_referencia, empresa_id):
        self.nome = nome
        self.edital = edital
        self.licitacao = licitacao
        self.precos_de_referencia = precos_de_referencia
        self.empresa_id = empresa_id

    def exibir_informacoes(self):
        return (f"Nome: {self.nome}, Edital: {self.edital}, "
                f"Licitacao: {self.licitacao}, Precos de Referencia: {self.precos_de_referencia}, ID: {self.id}")
