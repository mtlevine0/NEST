import json

#Load in Properties
with open('NESTProperties.json') as properties_file:    
    data = json.load(properties_file)
    
dbConnectName = data["dbName"]
dbConnectUser = data["dbUser"]
dbConnectPassword = data["dbPassword"]
maxFileSize = data["maxFileSize"]
osauth_url = data["osauth_url"]
osauth_version = data["osauth_version"]
ospassword= data["ospassword"]
osproject_id= data["osproject_id"]
osuser_id= data["osuser_id"]
osregion_name= data["osregion_name"]
oscontainer_name= data["oscontainer_name"]