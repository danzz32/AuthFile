from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()


def init_db(app):
    """ Configurando aplicação Flask com SQLAlchemy e iniciando o banco de dados """

    db.init_app(app)

    with app.app_context():
        # Cria todas as tabelas no banco de dados
        db.create_all()

        # Verifica se as tabelas foram criadas
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        if tables:
            print("Tabelas e Banco de Dados criados")
            print("Tabelas existentes no banco de dados:")
            for table in tables:
                print(f"- {table}")
        else:
            print("Nenhuma tabela encontrada no banco de dados.")
