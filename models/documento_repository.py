from models import db
from objects.documento import Documento
from typing import Optional, List

class DocumentoRepository:
    def __init__(self):
        pass

    def add(self, documento: Documento) -> None:
        """
        Adiciona um novo Documento ao banco de dados.
        """
        try:
            db.session.add(documento)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Failed to add documento: {e}")

    def get_by_id(self, documento_id: int) -> Optional[Documento]:
        """
        Recupera um Documento pelo seu ID.
        """
        return Documento.query.get(documento_id)

    def get_all(self) -> List[Documento]:
        """
        Recupera todos os Documentos do banco de dados.
        """
        return Documento.query.all()

    def update(self, documento: Documento) -> None:
        """
        Atualiza um Documento existente.
        """
        try:
            db.session.merge(documento)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Failed to update documento: {e}")

    def delete(self, documento: Documento) -> None:
        """
        Remove um Documento do banco de dados.
        """
        try:
            db.session.delete(documento)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Failed to delete documento: {e}")
