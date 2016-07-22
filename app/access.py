from flask import jsonify, Blueprint
import database

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):

    # Get entry from db
    doc = getDBEntry(uid)
    
    # If there, do stuff
    if doc != 0:
        
        # If password protected 
        if doc['password'] != '':
            #could set template=autorization_page instead of returning
            return 'authorization page'
        
        # If it's a file
        #if doc['type'] == 'file':
            #result = 'file'
            
            #TODO: Get file
    
    #TODO: decrement self-destruct counter 
    
        sdCounter = int(doc['self_destruct_count'])
        sdCounter -= 1
    
        if sdCounter <= 0:
            deleteDBEntry(doc)
        else: 
            doc['self_destruct_count'] = unicode(sdCounter)
            updateDBEntry(doc)
        
        result = jsonify(doc)
    
    else: 
        result = '404'
    #TODO: populate the template 
    
    return result
    
    
@access_api.route('/<uid>/<auth>', methods=['POST'])
def authorization(uid, auth):
    
    data = {}
    for i, id in enumerate(database.db):
        print i, id
        data[i] = id
    return jsonify(data)


def getDBEntry(uid):
    doc = 0
    for id in database.db:
        if id == uid:
            doc = database.db.get(id)
    return doc


def updateDBEntry(doc):
    return database.db.save(doc)
    
    
def deleteDBEntry(doc):
    return database.db.delete(doc)