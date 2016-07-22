from flask import jsonify, Blueprint
import couchdb
import database

access_api = Blueprint('access_api', __name__)

@access_api.route('/<uid>', methods=['GET'])
def fetch(uid):
    data = {}
    for i, id in enumerate(database.db):
        print i, id
        data[i] = id
    return jsonify(data)
