from flask import Flask
from app.config import Config
from app.extensions import db, ma, migrate

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from app.routes.usuarios import usuario_bp
    from app.routes.tarefas import tarefa_bp
    
    app.register_blueprint(usuario_bp)
    app.register_blueprint(tarefa_bp)

    return app