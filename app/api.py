from flask import Blueprint, render_template

api_api = Blueprint('api_api', __name__)

@api_api.route('/api', methods=['GET'])
def api():
    return render_template('api.html')