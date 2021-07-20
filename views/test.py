from flask import Blueprint
from flask import render_template

bp = Blueprint('testing', __name__, url_prefix='/testing')

@bp.route('/register', methods=(['GET']))
def index():
    return render_template('hello.html', name="Muzzammil Hussain")