from flask import Flask, request, jsonify,Blueprint
from flasgger import Swagger, swag_from
signup = Blueprint("signup", __name__)


@signup.route('/chat', methods=['POST'])
@swag_from('swagger_config.yml')
def chat():
    result={}
    data = request.get_json()
    marks=data['Marks']
    subject = data['Subject']
    if marks <33:
        result[subject]='fail'
    else:
        result[subject]='pass'

    return jsonify(result)  


@signup.route('/subject', methods=['POST'])
@swag_from('./swagger_config_subject.yml')
def total_subject():
    data = request.get_json()
    subject = data['Subject']
    

    return jsonify({'subject':subject})  

@signup.route("/audit/test", methods=["GET"])
def test_audit_connection():
    return "Successfully connected to audit API"


