from flask import Flask
from flask import render_template

from views import test

app = Flask(__name__)

app.register_blueprint(test.bp)
