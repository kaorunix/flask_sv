# 木暮さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

page2_bp = Blueprint('page2_app', __name__, url_prefix='/api/page2')
