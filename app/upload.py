from flask import jsonify, Blueprint, request, Response
import database
import properties
import json

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/', methods=['GET'])
def upload():
    return 'upload page'

@upload_api.route('/publish', methods=['POST'])
def publish():
    contentLength = int(request.headers.get('content-length'))
    body = request.data
    #validate json
    print contentLength, properties.maxFileSize
    if contentLength < properties.maxFileSize:
        #Return a 200 OK, Make a db entry
        doc = json.loads(body)
        try:
            database.db.create(doc)
            print doc
        except:
            statusCode = 500
        statusCode = 200
    elif contentLength > properties.maxFileSize:
        #Return a 413 Payload to large, move on
        statusCode = 413
    else:
        #Return a 500 Internal Error, move on
        statusCode = 500
    # dataDict = json.loads(data)
    print body
    return Response(body, mimetype='application/json', status=statusCode)