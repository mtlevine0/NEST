from flask import jsonify, request, Response
import database
import properties
import json
import smtplib
from datetime import datetime
from datetime import timedelta
import uuid

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
        expirationTime = creationTime + timedelta(minutes=int(minutesAdd))  
    except:
        expirationTime = creationTime + timedelta(minutes=15)
    
    return str(expirationTime)