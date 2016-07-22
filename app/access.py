from flask import jsonify, Blueprint, render_template
import database
from .forms import AuthForm

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):

    # Get entry from db
    doc = getDBEntry(uid)
    
    # If there, do stuff
    if doc != 0:
        
        # If password protected 
        if doc['password'] != '':
            form = AuthForm()
            result = render_template('auth.html', form=form)
            
        else:
            #TODO: Get file
    
            # increment the self destruct time / handle deleting entry if 0
            incrementSD(doc)
            result = render_template('access.html', doc=doc)
    
    else: 
        result = render_template('404.html')
    #TODO: populate the template 
    
    return result
    
    
@access_api.route('/<uid>', methods=['POST'])
def authorization(password, uid):
    
    doc = getDBEntry(uid)
    
    if doc['password'] != password: 
        #TODO: add error parameter
        result = render_template('auth.html')
    else:
        incrementSD(doc)
        result = render_template('access.html')
    
    return result


def getDBEntry(uid):
    doc = 0
    for id in database.db:
        if id == uid:
            doc = database.db.get(id)
    return doc


def incrementSD(doc):
    sdCounter = int(doc['self_destruct_count'])
    sdCounter -= 1
    
    if sdCounter <= 0:
        deleteDBEntry(doc)
    else: 
        doc['self_destruct_count'] = unicode(sdCounter)
        updateDBEntry(doc)
    

def updateDBEntry(doc):
    return database.db.save(doc)
    
    
def deleteDBEntry(doc):
    return database.db.delete(doc)
    

    