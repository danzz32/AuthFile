from app.models import db
from app.objects.documento import Documento


class DocumentoRepository:
    def __init__(self):
        pass

    def add(self, documento):
        """
        Adiciona um novo Documento ao banco de dados.
        """
        db.session.add(documento)
        db.session.commit()

    def get_by_id(self, documento_id):
        """
        Recupera um Documento pelo seu ID.
        """
        return Documento.query.get(documento_id)

    def get_all(self):
        """
        Recupera todos os Documentos do banco de dados.
        """
        return Documento.query.all()

    def update(self, documento):
        """
        Atualiza um Documento existente.
        """
        db.session.commit()

    def delete(self, documento):
        """
        Remove um Documento do banco de dados.
        """
        db.session.delete(documento)
        db.session.commit()
