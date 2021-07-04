from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import AccountApi

system_account_id=999

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/account/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = AccountApi.getById(id, system_account_id)
    return account_json

@api_bp.route('/account/create/', methods=['POST'])
def createAccount():
    print("createAccount")
    payload = request.data.decode('utf-8')
    print(f"payload={payload}")
    response_json = AccountApi.create(payload, system_account_id)
    return jsonify(response_json)


class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}

api = Api(api_bp)
api.add_resource(Spam, '/spam')

