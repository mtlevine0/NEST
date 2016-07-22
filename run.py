import os
from flask import Flask, render_template
from app import upload, delete, access

app = Flask(__name__, static_url_path='/static')
app.config['WTF_CSRF_ENABLED'] = False

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

port = os.getenv('PORT', '5000')

if __name__ == "__main__":
    app.register_blueprint(upload.upload_api)
    app.register_blueprint(delete.delete_api)
    app.register_blueprint(access.access_api)

    app.run(host='0.0.0.0', port=int(port), threaded=True, debug=True)
