from flask import jsonify, Blueprint, request, Response, render_template
import database
import properties
import json
import smtplib
from datetime import datetime
from datetime import timedelta
import uuid
import publishHelper

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/', methods=['GET'])
def upload():
    return render_template('publish.html')


@upload_api.route('/publish', methods=['POST'])
def publish():
    contentLength = int(request.headers.get('content-length'))
    body = publishHelper.loadBody(request.data)
    
    #validate json
    email = body['email']
    print email
    print contentLength, properties.maxFileSize
    id = ''
    if contentLength < properties.maxFileSize:
        #Return a 200 OK, Make a db entry
        temp=json.dumps(body)
        doc=json.loads(temp)

        #TODO: handle bad requests such as text in a numeric field

        try:
            id = database.db.create(doc)
            print "ID: %s" % id
        except:
            print "DB push exception"
            statusCode = 500
        statusCode = 200
        try:
            publishHelper.send_email(properties.gmailAccount, properties.gmailPassword, email, properties.emailUploadSubject, "new paste has been created " + id)
        except:
            pass
    elif contentLength > properties.maxFileSize:
        #Return a 413 Payload to large, move on
        statusCode = 413
    else:
        #Return a 500 Internal Error, move on
        statusCode = 500

    return Response('{"id":"'+id+'"}', mimetype='application/json', status=statusCode)
