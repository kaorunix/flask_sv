# 椎谷割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

authority2_bp = Blueprint('authority2_app', __name__, url_prefix='/api/authority2')
