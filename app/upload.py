from flask import jsonify, Blueprint, request, Response
import database
import properties

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/', methods=['GET'])
def upload():
    return 'upload page'

@upload_api.route('/publish', methods=['POST'])
def publish():
    content_length = request.headers.get('content-length')
    body = request.data
    
    
    
    # dataDict = json.loads(data)
    print body
    return Response(body, mimetype='application/json')