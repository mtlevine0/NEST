from flask import jsonify, Blueprint

delete_api = Blueprint('delete_api', __name__)

@delete_api.route('/delete')
def WelcomeToMyapp():
    return 'delete page'
