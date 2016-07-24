from flask import jsonify, Blueprint, request, Response, render_template, redirect
from datetime import datetime
from datetime import timedelta
import database
import properties
import json
import publishHelper
from .forms import PublishForm


publish_api = Blueprint('publish_api', __name__)


@publish_api.route('/', methods=['GET'])
def landing():
    form = PublishForm()
    return render_template('publish.html', form=form)


@publish_api.route('/', methods=['POST'])
def publish():
    form = PublishForm()
    contentLength = int(request.headers.get('content-length'))
    rawRequest = json.dumps(form.data)
    doc = publishHelper.loadBody(rawRequest)
    
    if contentLength < properties.maxFileSize:
        
        #TODO: handle bad requests such as text in a numeric field
        try:
            id = database.db.create(doc)
            print "ID: %s" % id
        except:
            print "DB push exception"
            statusCode = 500
        statusCode = 200
        
        try:
            publishHelper.send_email(properties.gmailAccount,
            properties.gmailPassword, doc['email'], 
            properties.emailUploadSubject, "new paste has been created " + id)
        except:
            pass
        
    elif contentLength > properties.maxFileSize:
        #Return a 413 Payload to large, move on
        statusCode = 413
    else:
        #Return a 500 Internal Error, move on
        statusCode = 500

    Response('{"id":"'+id+'"}', mimetype='application/json', status=statusCode)
    
    return redirect("/" + id, code=302)