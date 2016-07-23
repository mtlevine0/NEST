#Imports
import couchdb
import json
import properties

# Set DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % properties.dbConnectUser)
couch.resource.credentials = (properties.dbConnectUser, properties.dbConnectPassword)

# Connect to DB to retrieve list of expired Eggs
db = couch[properties.dbConnectName]

# Fetch DB Doc
def getDBEntry(uid):
    doc = 0
    for id in db:
        if id == uid:
            doc = db.get(id)
    return doc
    
def updateDBEntry(doc):
    return db.save(doc)
    
def deleteDBEntry(doc):
    return db.delete(doc)