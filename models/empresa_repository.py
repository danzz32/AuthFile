from objects.empresa import Empresa

from models import db


class EmpresaRepository:
    def __init__(self):
        pass

    def add(self, empresa):
        """
        Adiciona uma nova Empresa ao banco de dados.
        """
        db.session.add(empresa)
        db.session.commit()

    def get_by_email(self, email):
        """
        Recupera uma Empresa pelo seu e-mail.
        """
        return Empresa.query.filter_by(email_comercial=email).first()

    def get_by_id(self, empresa_id):
        """
        Recupera uma Empresa pelo seu ID.
        """
        return Empresa.query.get(empresa_id)

    def get_all(self):
        """
        Recupera todas as Empresas do banco de dados.
        """
        return Empresa.query.all()

    def update(self, empresa):
        """
        Atualiza uma Empresa existente.
        """
        db.session.commit()

    def delete(self, empresa):
        """
        Remove uma Empresa do banco de dados.
        """
        db.session.delete(empresa)
        db.session.commit()
