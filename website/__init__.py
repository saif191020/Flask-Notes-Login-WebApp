from flask import Flask

def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] ="f98c9d9340dc4bee35b4a18d79d0fba231d0d5b94ae7613b5c14ee017461dc22"
    return app