from flask import jsonify, Blueprint, request, Response, render_template
import database
import properties
import json
import smtplib

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

@upload_api.route('/', methods=['GET'])
def upload():
    return render_template('publish.html')

@upload_api.route('/publish', methods=['POST'])
def publish():
    contentLength = int(request.headers.get('content-length'))
    body = request.data
    #validate json
    email = json.loads(body)['email']
    print contentLength, properties.maxFileSize
    if contentLength < properties.maxFileSize:
        #Return a 200 OK, Make a db entry
        doc = json.loads(body)
        try:
            id = database.db.create(doc)
            print id
        except:
            statusCode = 500
        statusCode = 200
        # send_email(properties.gmailAccount, properties.gmailPassword, email, properties.emailUploadSubject, "new paste has been created " + id)
    elif contentLength > properties.maxFileSize:
        #Return a 413 Payload to large, move on
        statusCode = 413
    else:
        #Return a 500 Internal Error, move on
        statusCode = 500
    # dataDict = json.loads(data)
    print body
    return Response(body, mimetype='application/json', status=statusCode)