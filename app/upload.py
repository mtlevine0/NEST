from flask import jsonify, Blueprint

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/upload')
def WelcomeToMyapp():
    return 'upload page'
