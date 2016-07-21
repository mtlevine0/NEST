import os
from flask import Flask
from app import upload, delete, access

app = Flask(__name__, static_url_path='/static')

port = os.getenv('PORT', '5000')

if __name__ == "__main__":
    
    app.register_blueprint(upload.upload_api)
    app.register_blueprint(delete.delete_api)
    app.register_blueprint(access.access_api)

    app.run(host='0.0.0.0', port=int(port))
