from flask import Blueprint

bp = Blueprint('home', __name__, url_prefix='/')


def init_app(app):
    from . import (
        index
    )
    app.register_blueprint(bp)
