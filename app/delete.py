from flask import jsonify, Blueprint, render_template
import database
import objectstorage

delete_api = Blueprint('delete_api', __name__)

#API to remove the page using the uid and admin password
@delete_api.route('/delete/<uid>/<urlAdminPassword>', methods=['POST'])
def removeEgg(uid, urlAdminPassword):
    
    #Retrieve Doc
    doc = database.getDBEntry(uid)
    if (doc == 0):
        result = render_template('error.html',message="404 Page Not Found - invalid Doc uid")
        objectstorage.os.close()
        return result
    
    #Set Variables From Doc
    try:
        docFileName = str(doc['filename']).lower()
        docAdminPassword = str(doc['admin_password'])
        docType = docTypeCheck(doc, uid)
    except:
        print "There was an issue setting up the variables for Document ID: %s" % uid
        result = render_template('error.html',message="500 Internal Server Error - Variables not defined")
        objectstorage.os.close()
        return result
    
    if (docAdminPassword != urlAdminPassword):
        result = render_template('error.html',message="403 Access Forbidden")
        
    elif (docAdminPassword == urlAdminPassword):
        try:
            if ((docFileName > "" and docFileName != "none") or docType == "file"):
                fileDeleteSuccess = deleteOSFile(docFileName,uid)
                result =  render_template('error.html',message=deleteDBDoc(doc,fileDeleteSuccess,uid))
            else:
                result = render_template('error.html',message=deleteDBDoc(doc,True,uid))
        except:
            result = render_template('error.html',message="500 Internal Server Error - A delete failed somplace")
            print "There was an exception processing the deletion of the Invalid Type Document ID: %s" % uid
    
    objectstorage.os.close()
    return result
    

def docTypeCheck(document, uid):
    print "docTypeCheck for ID: %s" % uid
    
    #Try to set the docType Variable
    try:
        docType = document['type'].lower()
    except:
        print "An exception occurred checking the docType for Document ID: %s" % uid
        return "invalid"
        
    if (docType == "file"):
        return "file"
    elif (docType == "text"):
        return "text"
    else:
        return "invalid"

#Delete Document from the DB
def deleteDBDoc(document,FileRemovalStatus,uid):
    if(FileRemovalStatus == True):
        try:
            database.db.delete(document)
            print "We have successfully deleted document with ID: %s" % uid
            return "Delete Successful"
        except:
            print "Something went wrong trying to delete the DB document associated with document ID: %s" % uid
            return "500 Internal Server Error - DB Delete Failed"
    else:
        return "500 Internal Server Error - Potential File Delete Failed"
        
def deleteOSFile(fileName,uid):
    print "filename: %s" % fileName
    try:
        objectstorage.deleteFile(fileName)
        print "We have successfully deleted the file associated with document ID: %s" % uid
        return True
    except:
        print "Something went wrong trying to delete the File associated with document ID: %s" % uid
        return False
