from flask import jsonify, Blueprint

access_api = Blueprint('access_api', __name__)

@access_api.route('/access')
def WelcomeToMyapp():
    return 'access page'
