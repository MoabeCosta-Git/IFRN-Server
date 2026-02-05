from flask import Flask
from app.config import Config
from app.extensions import db, ma, migrate, login_manager
from app.models.usuario import Usuario

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from app.routes.usuarios import usuario_bp
    from app.routes.tarefas import tarefa_bp
    from app.routes.auth import auth_bp
    
    app.register_blueprint(usuario_bp)
    app.register_blueprint(tarefa_bp)
    app.register_blueprint(auth_bp)

    return app