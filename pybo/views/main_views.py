from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/') # 블루프린트 객체 생성

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!!!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))


