import os

from flask import Flask
from flask import render_template

from config import config
from views import test


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return os.getenv('FLASK_CONFIG')

    return app

app = create_app(os.getenv('FLASK_CONFIG') or 'development')

if __name__ == '__main__':
    app.run()