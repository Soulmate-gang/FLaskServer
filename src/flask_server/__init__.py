from flask import Flask

from flask_server import config


def create_app(test_config=None):
    """ 创建应用 """
    flask_app = Flask(__name__, instance_relative_config=True)
    config.instance_pth.mkdir(exist_ok=True)

    # 跨域支持
    from flask_cors import CORS
    CORS(flask_app, supports_credentials=True)

    dev_db = config.instance_pth / 'dev.sqlite'
    flask_app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{dev_db.absolute()}'
    )
    if test_config:
        flask_app.config.from_mapping(test_config)
    else:
        flask_app.config.from_pyfile('config.py', silent=True)

    from flask_server import models
    models.init_app(flask_app)

    from flask_server import route
    route.init_app(flask_app)

    return flask_app


app = create_app()
app.app_context().push()
