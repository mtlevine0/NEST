from flask import Blueprint, render_template, request
import database
from .forms import AuthForm

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):

    # Get entry from db
    doc = database.getDBEntry(uid)
    # If there, do stuff
    if doc != 0:
        
        # If password protected 
        if doc['password'] == '':
            #TODO: Get file
            # increment the self destruct time / handle deleting entry if 0
            if doc['self_destruct_count'] != '':
                result = render_template('access.html', paste=doc['text'], 
                                                    sdCounter=incrementSD(doc))
            else: 
                result = render_template('access.html', paste=doc['text'])
                
        else:
            form = AuthForm()
            result = render_template('auth.html', form=form, uid=uid)
    else: 
        result = render_template('404.html')
    #TODO: populate the template 
    
    return result
    
    
@access_api.route('/<uid>', methods=['POST'])
def authorization(uid):
    
    doc = database.getDBEntry(uid)
    password = request.form['pass_input']
    form = AuthForm()
    
    #TODO: Access lockout
    
    if doc['password'] != password: 
        #TODO: add error parameter
        result = render_template('auth.html', form=form, uid=uid, 
                            message='Ah, Ah, Ah! You didn\'t say the magic word!')
    else:
        result = render_template('access.html', paste=doc['text'], 
                                                    sdCounter=incrementSD(doc))
        
    return result
    
    
def incrementSD(doc):
    
    sdCounter = int(doc['self_destruct_count'])
    sdCounter -= 1
    
    if sdCounter == 0:
        database.deleteDBEntry(doc)
    else: 
        doc['self_destruct_count'] = unicode(sdCounter)
        database.updateDBEntry(doc)
            
    return sdCounter

    

    