import unittest

from sqlalchemy import text

from app import create_app
from models import db


class TestDatabaseCreation(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
