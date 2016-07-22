#Imports
import couchdb
import json
from datetime import datetime
import swiftclient

#Load in Properties for DB and OS
with open('hatchProperties.json') as properties_file:    
    properties = json.load(properties_file)
    
dbConnectName = properties["dbName"]
dbConnectUser = properties["dbUser"]
dbConnectPassword = properties["dbPassword"]
osauth_url = properties["osauth_url"]
osauth_version = properties["osauth_version"]
ospassword = properties["ospassword"]
osproject_id = properties["osproject_id"]
osuser_id = properties["osuser_id"]
osregion_name = properties["osregion_name"]
oscontainer_name = properties["oscontainer_name"]

#Check if db doc is a file upload
def docTypeCheck(document):
    if (document['type'].lower() == "file"):
        return True
    else:
        return False

# Set up and establish DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % dbConnectUser)
couch.resource.credentials = (dbConnectUser, dbConnectPassword)
db = couch[dbConnectName]

# Set up and establish OS Connection
osConnection = swiftclient.Connection(key=ospassword, 
	authurl=osauth_url,  
	auth_version=osauth_version, 
	os_options={"project_id": osproject_id, 
				"user_id": osuser_id, 
				"region_name": osregion_name})

# Iterate through Eggs and delete expired ones
for id in db:
    doc = db.get(id)
    #Try to convert the expiration time to a datetime variable
    try:
        expirationTime = datetime.strptime(doc['expiration_time'], '%Y-%m-%d %H:%M:%S.%f')
    except:
        #Handle invalid formatted expiration times based on their document "Type"
        print "%s: Has an Invalid Format and is being handled now" % id
        if (docTypeCheck(doc) == True):
            try:
                osConnection.delete_object(oscontainer_name, str(doc['filename']))
                print "We have successfully deleted the file associated with document ID: %s" % id
            except:
                print "Something went wrong trying to delete the File associated with document ID: %s" % id
                continue
        try:
            db.delete(doc)
            print "We have successfully deleted document with ID: %s" % id
        except:
            print "Something went wrong trying to delete the DB document associated with document ID: %s" % id
            
        continue
    
    #Remove expired Eggs that have files associated with them
    if (expirationTime < datetime.utcnow() and docTypeCheck(doc) == True):
        ## Remove File from O.S. and delete DB doc
        try:
            osConnection.delete_object(oscontainer_name, str(doc['filename']))
            print "We have successfully deleted the file associated with document ID: %s" % id
            db.delete(doc)
            print "We have successfully deleted document with ID: %s" % id
        except:
            print "Something went wrong trying to delete the DB document or File associated with document ID: %s" % id
    
    #Remove expired Eggs that do not have files associated with them
    elif (expirationTime < datetime.utcnow() and docTypeCheck(doc) == False):
        try:
            db.delete(doc)
            print "We have successfully deleted document with ID: %s" % id
        except:
           print "There was an exception deleting the document with ID: %s" % id
           
osConnection.close()