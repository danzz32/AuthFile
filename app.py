from flask import Flask
from config import Config
from models import init_db
from controllers.routes import main_bp      

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Iniciando o banco de dados
    init_db(app)

    # Registrar rotas e blueprints
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
