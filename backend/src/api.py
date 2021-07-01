from flask import Blueprint
from flask_restful import Api, Resource
from restapi import AccountApi

system_account_id=999

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/account/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = AccountApi.getById(id, system_account_id)
    return account_json


class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}

api = Api(api_bp)
api.add_resource(Spam, '/spam')

