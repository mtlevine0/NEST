#Imports
import couchdb
import json
import properties

# Set DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % properties.dbConnectUser)
couch.resource.credentials = (properties.dbConnectUser, properties.dbConnectPassword)

# Connect to DB to retrieve list of expired Eggs
db = couch[properties.dbConnectName]
