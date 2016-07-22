from flask import jsonify, Blueprint
import couchdb

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):
    return uid
