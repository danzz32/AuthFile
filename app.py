from flask import Flask
from config import Config
from models import init_db
from models.empresa_repository import Empresa


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Iniciando o banco de dados
    init_db(app)

    from controllers.routes import main_bp
    app.register_blueprint(main_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
