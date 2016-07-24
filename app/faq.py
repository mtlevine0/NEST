from flask import Blueprint, render_template


faq_api = Blueprint('faq_api', __name__)

@faq_api.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')