#Imports
import couchdb
import json
import properties

# Set DB Connection
couch = couchdb.Server("https://%s.cloudant.com" % properties.dbConnectUser)
couch.resource.credentials = (properties.dbConnectUser, properties.dbConnectPassword)

# Connect to DB to retrieve list of expired Eggs
db = couch[properties.dbConnectName]

def getDBEntry(uid):
    doc = 0
    for id in database.db:
        if id == uid:
            doc = database.db.get(id)
    return doc


def updateDBEntry(doc):
    return database.db.save(doc)
    
    
def deleteDBEntry(doc):
    return database.db.delete(doc)