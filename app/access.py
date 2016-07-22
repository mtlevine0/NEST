from flask import jsonify, Blueprint
import database


access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):

    #TODO: if uid in db
    
        #TODO: pull back data
    
        #TODO: if password != NULL
        
            #TODO: return autorizaion page
        
        #TODO: if type == file
            
            #TODO: Grab the file
    
    #TODO: Increment self-destruct counter 
    
    #TODO: populate the template 
    
    return 'access page'
    
    
@access_api.route('/<uid>/<auth>', methods=['POST'])
def authorization(uid, auth):
    
    data = {}
    for i, id in enumerate(database.db):
        print i, id
        data[i] = id
    return jsonify(data)

