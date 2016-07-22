#Imports
import couchdb
import json

#Load in Properties
with open('NESTProperties.json') as properties_file:    
    data = json.load(properties_file)
    
dbConnectName = data["dbName"]
dbConnectUser = data["dbUser"]
dbConnectPassword = data["dbPassword"]


# Set DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % dbConnectUser)
couch.resource.credentials = (dbConnectUser, dbConnectPassword)


# Connect to DB to retrieve list of expired Eggs
db = couch[dbConnectName]


print db.info()
