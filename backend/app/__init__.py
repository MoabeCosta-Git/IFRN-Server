from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .config import Config

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.json.sort_keys = False

    db.init_app(app)
    migrate.init_app(app)
    ma.init_app(app, db)

    app.register_blueprint()

    return app