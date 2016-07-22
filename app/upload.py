from flask import jsonify, Blueprint, request, Response, render_template
import database
import properties
import json
import smtplib
from datetime import datetime
from datetime import timedelta
import uuid

upload_api = Blueprint('upload_api', __name__)

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    # print 'successfully sent the mail'
    # except:
    #     print "failed to send mail"
    
#Load Body Function to handle loading in backend DB data
def loadBody(requestData):

    #Add/Alter Data
    createdDate = datetime.utcnow()
    data = json.loads(requestData)
    
    data['expiration_date'] = calculateExpirationTime(createdDate, data['expiration_time'])
    data['type'] = "text"
    data['filename'] = ""
    data['created_date'] = str(createdDate)
    data['admin_password'] = str(uuid.uuid4())
    
    return data
    
# Calculate the expiration Time
def calculateExpirationTime(creationTime,minutesAdd):
    try:
        expirationTime = creationTime + timedelta(minutes=minutesAdd)
    except:
        expirationTime = creationTime + timedelta(minutes=15)
    
    return str(expirationTime)

@upload_api.route('/', methods=['GET'])
def upload():
    return render_template('publish.html')

@upload_api.route('/publish', methods=['POST'])
def publish():
    contentLength = int(request.headers.get('content-length'))
    body = loadBody(request.data)
    
    #validate json
    email = body['email']
    print email
    print contentLength, properties.maxFileSize
    id = ''
    if contentLength < properties.maxFileSize:
        #Return a 200 OK, Make a db entry
        temp=json.dumps(body)
        doc=json.loads(temp)

        try:
            id = database.db.create(doc)
            print "ID: %s" % id
        except:
            print "DB push exception"
            statusCode = 500
        statusCode = 200
        # send_email(properties.gmailAccount, properties.gmailPassword, email, properties.emailUploadSubject, "new paste has been created " + id)
    elif contentLength > properties.maxFileSize:
        #Return a 413 Payload to large, move on
        statusCode = 413
    else:
        #Return a 500 Internal Error, move on
        statusCode = 500

    return Response({"id":id}, mimetype='application/json', status=statusCode)
