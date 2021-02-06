from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "f98c9d9340dc4bee35b4a18d79d0fba231d0d5b94ae7613b5c14ee017461dc22"
    app.config['SQLAlCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app=app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
