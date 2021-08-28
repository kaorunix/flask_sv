# 取出さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

project2_bp = Blueprint('project2_app', __name__, url_prefix='/api/project2')
