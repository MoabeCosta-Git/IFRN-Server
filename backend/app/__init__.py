from flask import Flask
from .config import Config
from .extensoes import 

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.json.sort_keys = False

    db.init_app(app)
    migrate.init_app(app)
    ma.init_app(app, db)

    app.register_blueprint()

    return app