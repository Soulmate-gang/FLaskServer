from flask import jsonify

from . import bp


@bp.route('/index', methods=['GET'])
def index():
    """ index """
    return jsonify({})
