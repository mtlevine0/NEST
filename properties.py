import json

#Load in Properties
with open('NESTProperties.json') as properties_file:    
    data = json.load(properties_file)
    
dbConnectName = data["dbName"]
dbConnectUser = data["dbUser"]
dbConnectPassword = data["dbPassword"]