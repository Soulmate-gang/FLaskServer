from flask import jsonify

from . import bp


@bp.route('/index', methods=['GET'])
def index():
    """ index """
    data = {"content": "ths is index"}
    return jsonify(data)
