import os

from flask import Flask
from flask import render_template

from config import config
from app.views import test
from app.helpers.sqlalchemy import db  


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return os.getenv('FLASK_CONFIG')

    return app
