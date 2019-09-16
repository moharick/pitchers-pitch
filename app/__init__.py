
from flask import Flask
from config import Config
app =  Flask(__name__)

def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app