from flask import Blueprint, render_template, request
import database
import accessHelper
from .forms import AuthForm

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):

    # Get entry from db
    doc = database.getDBEntry(uid)
    # If there, do stuff
    if doc != 0:
        # If password protected 
        if doc['recently_created'] == True:
            #TODO: Get file
            doc['recently_created'] = False
            database.updateDBEntry(doc)
            result = render_template('access.html', content=doc['text'], 
                                                    sdCounter=doc['sdCounter'])
                                                    
        elif doc['password'] == '':
            result = render_template('access.html', content=doc['text'], 
                                        sdCounter=accessHelper.incrementSD(doc))
                                        
        else:
            form = AuthForm()
            result = render_template('auth.html', form=form, uid=uid)
                
    else: 
        result = render_template('404.html')
 
    
    return result
    
    
@access_api.route('/<uid>', methods=['POST'])
def authorization(uid):
    
    doc = database.getDBEntry(uid)
    
    if doc != 0:
        password = request.form['pass_input']
        form = AuthForm()
    
        #TODO: Access lockout
    
        if doc['password'] != password: 
            #TODO: add error parameter
            result = render_template('auth.html', form=form, uid=uid, 
                        message='Ah, Ah, Ah! You didn\'t say the magic word!')
        else:
            result = render_template('access.html', content=doc['text'], 
                                        sdCounter=accessHelper.incrementSD(doc))

    else: 
        result = render_template('404.html')
        
    return result
