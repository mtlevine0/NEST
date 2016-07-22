from flask import jsonify, Blueprint, render_template
import database
import objectstorage

delete_api = Blueprint('delete_api', __name__)

#API to remove the page using the uid and admin password
@delete_api.route('/delete/<uid>/<password>', methods=['POST'])
def removeEgg(uid, urlAdminPassword):
    
    #Retrieve Doc
    doc = database.getDBEntry(uid)
    
    #Set Variables From Doc
    try:
        docFileName = str(doc['filename'])
        docAdminPassword = str(doc['admin_password'])
        docType = docTypeCheck(doc)
    except:
        print "There was an issue setting up the variables for Document ID: %s" % uid
    
    if (docAdminPassword != urlAdminPassword):
        result = render_template('error.html',message="403 Access Forbidden")
        
    elif (docAdminPassword == urlAdminPassword):
        try:
            if (docFileName > "" or docType == "file"):
                fileDeleteSuccess = deleteOSFile(docFileName)
                result =  render_template('error.html',message=deleteDBDoc(doc,fileDeleteSuccess))
            else:
                result = render_template('error.html',message=deleteDBDoc(doc,True))
        except:
            result = render_template('error.html',message="500 Internal Server Error - A delete failed somplace")
            print "There was an exception processing the deletion of the Invalid Type Document ID: %s" % uid
    
    return result
    

def docTypeCheck(document):
    print "docTypeCheck for ID: %s" % id
    #Try to set the docType Variable
    try:
        docType = document['type'].lower()
    except:
        print "An exception occurred checking the docType for Document ID: %s" % id
        return "invalid"
        
    if (docType == "file"):
        return "file"
    elif (docType == "text"):
        return "text"
    else:
        return "invalid"

#Delete Document from the DB
def deleteDBDoc(document,FileRemovalStatus):
    if(FileRemovalStatus == True):
        try:
            database.db.delete(document)
            print "We have successfully deleted document with ID: %s" % id
            return "Delete Successful"
        except:
            print "Something went wrong trying to delete the DB document associated with document ID: %s" % id
            return "500 Internal Server Error - DB Delete Failed"
    else:
        return "500 Internal Server Error - Potential File Delete Failed"
        
def deleteOSFile(fileName):
    try:
        objectstorage.deleteFile(fileName)
        print "We have successfully deleted the file associated with document ID: %s" % id
        return True
    except:
        print "Something went wrong trying to delete the File associated with document ID: %s" % id
        return False
