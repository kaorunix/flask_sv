# 椎谷割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

authority_bp = Blueprint('authority_app', __name__, url_prefix='/api/authority')
