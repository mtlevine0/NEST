from flask import Blueprint, render_template

about_api = Blueprint('about_api', __name__)

@about_api.route('/about', methods=['GET'])
def about():
    return render_template('about.html')