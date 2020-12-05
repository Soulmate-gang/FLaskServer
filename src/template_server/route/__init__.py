from flask import Blueprint

bp = Blueprint('home', __name__, url_prefix='/')


def init_app(app):
    from template_server.route import index
    app.register_blueprint(bp)
