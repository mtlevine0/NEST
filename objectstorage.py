import swiftclient
import properties

# Set up and establish OS Connection
os = swiftclient.Connection(key=properties.ospassword, 
	authurl=properties.osauth_url,  
	auth_version=properties.osauth_version, 
	os_options={"project_id": properties.osproject_id, 
				"user_id": properties.osuser_id, 
				"region_name": properties.osregion_name})
				
def deleteFile(fileName):
    os.delete_object(properties.oscontainer_name, fileName)