#Imports
import couchdb
import json

#Load in Properties
with open('hatchProperties.json') as properties_file:    
    data = json.load(properties_file)
    
print data
    
dbConnectName = "nw-nest-db-test"
dbConnectUser = "6bb93b4a-b32d-4fa9-ac34-81144d9bbb69-bluemix"
dbConnectPassword = "2d3848dd07d0ec8a0ae80672213d653b132861b4ffe5941fcf31cb50f0234a29"

# Set DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % dbConnectUser)
couch.resource.credentials = (dbConnectUser, dbConnectPassword)

# Connect to DB to retrieve list of expired Eggs
db = couch[dbConnectName]

print db.info()
