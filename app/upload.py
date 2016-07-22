from flask import jsonify, Blueprint

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/', methods=['GET'])
def upload():
    return 'upload page'

@upload_api.route('/publish', methods=['POST'])
def publish():
    return 'publish page'