import unittest

from sqlalchemy import text

from app import create_app
from models import db
from models.empresa_repository import Empresa


class TestEmpresaModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Configuração da aplicação e banco de dados para os testes """
        cls.app = create_app()
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """ Limpeza após os testes """
        with cls.app.app_context():
            db.drop_all()

    def test_database_creation(self):
        """ Testa se a tabela 'empresas' foi criada no banco de dados """
        with self.app.app_context():
            # Use a conexão diretamente para a execução da consulta
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT name FROM sqlite_master WHERE type='table' AND name='empresas';"))
                table_name = result.fetchone()
                self.assertIsNotNone(table_name, "A tabela 'empresas' não foi criada.")
                self.assertEqual(table_name[0], 'empresas')

    def test_add_empresa(self):
        """ Testa a adição de uma nova empresa ao banco de dados """
        with self.app.app_context():
            # Adiciona uma empresa
            nova_empresa = Empresa(
                nome='Empresa Teste',
                email_comercial='teste@empresa.com',
                senha='senha123',
                cnpj='12.345.678/0001-99',
                representante='Representante Teste'
            )
            db.session.add(nova_empresa)
            db.session.commit()

            # Depuração: imprime todos os registros na tabela para verificação
            all_empresas = Empresa.query.all()
            for emp in all_empresas:
                print(f"Empresa encontrada: {emp.nome}, {emp.email_comercial}")

    def test_get_by_email(self):
        """ Testa a obtenção de uma empresa pelo e-mail """
        with self.app.app_context():
            # Adiciona uma empresa
            nova_empresa = Empresa(
                nome='Empresa Teste',
                email_comercial='teste@empresa.com',
                senha='senha123',
                cnpj='12.345.678/0001-99',
                representante='Representante Teste'
            )
            db.session.add(nova_empresa)
            db.session.commit()

            # Depuração: imprime todos os registros na tabela para verificação
            all_empresas = Empresa.query.all()
            for emp in all_empresas:
                print(f"Empresa encontrada: {emp.nome}, {emp.email_comercial}")

    def test_update_empresa(self):
        """ Testa a atualização de uma empresa existente """
        with self.app.app_context():
            # Adiciona uma empresa
            nova_empresa = Empresa(
                nome='Empresa Teste',
                email_comercial='teste@empresa.com',
                senha='senha123',
                cnpj='12.345.678/0001-99',
                representante='Representante Teste'
            )
            db.session.add(nova_empresa)
            db.session.commit()

            # Obtém a empresa e atualiza
            empresa = Empresa.query.filter_by(email_comercial='teste@empresa.com').first()
            empresa.nome = 'Empresa Atualizada'
            db.session.commit()

            # Verifica se a empresa foi atualizada
            empresa_atualizada = Empresa.query.filter_by(email_comercial='teste@empresa.com').first()
            self.assertEqual(empresa_atualizada.nome, 'Empresa Atualizada')

            # Depuração: imprime todos os registros na tabela para verificação
            all_empresas = Empresa.query.all()
            for emp in all_empresas:
                print(f"Empresa encontrada: {emp.nome}, {emp.email_comercial}")

    def test_delete_empresa(self):
        """ Testa a exclusão de uma empresa existente """
        with self.app.app_context():
            # Adiciona uma empresa
            nova_empresa = Empresa(
                nome='Empresa Teste',
                email_comercial='teste@empresa.com',
                senha='senha123',
                cnpj='12.345.678/0001-99',
                representante='Representante Teste'
            )
            db.session.add(nova_empresa)
            db.session.commit()

            # Obtém a empresa e a exclui
            empresa = Empresa.query.filter_by(email_comercial='teste@empresa.com').first()
            self.assertIsNotNone(empresa, "A empresa não foi encontrada.")
            db.session.delete(empresa)
            db.session.commit()

            # Verifica se a empresa foi excluída
            empresa_deletada = Empresa.query.filter_by(email_comercial='teste@empresa.com').first()
            self.assertIsNone(empresa_deletada, "A empresa não foi excluída.")


if __name__ == '__main__':
    unittest.main()
